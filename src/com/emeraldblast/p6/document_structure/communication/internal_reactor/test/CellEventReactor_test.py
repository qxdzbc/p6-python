import unittest

from com.emeraldblast.p6.document_structure.cell.DataCell import DataCell
from com.emeraldblast.p6.document_structure.cell.address.CellIndex import CellIndex
from com.emeraldblast.p6.document_structure.communication.internal_reactor.CellReactor import CellReactor
from com.emeraldblast.p6.document_structure.communication.internal_reactor.eventData.CellEventData import CellEventData


class CellEventReactorTest(unittest.TestCase):
    x=0
    def cb(self,cell:CellEventData):
        self.x+=1
    def test_callbackIsCalled(self):
        cell = DataCell(CellIndex(1,2),)
        cellReactor = CellReactor("123", self.cb)
        cellReactor.react(cell)
        self.assertEqual(1,self.x)