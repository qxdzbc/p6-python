import json
from abc import ABC
from pathlib import Path
from typing import Optional, Union

from google.protobuf.struct_pb2 import NullValue

from bicp_document_structure.formula_translator.FormulaTranslator import FormulaTranslator
from bicp_document_structure.message.proto.Common_pb2 import NullableString
from bicp_document_structure.message.proto.DocProto_pb2 import WorkbookProto
from bicp_document_structure.util.CanCheckEmpty import CanCheckEmpty
from bicp_document_structure.util.ToJson import ToJson
from bicp_document_structure.util.ToProto import ToProto
from bicp_document_structure.util.Util import default
from bicp_document_structure.util.report.error.ErrorReport import ErrorReport
from bicp_document_structure.util.result.Result import Result
from bicp_document_structure.workbook.WorkbookJson import WorkbookJson
from bicp_document_structure.workbook.key.WorkbookKey import WorkbookKey
from bicp_document_structure.worksheet.Worksheet import Worksheet


class Workbook(ToJson, CanCheckEmpty, ToProto[WorkbookProto], ABC):

    def getIndexOfWorksheet(self, sheetName: str) -> int:
        for (index, sheet) in enumerate(self.worksheets):
            if sheet.name == sheetName:
                return index
        return -1

    def toProtoObj(self) -> WorkbookProto:
        rt = WorkbookProto()
        rt.name = default(self.name, "")
        pathStr = NullableString()
        if self.path is None:
            pathStr.null = NullValue.NULL_VALUE
        else:
            pathStr.str = str(self.path.absolute())
        rt.path.CopyFrom(pathStr)
        sheets = []
        for sheet in self.worksheets:
            sheets.append(sheet.toProtoObj())
        rt.worksheet.extend(sheets)
        return rt

    def getTranslator(self, sheetName: str) -> FormulaTranslator:
        raise NotImplementedError()

    def haveSheet(self, sheetName: str) -> bool:
        return self.getWorksheetOrNone(sheetName) is not None

    def reRun(self):
        """rerun all worksheet in this workbook"""
        for sheet in self.worksheets:
            sheet.reRun()

    def renameWorksheet(self, oldSheetNameOrIndex: str | int, newSheetName: str):
        rs = self.renameWorksheetRs(oldSheetNameOrIndex, newSheetName)
        if rs.isErr():
            raise rs.err.toException()

    def renameWorksheetRs(self, oldSheetNameOrIndex: str | int, newSheetName: str) -> Result[None, ErrorReport]:
        raise NotImplementedError()

    @property
    def worksheets(self) -> list[Worksheet]:
        """return a list of all sheet in this workbook"""
        raise NotImplementedError()

    @property
    def workbookKey(self) -> WorkbookKey:
        raise NotImplementedError()

    @workbookKey.setter
    def workbookKey(self, newKey: WorkbookKey):
        raise NotImplementedError()

    @property
    def activeWorksheet(self) -> Optional[Worksheet]:
        raise NotImplementedError()

    def setActiveWorksheet(self, indexOrName: Union[int, str]):
        raise NotImplementedError()

    def getWorksheetByName(self, name: str) -> Worksheet:
        """
        :param name: sheet name
        :return: the sheet having that name or None if no such sheet exists
        """
        raise NotImplementedError()

    def getWorksheetByNameRs(self, name: str) -> Result[Worksheet, ErrorReport]:
        raise NotImplementedError()

    def getWorksheetByIndexRs(self, index: int) -> Result[Worksheet, ErrorReport]:
        raise NotImplementedError()

    def getWorksheetRs(self, nameOrIndex: Union[str, int]) -> Result[Worksheet, ErrorReport]:
        raise NotImplementedError()

    def getWorksheetByNameOrNone(self, name: str) -> Worksheet | None:
        """
        :param name: sheet name
        :return: the sheet having that name or None if no such sheet exists
        """
        raise NotImplementedError()

    def getWorksheetByIndex(self, index: int) -> Worksheet:
        """
        :param index: index of a sheet
        :return: the sheet at that index, or None if no such sheet exists
        """
        raise NotImplementedError()

    def getWorksheetByIndexOrNone(self, index: int) -> Optional[Worksheet]:
        """
        :param index: index of a sheet
        :return: the sheet at that index, or None if no such sheet exists
        """
        raise NotImplementedError()

    def getWorksheetOrNone(self, nameOrIndex: Union[str, int]) -> Optional[Worksheet]:
        raise NotImplementedError()

    def getWorksheet(self, nameOrIndex: Union[str, int]) -> Worksheet:
        """
        get a sheet either by name or index
        :param nameOrIndex: name or index
        :return: the sheet at that index/name, or None if no such sheet exists
        """
        raise NotImplementedError()

    @property
    def sheetCount(self) -> int:
        raise NotImplementedError()

    @property
    def name(self) -> str:
        raise NotImplementedError()

    @name.setter
    def name(self, newName: str):
        raise NotImplementedError()

    @property
    def path(self) -> Path:
        raise NotImplementedError()

    @path.setter
    def path(self, newPath: Path):
        raise NotImplementedError()

    def createNewWorksheet(self, newSheetName: Optional[str]) -> Worksheet:
        """
        add a new empty sheet to this workbook
        :param newSheetName: name of the new sheet
        :return the new worksheet
        :raise ValueError if the newSheetName already exists
        """
        createRs = self.createNewWorksheetRs(newSheetName)
        if createRs.isOk():
            return createRs.value
        else:
            raise createRs.err.toException()

    def createNewWorksheetRs(self, newSheetName: Optional[str] = None) -> Result[Worksheet, ErrorReport]:
        """
        add a new empty sheet to this workbook
        :param newSheetName: name of the new sheet
        :return Result object containing the new worksheet or ErrorRepor
        """
        raise NotImplementedError()

    def removeWorksheetByName(self, sheetName: str) -> Optional[Worksheet]:
        """ remove sheet by name. If the target sheet does not exist, simply return"""
        removeRs = self.removeWorksheetByNameRs(sheetName)
        if removeRs.isOk():
            return removeRs.value
        else:
            raise removeRs.err.toException()

    def removeWorksheetByIndex(self, index: int) -> Optional[Worksheet]:
        """ remove sheet by index. If the target sheet does not exist, simply return"""
        removeRs = self.removeWorksheetByIndexRs(index)
        if removeRs.isOk():
            return removeRs.value
        else:
            raise removeRs.err.toException()

    def removeWorksheet(self, nameOrIndex: Union[str, int]) -> Optional[Worksheet]:
        """ remove sheet by either index or name. If the target sheet does not exist, simply return"""
        removeRs = self.removeWorksheetRs(nameOrIndex)
        if removeRs.isOk():
            return removeRs.value
        else:
            raise removeRs.err.toException()

    def removeWorksheetByNameRs(self, sheetName: str) -> Result[Worksheet, ErrorReport]:
        """ remove sheet by name. If the target sheet does not exist, simply return"""
        raise NotImplementedError()

    def removeWorksheetByIndexRs(self, index: int) -> Result[Worksheet, ErrorReport]:
        """ remove sheet by index. If the target sheet does not exist, simply return"""
        raise NotImplementedError()

    def removeWorksheetRs(self, nameOrIndex: Union[str, int]) -> Result[Worksheet, ErrorReport]:
        """ remove sheet by either index or name. If the target sheet does not exist, simply return"""
        raise NotImplementedError()

    def toJson(self) -> WorkbookJson:
        jsons = []
        for sheet in self.worksheets:
            jsons.append(sheet.toJson())
        pathJson = None
        if self.workbookKey.filePath is not None:
            pathJson = str(self.workbookKey.filePath)
        return WorkbookJson(self.name, pathJson, jsons)

    def listWorksheet(self) -> str:
        """return a list of sheet as string"""
        rt = ""
        for (i, sheet) in enumerate(self.worksheets):
            rt += "{num}. {sheetName}\n".format(
                num = str(i),
                sheetName = sheet.name
            )
        if not rt:
            rt = "empty book"
        print(rt)

    def reportJsonStr(self) -> str:
        return json.dumps(self.toJson().toJsonDict())

    def toJsonStrForSaving(self) -> str:
        return self.toJson().toJsonStrForSaving()
