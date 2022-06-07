from pathlib import Path
from typing import Union

from com.emeraldblast.p6.document_structure.cell.Cells import Cells
from com.emeraldblast.p6.document_structure.file.P6Files import P6Files
from com.emeraldblast.p6.document_structure.workbook import WorkbookJson
from com.emeraldblast.p6.document_structure.workbook.WorkBook import Workbook
from com.emeraldblast.p6.document_structure.workbook.WorkbookImp import WorkbookImp
from com.emeraldblast.p6.document_structure.worksheet.Worksheet import Worksheet
from com.emeraldblast.p6.document_structure.worksheet.Worksheets import Worksheets
from com.emeraldblast.p6.proto.DocProtos_pb2 import WorkbookProto


class Workbooks:

    @staticmethod
    def fromProto(proto: WorkbookProto, filePath: Path | None = None) -> Workbook:
        wbName = proto.workbookKey.name
        wb = WorkbookImp(
            name = wbName,
            path = filePath
        )
        for wsProto in proto.worksheet:
            ws:Worksheet = Worksheets.fromProto(wsProto,wb)
            wb.addWorksheet(ws)
        return wb

    @staticmethod
    def wbFromJson(wbJson: WorkbookJson, filePath: Union[Path, None] = None) -> Workbook:
        path = filePath
        if filePath is None:
            if wbJson.path is None:
                path = P6Files.defaultPath
            else:
                path = Path(wbJson.path)

        wb = WorkbookImp(
            name = str(path.name),
            path = path,
        )

        for sheetJson in wbJson.worksheets:
            sheet: Worksheet = wb.createNewWorksheet(sheetJson.name)
            for cellJson in sheetJson.cells:
                dummyCell = Cells.cellFromJson(cellJson)
                realCell = sheet.cell(dummyCell.address)
                realCell.copyFrom(dummyCell)
        return wb
