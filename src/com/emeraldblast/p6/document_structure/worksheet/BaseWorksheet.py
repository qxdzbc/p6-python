import json
from abc import ABC

from com.emeraldblast.p6.proto.DocProtos_pb2 import WorksheetProto

from com.emeraldblast.p6.document_structure.cell.address.CellAddress import CellAddress
from com.emeraldblast.p6.document_structure.copy_paste.Paster import Paster
from com.emeraldblast.p6.document_structure.range.Range import Range
from com.emeraldblast.p6.document_structure.range.address.RangeAddress import RangeAddress
from com.emeraldblast.p6.document_structure.range.address.RangeAddresses import RangeAddresses
from com.emeraldblast.p6.document_structure.util.result.Results import Results
from com.emeraldblast.p6.document_structure.worksheet.Worksheet import Worksheet


class BaseWorksheet(Worksheet,ABC):


    @property
    def usedRangeAddress(self) -> RangeAddress | None:
        if self.minUsedCol and self.maxUsedCol and self.minUsedRow and self.maxUsedRow:
            return RangeAddresses.fromColRow(
                minCol = self.minUsedCol,
                maxCol = self.maxUsedCol,
                minRow = self.minUsedRow,
                maxRow = self.maxUsedRow,
            )
        else:
            return None

    @property
    def usedRange(self) -> Range | None:
        if self.usedRangeAddress:
            return self.range(self.usedRangeAddress)
        else:
            return None

    def pasteDataFrameFromClipboard(self, anchorCell: CellAddress):
        rs = self.pasteDataFrameFromClipboardRs(anchorCell)
        Results.extractOrRaise(rs)


    def pasteProtoFromClipboard(self, anchorCell: CellAddress, paster: Paster | None = None):
        rs = self.pasteProtoFromClipboardRs(anchorCell, paster)
        Results.extractOrRaise(rs)



    def compareWith(self, ws2: Worksheet) -> bool:
        """compare all cell of this sheet with another. Very inefficient, use with care"""
        ws1 = self.rootWorksheet
        ws2 = ws2.rootWorksheet
        sameName = ws1.name == ws2.name
        if sameName:
            sameCellCount = ws1.cellCount == ws1.cellCount
            if sameCellCount:
                z = True
                for c1 in ws1.cells:
                    c2 = ws2.cell(c1.address)
                    if c1 != c2:
                        return False

                for c2 in ws2.cells:
                    c1 = ws1.cell(c2.address)
                    if c2 != c1:
                        return False
                return z
            else:
                return False
        else:
            return False

    @property
    def cellCount(self):
        return self.size


    def toProtoObj(self) -> WorksheetProto:
        rt = WorksheetProto()
        rt.name = self.name
        cells = []
        for cell in self.cells:
            cells.append(cell.toProtoObj())
        rt.cell.extend(cells)
        return rt

    def removeFromWorkbook(self):
        self.workbook = None


    def reportJsonStr(self) -> str:
        return json.dumps({
            "name": self.name
        })

    def rename(self, newName: str):
        rs = self.renameRs(newName)
        if rs.isErr():
            raise rs.err.toException()

