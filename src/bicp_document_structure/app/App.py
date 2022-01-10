from abc import ABC
from typing import Optional, Union

from bicp_document_structure.app.run_result.RunResult import RunResult
from bicp_document_structure.workbook.WorkBook import Workbook


class App(ABC):
    """
    this class represents the state of the app.
    """
    @property
    def result(self)->RunResult:
        raise NotImplementedError()

    @property
    def activeWorkbook(self) -> Optional[Workbook]:
        raise NotImplementedError()

    def setActiveWorkbook(self, indexOrName: Union[int, str]):
        """
        Set workbook at indexOrName the active workbook.
        Should raise an exception if the indexOrName is invalid
        """
        raise NotImplementedError()

    @property
    def activeSheet(self):
        raise NotImplementedError()

    def getWorkbookByIndex(self, index: int) -> Optional[Workbook]:
        """:return workbook at an index"""
        raise NotImplementedError()

    def hasNoWorkbook(self) -> bool:
        """
        :return: true if this app does not have any workbook
        """
        raise NotImplementedError()

    def createNewWorkBook(self, name: str):
        """create a new workbook, and add it to this app state"""
        raise NotImplementedError()

    def saveWorkbook(self, nameOrIndex: Union[int, str], filePath: str):
        """save a workbook at nameOrIndex to a certain filePath"""
        raise NotImplementedError()

    def loadWorkbook(self, filePath: str) -> bool:
        """load a workbook from a file path, and add it to this app state"""
        raise NotImplementedError()
