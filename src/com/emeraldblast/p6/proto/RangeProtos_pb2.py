# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/emeraldblast/p6/proto/RangeProtos.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from com.emeraldblast.p6.proto import CommonProtos_pb2 as com_dot_emeraldblast_dot_p6_dot_proto_dot_CommonProtos__pb2
from com.emeraldblast.p6.proto import DocProtos_pb2 as com_dot_emeraldblast_dot_p6_dot_proto_dot_DocProtos__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+com/emeraldblast/p6/proto/RangeProtos.proto\x12\x19\x63om.emeraldblast.p6.proto\x1a,com/emeraldblast/p6/proto/CommonProtos.proto\x1a)com/emeraldblast/p6/proto/DocProtos.proto\"|\n\x1cRangeToClipboardRequestProto\x12\x38\n\x07rangeId\x18\x01 \x01(\x0b\x32\'.com.emeraldblast.p6.proto.RangeIdProto\x12\x15\n\x08windowId\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x0b\n\t_windowId\"\xc5\x01\n\x1dRangeToClipboardResponseProto\x12\x46\n\x0e\x65rrorIndicator\x18\x01 \x01(\x0b\x32..com.emeraldblast.p6.proto.ErrorIndicatorProto\x12\x38\n\x07rangeId\x18\x02 \x01(\x0b\x32\'.com.emeraldblast.p6.proto.RangeIdProto\x12\x15\n\x08windowId\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\x0b\n\t_windowId\"y\n\x0eRangeCopyProto\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.com.emeraldblast.p6.proto.RangeIdProto\x12\x32\n\x04\x63\x65ll\x18\x02 \x03(\x0b\x32$.com.emeraldblast.p6.proto.CellProtob\x06proto3')



_RANGETOCLIPBOARDREQUESTPROTO = DESCRIPTOR.message_types_by_name['RangeToClipboardRequestProto']
_RANGETOCLIPBOARDRESPONSEPROTO = DESCRIPTOR.message_types_by_name['RangeToClipboardResponseProto']
_RANGECOPYPROTO = DESCRIPTOR.message_types_by_name['RangeCopyProto']
RangeToClipboardRequestProto = _reflection.GeneratedProtocolMessageType('RangeToClipboardRequestProto', (_message.Message,), {
  'DESCRIPTOR' : _RANGETOCLIPBOARDREQUESTPROTO,
  '__module__' : 'com.emeraldblast.p6.proto.RangeProtos_pb2'
  # @@protoc_insertion_point(class_scope:com.emeraldblast.p6.proto.RangeToClipboardRequestProto)
  })
_sym_db.RegisterMessage(RangeToClipboardRequestProto)

RangeToClipboardResponseProto = _reflection.GeneratedProtocolMessageType('RangeToClipboardResponseProto', (_message.Message,), {
  'DESCRIPTOR' : _RANGETOCLIPBOARDRESPONSEPROTO,
  '__module__' : 'com.emeraldblast.p6.proto.RangeProtos_pb2'
  # @@protoc_insertion_point(class_scope:com.emeraldblast.p6.proto.RangeToClipboardResponseProto)
  })
_sym_db.RegisterMessage(RangeToClipboardResponseProto)

RangeCopyProto = _reflection.GeneratedProtocolMessageType('RangeCopyProto', (_message.Message,), {
  'DESCRIPTOR' : _RANGECOPYPROTO,
  '__module__' : 'com.emeraldblast.p6.proto.RangeProtos_pb2'
  # @@protoc_insertion_point(class_scope:com.emeraldblast.p6.proto.RangeCopyProto)
  })
_sym_db.RegisterMessage(RangeCopyProto)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RANGETOCLIPBOARDREQUESTPROTO._serialized_start=163
  _RANGETOCLIPBOARDREQUESTPROTO._serialized_end=287
  _RANGETOCLIPBOARDRESPONSEPROTO._serialized_start=290
  _RANGETOCLIPBOARDRESPONSEPROTO._serialized_end=487
  _RANGECOPYPROTO._serialized_start=489
  _RANGECOPYPROTO._serialized_end=610
# @@protoc_insertion_point(module_scope)
