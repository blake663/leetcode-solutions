# Last updated: 11/10/2025, 8:00:06 PM
class Spreadsheet:

    def __init__(self, rows: int):
        self.table = {}

    def setCell(self, cell: str, value: int) -> None:
        self.table[cell] = value

    def resetCell(self, cell: str) -> None:
        if cell in self.table:
            del self.table[cell]

    def getValue(self, formula: str) -> int:
        res = 0
        for val in formula[1:].split('+'):
            if val[0].isalpha():
                res += self.table.get(val, 0)
            else:
                res += int(val)
        
        return res


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)