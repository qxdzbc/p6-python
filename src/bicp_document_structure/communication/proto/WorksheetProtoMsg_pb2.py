# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WorksheetProtoMsg.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import Common_pb2 as Common__pb2
from . import DocProto_pb2 as DocProto__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17WorksheetProtoMsg.proto\x12\x19\x63om.emeraldblast.p6.proto\x1a\x0c\x43ommon.proto\x1a\x0e\x44ocProto.proto\"\x81\x01\n\x1bRenameWorksheetRequestProto\x12@\n\x0bworkbookKey\x18\x01 \x01(\x0b\x32+.com.emeraldblast.p6.proto.WorkbookKeyProto\x12\x0f\n\x07oldName\x18\x02 \x01(\t\x12\x0f\n\x07newName\x18\x03 \x01(\t\"\xe4\x01\n\x1cRenameWorksheetResponseProto\x12@\n\x0bworkbookKey\x18\x01 \x01(\x0b\x32+.com.emeraldblast.p6.proto.WorkbookKeyProto\x12\x0f\n\x07oldName\x18\x02 \x01(\t\x12\r\n\x05index\x18\x03 \x01(\x05\x12\x0f\n\x07newName\x18\x04 \x01(\t\x12\x0f\n\x07isError\x18\x05 \x01(\x08\x12@\n\x0b\x65rrorReport\x18\x06 \x01(\x0b\x32+.com.emeraldblast.p6.proto.ErrorReportProtob\x06proto3')



_RENAMEWORKSHEETREQUESTPROTO = DESCRIPTOR.message_types_by_name['RenameWorksheetRequestProto']
_RENAMEWORKSHEETRESPONSEPROTO = DESCRIPTOR.message_types_by_name['RenameWorksheetResponseProto']
RenameWorksheetRequestProto = _reflection.GeneratedProtocolMessageType('RenameWorksheetRequestProto', (_message.Message,), {
  'DESCRIPTOR' : _RENAMEWORKSHEETREQUESTPROTO,
  '__module__' : 'WorksheetProtoMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.emeraldblast.p6.proto.RenameWorksheetRequestProto)
  })
_sym_db.RegisterMessage(RenameWorksheetRequestProto)

RenameWorksheetResponseProto = _reflection.GeneratedProtocolMessageType('RenameWorksheetResponseProto', (_message.Message,), {
  'DESCRIPTOR' : _RENAMEWORKSHEETRESPONSEPROTO,
  '__module__' : 'WorksheetProtoMsg_pb2'
  # @@protoc_insertion_point(class_scope:com.emeraldblast.p6.proto.RenameWorksheetResponseProto)
  })
_sym_db.RegisterMessage(RenameWorksheetResponseProto)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RENAMEWORKSHEETREQUESTPROTO._serialized_start=85
  _RENAMEWORKSHEETREQUESTPROTO._serialized_end=214
  _RENAMEWORKSHEETRESPONSEPROTO._serialized_start=217
  _RENAMEWORKSHEETRESPONSEPROTO._serialized_end=445
# @@protoc_insertion_point(module_scope)
