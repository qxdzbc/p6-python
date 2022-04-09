from abc import ABC
from typing import Optional, Union, Tuple

from com.emeraldblast.p6.document_structure.cell.Cell import Cell
from com.emeraldblast.p6.document_structure.cell.address.CellAddress import CellAddress
from com.emeraldblast.p6.document_structure.range.Range import Range
from com.emeraldblast.p6.document_structure.range.address.RangeAddress import RangeAddress


class RangeWrapper(Range,ABC):
    
    def __init__(self, innerRange:Range):
        self._innerRange = innerRange
    
    @property
    def firstCellAddress(self) -> CellAddress:
        return self._innerRange.firstCellAddress

    @property
    def lastCellAddress(self) -> CellAddress:
        return self._innerRange.lastCellAddress

    def cell(self, address: Union[str, CellAddress, Tuple[int, int]]) -> Cell:
        return self._innerRange.cell(address)

    def addCell(self, cell: Cell):
        self._innerRange.addCell(cell)

    def deleteCell(self, address: CellAddress):
        self._innerRange.deleteCell(address)

    def getOrMakeCell(self, address: CellAddress) -> Cell:
        return self._innerRange.getOrMakeCell(address)

    def hasCellAt(self, address: CellAddress) -> bool:
        return self._innerRange.hasCellAt(address)

    def getCell(self, address: CellAddress) -> Optional[Cell]:
        return self._innerRange.getCell(address)

    def isEmpty(self) -> bool:
        return self._innerRange.isEmpty()

    @property
    def cells(self) -> list[Cell]:
        return self._innerRange.cells

    @property
    def rangeAddress(self) -> RangeAddress:
        return self._innerRange.rangeAddress