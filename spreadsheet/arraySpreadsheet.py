from spreadsheet.cell import Cell
from spreadsheet.baseSpreadsheet import BaseSpreadsheet
import time

# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Array-based spreadsheet implementation.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2023, RMIT University'
# ------------------------------------------------------------------------

class ArraySpreadsheet(BaseSpreadsheet):

    def __init__(self):
        # TO BE IMPLEMENTED
        self.spreadsheet = [[None]]
        self.rows = 0
        self.built = False
        self.columns = 0
        pass


    def buildSpreadsheet(self, lCells: [Cell]):
        """
        Construct the data structure to store nodes.
        @param lCells: list of cells to be stored
        """
        start = time.perf_counter()
        for cell in lCells:
            # extend number of rows
            if self.rows < cell.row:
                for i in range(cell.row - self.rows):
                    # append a row with corresponding columns
                    # we add 1 because indexes start at 0
                    self.spreadsheet.append([None] * (self.colNum()))
                self.rows = cell.row
            
            # extend number of columns
            if self.columns < cell.col:
                diff = cell.col - self.columns
                for i in range(self.rowNum()):
                    self.spreadsheet[i].extend([None] * diff)
                self.columns = cell.col
            
            # print(len(self.spreadsheet), "x", len(self.spreadsheet[0]), cell.row, cell.col)
            # for thing in self.spreadsheet:
            #     print(len(thing))
            # print(len(self.spreadsheet[cell.row]))
            self.spreadsheet[cell.row][cell.col] = cell.val
        end = time.perf_counter()
        timeTaken = end - start
        with open("gae.txt", "a") as f:
            f.write("For creating a array: " +str(timeTaken) + " of size " + str(self.rowNum()) + "x" + str(self.colNum())+"\n")
        f.close()
        self.built = True


    def appendRow(self)->bool:
        """
        Appends an empty row to the spreadsheet.

        @return True if operation was successful, or False if not.
        """
        start = time.perf_counter()
        if self.spreadsheet == None:
            end = time.perf_counter()
            timeTaken = end - start
            with open("gae.txt", "a") as f:
                f.write("For appending row" +str(timeTaken))
            f.close()
            return False
        else:
            self.rows += 1
            self.spreadsheet.append([None] * (self.rows + 1))
            end = time.perf_counter()
            timeTaken = end - start
            with open("gae.txt", "a") as f:
                f.write("For appending row: " +str(timeTaken)+"\n")
            f.close()
            return True


    def appendCol(self)->bool:
        """
        Appends an empty column to the spreadsheet.

        @return True if operation was successful, or False if not.
        """
        start = time.perf_counter()
        if self.spreadsheet == None:
            end = time.perf_counter()
            timeTaken = end - start
            with open("gae.txt", "a") as f:
                f.write("For appending col" +str(timeTaken))
            f.close()
            return False
        else:
            self.columns += 1
            for row in self.spreadsheet:
                row.extend([None])
            end = time.perf_counter()
            timeTaken = end - start
            with open("gae.txt", "a") as f:
                f.write("For appending col: " +str(timeTaken)+"\n")
            f.close()
            return True


    def insertRow(self, rowIndex: int)->bool:
        """
        Inserts an empty row into the spreadsheet.

        @param rowIndex Index of the existing row that will be after the newly inserted row.  If inserting as first row, specify rowIndex to be 0.  If inserting a row after the last one, specify rowIndex to be rowNum()-1.

        @return True if operation was successful, or False if not, e.g., rowIndex is invalid.
        """
        start = time.perf_counter()
        if rowIndex < -1 or rowIndex >= self.rowNum():
            return False
        else:
            # IR 0 will insert a row AFTER row 0
            self.spreadsheet.insert(rowIndex + 1, [None] * self.columns)
            self.rows += 1
            end = time.perf_counter()
            timeTaken = end - start
            with open("gae.txt", "a") as f:
                f.write("For insert row: " +str(timeTaken)+"\n")
            f.close()
            return True


    def insertCol(self, colIndex: int)->bool:
        """
        Inserts an empty column into the spreadsheet.

        @param colIndex Index of the existing column that will be after the newly inserted row.  If inserting as first column, specify colIndex to be 0.  If inserting a column after the last one, specify colIndex to be colNum()-1.

        return True if operation was successful, or False if not, e.g., colIndex is invalid.
        """
        start = time.perf_counter()
        if colIndex < -1 or colIndex >= self.colNum():
            return False
        else:
            for row in self.spreadsheet:
                row.insert(colIndex + 1, None)
            self.columns += 1
            end = time.perf_counter()
            timeTaken = end - start
            with open("gae.txt", "a") as f:
                f.write("For insert col: " +str(timeTaken)+"\n")
            f.close()
            return True


    def update(self, rowIndex: int, colIndex: int, value: float) -> bool:
        """
        Update the cell with the input/argument value.

        @param rowIndex Index of row to update.
        @param colIndex Index of column to update.
        @param value Value to update.  Can assume they are floats.

        @return True if cell can be updated.  False if cannot, e.g., row or column indices do not exist.
        """
        start = time.perf_counter()
        if rowIndex < -1 or rowIndex >= self.rowNum() or colIndex < -1 or colIndex >= self.colNum():
            return False
        else:
            self.spreadsheet[rowIndex][colIndex] = value
            end = time.perf_counter()
            timeTaken = end - start
            with open("gae.txt", "a") as f:
                f.write("For update: " +str(timeTaken)+"\n")
            f.close()
            return True


    def rowNum(self)->int:
        """
        @return Number of rows the spreadsheet has.
        """
        start = time.perf_counter()
        # Add 1 because indexing starts at 0
        end = time.perf_counter()
        timeTaken = end - start
        if self.built:
            with open("gae.txt", "a") as f:
                f.write("For rowNum: " +str(timeTaken)+"\n")
            f.close()
        return len(self.spreadsheet)


    def colNum(self)->int:
        """
        @return Number of column the spreadsheet has.
        """
        start = time.perf_counter()
        end = time.perf_counter()
        timeTaken = end - start
        if self.built:
            with open("gae.txt", "a") as f:
                f.write("For colNum: " +str(timeTaken)+"\n")
            f.close()
        return self.columns + 1



    def find(self, value: float) -> [(int, int)]:
        """
        Find and return a list of cells that contain the value 'value'.

        @param value value to search for.

        @return List of cells (row, col) that contains the input value.
	    """
        start = time.perf_counter()
        matches = []
        curr_row = 0
        
        for row in self.spreadsheet:
            curr_col = 0
            for val in row:
                if val == value:
                    matches.append((curr_row, curr_col))
                curr_col += 1
            curr_row += 1

        # REPLACE WITH APPROPRIATE RETURN VALUE
        end = time.perf_counter()
        timeTaken = end - start
        with open("gae.txt", "a") as f:
            f.write("For find: " +str(timeTaken)+"\n")
        f.close()
        return matches

    def entries(self) -> [Cell]:
        """
        @return A list of cells that have values (i.e., all non None cells).
        """
        start = time.perf_counter()
        matches = []
        curr_row = 0
        
        for row in self.spreadsheet:
            curr_col = 0
            for val in row:
                if val != None:
                    matches.append(Cell(curr_row, curr_col, val))
                curr_col += 1
            curr_row += 1
        end = time.perf_counter()
        timeTaken = end - start
        with open("gae.txt", "a") as f:
            f.write("For entries: " +str(timeTaken)+"\n")
        f.close()
        return matches
