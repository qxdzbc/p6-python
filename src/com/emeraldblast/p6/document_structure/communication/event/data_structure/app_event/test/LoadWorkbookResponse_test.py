import unittest

from com.emeraldblast.p6.document_structure.communication.event.P6Events import P6Events
from com.emeraldblast.p6.document_structure.communication.event.data_structure.app_event.LoadWorkbookResponse import \
    LoadWorkbookResponse
from com.emeraldblast.p6.document_structure.util.report.error.ErrorHeader import ErrorHeader
from com.emeraldblast.p6.document_structure.util.report.error.ErrorReport import ErrorReport
from com.emeraldblast.p6.document_structure.workbook.WorkbookImp import WorkbookImp
from com.emeraldblast.p6.proto.AppEventProtos_pb2 import LoadWorkbookResponseProto


class LoadWorkbookResponse_test(unittest.TestCase):

    # def test_toEventData(self):
    #     o = LoadWorkbookResponse(
    #         isError = False,
    #         windowId = "123",
    #         workbook = WorkbookImp("abc")
    #     )
    #     edt = o.toEventData()
    #     self.assertEqual(P6Events.App.LoadWorkbook.event,edt.event)


    def test_toProto_1(self):
        wb = WorkbookImp("abc")
        o = LoadWorkbookResponse(
            isError = False,
            windowId = "123",
            workbook = wb
        )
        p = o.toProtoObj()
        expect = LoadWorkbookResponseProto(
            isError = o.isError,
            windowId="123",
            workbook = wb.toProtoObj()
        )
        self.assertEqual(expect,p)

    def test_toProto_2(self):
        er = ErrorReport(
            header=ErrorHeader("123","Abc")
        )
        o = LoadWorkbookResponse(
            isError = True,
            windowId = "123",
            errorReport = er
        )
        p = o.toProtoObj()
        expect = LoadWorkbookResponseProto(
            isError = o.isError,
            windowId = "123",
            errorReport = er.toProtoObj()
        )
        self.assertEqual(expect,p)




if __name__ == '__main__':
    unittest.main()
