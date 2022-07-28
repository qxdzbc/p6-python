from dataclasses import dataclass
from typing import Optional

from com.emeraldblast.p6.document_structure.util.ToProto import ToProto, P
from com.emeraldblast.p6.document_structure.workbook.WorkBook import Workbook
from com.emeraldblast.p6.document_structure.worksheet.Worksheet import Worksheet
from com.emeraldblast.p6.document_structure.worksheet.Worksheets import Worksheets
from com.emeraldblast.p6.proto.service.workbook.GetWorksheetResponseProto_pb2 import GetWorksheetResponseProto

@dataclass
class GetWorksheetResponse(ToProto[GetWorksheetResponseProto]):
    worksheet:Optional[Worksheet] = None

    def toProtoObj(self) -> GetWorksheetResponseProto:
        ws = None
        if self.worksheet:
            ws = self.worksheet.toProtoObj()
        return GetWorksheetResponseProto(
            worksheet = ws
        )
    @staticmethod
    def fromProto(proto:GetWorksheetResponseProto,wb:Workbook = None):
        ws = None
        if proto.HasField("worksheet"):
            ws = Worksheets.fromProto(proto.worksheet,wb)
        return GetWorksheetResponse(worksheet = ws)