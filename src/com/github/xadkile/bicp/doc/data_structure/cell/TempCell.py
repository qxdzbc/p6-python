from com.github.xadkile.bicp.doc.data_structure.cell.Cell import Cell
from com.github.xadkile.bicp.doc.data_structure.cell.DataCell import DataCell
from com.github.xadkile.bicp.doc.data_structure.cell.position.CellPosition import CellPosition
from com.github.xadkile.bicp.doc.data_structure.cell.position.IndexCellPosition import IndexCellPosition
from com.github.xadkile.bicp.doc.data_structure.cell_holder.CellHolder import CellHolder


class TempCell(Cell):

    """
    act as a temporary cell returned by querying non-existing cell from a CellHolder.
    Only write object to the holder when the content of the temp cell is mutated.
    """

    def __init__(self, holder: CellHolder, position:CellPosition):
        self.__pos = position
        self.__colIndex = position.getColIndex()
        self.__rowIndex = position.getRowIndex()
        self.__holder = holder
        self.__innerCell = None
        self.__cellWritten = False
        if holder.hasCellAt(position):
            self.__innerCell = holder.getCell(position)
            self.__cellWritten = True
        else:
            self.__innerCell = DataCell(position)
            self.__cellWritten=False

    @property
    def value(self):
        return self.__innerCell.value

    @value.setter
    def value(self, newValue):
        self.__innerCell.value = newValue
        self.__writeCell()

    @property
    def code(self) -> str:
        return self.__innerCell.code

    @code.setter
    def code(self,newCode:str):
        self.__innerCell.code = newCode
        self.__writeCell()

    def __writeCell(self):
        if not self.__cellWritten:
            self.__holder.setCell(self.__pos,self.__innerCell)
            self.__cellWritten = True