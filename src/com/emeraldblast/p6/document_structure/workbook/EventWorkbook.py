from typing import Callable, Optional, Union

from com.emeraldblast.p6.document_structure.communication.event.data_structure.common.ErrorIndicator import \
    ErrorIndicator

from com.emeraldblast.p6.document_structure.script.ScriptEntry import ScriptEntry

from com.emeraldblast.p6.document_structure.communication.event.data_structure.app_event.SetActiveWorksheetResponse import \
    SetActiveWorksheetResponse
from com.emeraldblast.p6.document_structure.communication.event.data_structure.script_event.new_script.NewScriptNotification import \
    NewScriptNotification
from com.emeraldblast.p6.document_structure.communication.event.data_structure.workbook_event.CreateNewWorksheetResponse import \
    CreateNewWorksheetResponse
from com.emeraldblast.p6.document_structure.communication.event.data_structure.workbook_event.DeleteWorksheetResponse import \
    DeleteWorksheetResponse
from com.emeraldblast.p6.document_structure.communication.notifier.eventData.EventData import EventData
from com.emeraldblast.p6.document_structure.communication.reactor import EventReactorContainer
from com.emeraldblast.p6.document_structure.script.ScriptEntryKey import ScriptEntryKey
from com.emeraldblast.p6.document_structure.util.report.error.ErrorReport import ErrorReport
from com.emeraldblast.p6.document_structure.util.result.Ok import Ok
from com.emeraldblast.p6.document_structure.util.result.Result import Result
from com.emeraldblast.p6.document_structure.workbook.WorkBook import Workbook
from com.emeraldblast.p6.document_structure.workbook.WorkbookWrapper import WorkbookWrapper
from com.emeraldblast.p6.document_structure.worksheet.EventWorksheet import EventWorksheet
from com.emeraldblast.p6.document_structure.worksheet.Worksheet import Worksheet


class EventWorkbook(WorkbookWrapper):
    """
    The reason EventReactorContainer is not injected here directly because they can
    """

    def __init__(self, innerWorkbook: Workbook,
                 onCellEvent: Callable[[EventData], None] = None,
                 onWorksheetEvent: Callable[[EventData], None] = None,
                 onRangeEvent: Callable[[EventData], None] = None,
                 onWorkbookEvent: Callable[[EventData], None] = None,
                 onOtherEvent: Callable[[EventData], None] = None,
                 onScriptEvent:Callable[[EventData], None] = None,
                 ):
        super().__init__(innerWorkbook)
        self.__onCellChange: Callable[[EventData], None] = onCellEvent
        self.__onWorksheetEvent: Callable[[EventData], None] = onWorksheetEvent
        self.__onRangeEvent: Callable[[EventData], None] = onRangeEvent
        self.__onWorkbookEvent: Callable[[EventData], None] = onWorkbookEvent
        self.__onOtherEvent: Callable[[EventData], None] = onOtherEvent
        self.__onScriptEvent: Callable[[EventData], None] = onScriptEvent

        self._iwb = self._innerWorkbook

    @staticmethod
    def create(innerWorkbook: Workbook, reactorContainer: EventReactorContainer) -> 'EventWorkbook':

        def triggerEventReactor(data: EventData):
            reactorContainer.triggerReactorsFor(data.event, data)

        return EventWorkbook(
            innerWorkbook = innerWorkbook,
            onCellEvent = triggerEventReactor,
            onWorksheetEvent = triggerEventReactor,
            onRangeEvent = triggerEventReactor,
            onWorkbookEvent = triggerEventReactor,
            onOtherEvent = triggerEventReactor,
            onScriptEvent = triggerEventReactor,
        )

    def _makeScriptEntry(self,name,script)->ScriptEntry:
        return ScriptEntry(
            key = ScriptEntryKey(
                name = name,
                workbookKey = self.workbookKey
            ),
            script = script
        )

    def addScriptRs(self, name: str, script: str) -> Result[None, ErrorReport]:
        rs= self.rootWorkbook.addScriptRs(name, script)
        notif = None
        if rs.isOk():
            notif = NewScriptNotification(
                scriptEntries = [
                    self._makeScriptEntry(name,script)
                ],
                errorIndicator = ErrorIndicator.noError()
            )
        else:
            notif = NewScriptNotification(
                scriptEntries = [],
                errorIndicator = ErrorIndicator.error(rs.err)
            )
        self.__onScriptEvent(notif.toEventData())
        return rs

    @property
    def worksheets(self) -> list[Worksheet]:
        """wrap the result worksheets in event worksheet, so that they can propagate event"""
        sheets = self._innerWorkbook.worksheets
        rt = list(map(lambda s: self.__wrapInEventWorksheet(s), sheets))
        return rt

    @property
    def activeWorksheet(self) -> Optional[Worksheet]:
        """wrap the result worksheet in event worksheet, so that it can propagate event"""
        activeSheet = self._innerWorkbook.activeWorksheet
        return self.__wrapInEventWorksheet(activeSheet)

    def __handleWsRs(self, rs: Result[Worksheet, ErrorReport]):
        if rs.isOk():
            return Ok(self.__wrapInEventWorksheet(rs.value))
        else:
            return rs

    def getWorksheetByNameRs(self, name: str) -> Result[Worksheet, ErrorReport]:
        rs = self._iwb.getWorksheetByNameRs(name)
        return self.__handleWsRs(rs)

    def getWorksheetByIndexRs(self, index: int) -> Result[Worksheet, ErrorReport]:
        rs = self._iwb.getWorksheetByIndexRs(index)
        return self.__handleWsRs(rs)

    def getWorksheetRs(self, nameOrIndex: Union[str, int]) -> Result[Worksheet, ErrorReport]:
        rs = self._iwb.getWorksheetRs(nameOrIndex)
        return self.__handleWsRs(rs)

    def createNewWorksheet(self, newSheetName: Optional[str]) -> Worksheet:
        rs = self.createNewWorksheetRs(newSheetName)
        if rs.isOk():
            return rs.value
        else:
            raise rs.err.toException()

    def createNewWorksheetRs(self, newSheetName: Optional[str] = None) -> Result[Worksheet, ErrorReport]:
        rs = self._iwb.createNewWorksheetRs(newSheetName)

        name = str(newSheetName)
        if rs.isOk():
            name = rs.value.name

        if rs.isOk():
            newWorksheet = rs.value
            if self.__onWorkbookEvent is not None:
                res = CreateNewWorksheetResponse(self.workbookKey, name)
                self.__onWorkbookEvent(res.toEventData())
            return Ok(self.__wrapInEventWorksheet(newWorksheet))
        else:
            if self.__onWorkbookEvent is not None:
                errReport: ErrorReport = rs.err
                res = CreateNewWorksheetResponse(
                    workbookKey = self.workbookKey,
                    newWorksheetName = name,
                    isError = True,
                    errorReport = errReport)
                self.__onWorkbookEvent(res.toEventData())
            return rs

    def __wrapInEventWorksheet(self, sheet: Worksheet) -> Worksheet:
        def onRangeEvent(data: EventData):
            if self.__onRangeEvent is not None:
                self.__onRangeEvent(data)

        def onCellEvent(eventData: EventData):
            if self.__onCellChange is not None:
                self.__onCellChange(eventData)

        def onSheetEvent(data: EventData):
            if self.__onWorksheetEvent is not None:
                self.__onWorksheetEvent(data)

        # update rename function
        return EventWorksheet(
            innerWorksheet = sheet,
            onCellEvent = onCellEvent,
            onWorksheetEvent = onSheetEvent,
            onRangeEvent = onRangeEvent)

    def deleteWorksheetByNameRs(self, sheetName: str) -> Result[Worksheet, ErrorReport]:
        rs = self._iwb.deleteWorksheetByNameRs(sheetName)
        response = DeleteWorksheetResponse(
            workbookKey = self.workbookKey,
            isError = rs.isErr()
        )

        if rs.isOk():
            response.targetWorksheet = sheetName

        if rs.isErr():
            response.errorReport = rs.err

        self.__onWorkbookEvent(response.toEventData())
        return rs

    def deleteWorksheetByIndexRs(self, index: int) -> Result[Worksheet, ErrorReport]:
        rs = self._iwb.deleteWorksheetByIndexRs(index)
        response = DeleteWorksheetResponse(
            workbookKey = self.workbookKey,
            isError = rs.isErr()
        )
        if rs.isOk():
            response.targetWorksheet = rs.value.name
        if rs.isErr():
            response.errorReport = rs.err
        self.__onWorkbookEvent(response.toEventData())
        return rs

    def setActiveWorksheetRs(self, indexOrName: Union[int, str]) -> Result[Worksheet, ErrorReport]:
        rs = self._iwb.setActiveWorksheetRs(indexOrName)

        response = SetActiveWorksheetResponse(
            workbookKey = self.workbookKey,
        )
        if rs.isOk():
            ws = rs.value
            response.worksheetName = ws.name
        else:
            response.worksheetName = indexOrName
            response.isError = True
            response.errorReport = rs.err

        self.__onOtherEvent(response.toEventData())
        return rs
