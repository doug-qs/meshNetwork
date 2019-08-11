# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nodeConfig.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='nodeConfig.proto',
  package='nodeConfig',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x10nodeConfig.proto\x12\nnodeConfig\"\x8f\x03\n\x11NodeConfiguration\x12\x0e\n\x06nodeId\x18\x01 \x01(\r\x12\x13\n\x0bmaxNumNodes\x18\x02 \x01(\r\x12\x10\n\x08platform\x18\x03 \x01(\t\x12\x19\n\x11nodeUpdateTimeout\x18\x04 \x01(\x02\x12\x1b\n\x13\x46\x43\x43ommWriteInterval\x18\x05 \x01(\x02\x12\x14\n\x0c\x46\x43\x43ommDevice\x18\x06 \x01(\t\x12\x12\n\nFCBaudrate\x18\x07 \x01(\x04\x12\x13\n\x0b\x63mdInterval\x18\x08 \x01(\x02\x12\x13\n\x0blogInterval\x18\t \x01(\x02\x12\x10\n\x08\x63ommType\x18\n \x01(\t\x12\x17\n\x0fnumMeshNetworks\x18\x0b \x01(\r\x12\x13\n\x0bmeshDevices\x18\x0c \x03(\t\x12\x0e\n\x06radios\x18\r \x03(\t\x12\x12\n\nmsgParsers\x18\x0e \x03(\t\x12\x14\n\x0cmeshBaudrate\x18\x0f \x01(\x04\x12\x13\n\x0bparseMsgMax\x18\x10 \x01(\r\x12\x14\n\x0crxBufferSize\x18\x11 \x01(\r\x12\x12\n\ngcsPresent\x18\x12 \x01(\x08\"W\n\x16InterfaceConfiguration\x12\x15\n\rnodeCommIntIP\x18\x01 \x01(\t\x12\x12\n\ncommRdPort\x18\x02 \x01(\r\x12\x12\n\ncommWrPort\x18\x03 \x01(\r\"\xb9\x05\n\x11TDMAConfiguration\x12\x10\n\x08sleepPin\x18\x01 \x01(\t\x12\x14\n\x0c\x65nableLength\x18\x02 \x01(\x02\x12\x17\n\x0fslotGuardLength\x18\x03 \x01(\x02\x12\x18\n\x10preTxGuardLength\x18\x04 \x01(\x02\x12\x19\n\x11postTxGuardLength\x18\x05 \x01(\x02\x12\x10\n\x08txLength\x18\x06 \x01(\x02\x12\x0f\n\x07rxDelay\x18\x07 \x01(\x02\x12\x16\n\x0einitTimeToWait\x18\x08 \x01(\x02\x12\x13\n\x0bmaxNumSlots\x18\t \x01(\r\x12\x17\n\x0f\x64\x65siredDataRate\x18\n \x01(\x02\x12\x15\n\rinitSyncBound\x18\x0b \x01(\r\x12\x18\n\x10operateSyncBound\x18\x0c \x01(\r\x12\x15\n\roffsetTimeout\x18\r \x01(\x02\x12\x18\n\x10offsetTxInterval\x18\x0e \x01(\x02\x12\x18\n\x10statusTxInterval\x18\x0f \x01(\x02\x12\x17\n\x0flinksTxInterval\x18\x10 \x01(\x02\x12\x16\n\x0emaxTxBlockSize\x18\x11 \x01(\r\x12\x13\n\x0blinkTimeout\x18\x12 \x01(\x02\x12\x1d\n\x15\x62lockTxRequestTimeout\x18\x13 \x01(\r\x12\x17\n\x0fminBlockTxDelay\x18\x14 \x01(\r\x12\x0c\n\x04\x66pga\x18\x15 \x01(\x08\x12\x17\n\x0f\x66pgaFailsafePin\x18\x16 \x01(\t\x12\x14\n\x0c\x66pgaFifoSize\x18\x17 \x01(\r\x12\x11\n\tenablePin\x18\x18 \x01(\t\x12\x11\n\tstatusPin\x18\x19 \x01(\t\x12\x13\n\x0brecvAllMsgs\x18\x1a \x01(\x08\x12\x14\n\x0crestartDelay\x18\x1b \x01(\r\x12\x13\n\x0bpollTimeout\x18\x1c \x01(\r\x12\x13\n\x0b\x61\x64minEnable\x18\x1d \x01(\x08\x12\x13\n\x0b\x61\x64minLength\x18\x1e \x01(\r\"\xa3\x01\n\x10NodeConfig_proto\x12+\n\x04node\x18\x01 \x01(\x0b\x32\x1d.nodeConfig.NodeConfiguration\x12\x35\n\tinterface\x18\x02 \x01(\x0b\x32\".nodeConfig.InterfaceConfiguration\x12+\n\x04tdma\x18\x03 \x01(\x0b\x32\x1d.nodeConfig.TDMAConfigurationb\x06proto3')
)




_NODECONFIGURATION = _descriptor.Descriptor(
  name='NodeConfiguration',
  full_name='nodeConfig.NodeConfiguration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nodeId', full_name='nodeConfig.NodeConfiguration.nodeId', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maxNumNodes', full_name='nodeConfig.NodeConfiguration.maxNumNodes', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='platform', full_name='nodeConfig.NodeConfiguration.platform', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nodeUpdateTimeout', full_name='nodeConfig.NodeConfiguration.nodeUpdateTimeout', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='FCCommWriteInterval', full_name='nodeConfig.NodeConfiguration.FCCommWriteInterval', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='FCCommDevice', full_name='nodeConfig.NodeConfiguration.FCCommDevice', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='FCBaudrate', full_name='nodeConfig.NodeConfiguration.FCBaudrate', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cmdInterval', full_name='nodeConfig.NodeConfiguration.cmdInterval', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='logInterval', full_name='nodeConfig.NodeConfiguration.logInterval', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='commType', full_name='nodeConfig.NodeConfiguration.commType', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='numMeshNetworks', full_name='nodeConfig.NodeConfiguration.numMeshNetworks', index=10,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='meshDevices', full_name='nodeConfig.NodeConfiguration.meshDevices', index=11,
      number=12, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='radios', full_name='nodeConfig.NodeConfiguration.radios', index=12,
      number=13, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msgParsers', full_name='nodeConfig.NodeConfiguration.msgParsers', index=13,
      number=14, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='meshBaudrate', full_name='nodeConfig.NodeConfiguration.meshBaudrate', index=14,
      number=15, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parseMsgMax', full_name='nodeConfig.NodeConfiguration.parseMsgMax', index=15,
      number=16, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rxBufferSize', full_name='nodeConfig.NodeConfiguration.rxBufferSize', index=16,
      number=17, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gcsPresent', full_name='nodeConfig.NodeConfiguration.gcsPresent', index=17,
      number=18, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=432,
)


_INTERFACECONFIGURATION = _descriptor.Descriptor(
  name='InterfaceConfiguration',
  full_name='nodeConfig.InterfaceConfiguration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nodeCommIntIP', full_name='nodeConfig.InterfaceConfiguration.nodeCommIntIP', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='commRdPort', full_name='nodeConfig.InterfaceConfiguration.commRdPort', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='commWrPort', full_name='nodeConfig.InterfaceConfiguration.commWrPort', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=434,
  serialized_end=521,
)


_TDMACONFIGURATION = _descriptor.Descriptor(
  name='TDMAConfiguration',
  full_name='nodeConfig.TDMAConfiguration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sleepPin', full_name='nodeConfig.TDMAConfiguration.sleepPin', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enableLength', full_name='nodeConfig.TDMAConfiguration.enableLength', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='slotGuardLength', full_name='nodeConfig.TDMAConfiguration.slotGuardLength', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='preTxGuardLength', full_name='nodeConfig.TDMAConfiguration.preTxGuardLength', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='postTxGuardLength', full_name='nodeConfig.TDMAConfiguration.postTxGuardLength', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='txLength', full_name='nodeConfig.TDMAConfiguration.txLength', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rxDelay', full_name='nodeConfig.TDMAConfiguration.rxDelay', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='initTimeToWait', full_name='nodeConfig.TDMAConfiguration.initTimeToWait', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maxNumSlots', full_name='nodeConfig.TDMAConfiguration.maxNumSlots', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='desiredDataRate', full_name='nodeConfig.TDMAConfiguration.desiredDataRate', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='initSyncBound', full_name='nodeConfig.TDMAConfiguration.initSyncBound', index=10,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operateSyncBound', full_name='nodeConfig.TDMAConfiguration.operateSyncBound', index=11,
      number=12, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offsetTimeout', full_name='nodeConfig.TDMAConfiguration.offsetTimeout', index=12,
      number=13, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offsetTxInterval', full_name='nodeConfig.TDMAConfiguration.offsetTxInterval', index=13,
      number=14, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='statusTxInterval', full_name='nodeConfig.TDMAConfiguration.statusTxInterval', index=14,
      number=15, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='linksTxInterval', full_name='nodeConfig.TDMAConfiguration.linksTxInterval', index=15,
      number=16, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maxTxBlockSize', full_name='nodeConfig.TDMAConfiguration.maxTxBlockSize', index=16,
      number=17, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='linkTimeout', full_name='nodeConfig.TDMAConfiguration.linkTimeout', index=17,
      number=18, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='blockTxRequestTimeout', full_name='nodeConfig.TDMAConfiguration.blockTxRequestTimeout', index=18,
      number=19, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minBlockTxDelay', full_name='nodeConfig.TDMAConfiguration.minBlockTxDelay', index=19,
      number=20, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fpga', full_name='nodeConfig.TDMAConfiguration.fpga', index=20,
      number=21, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fpgaFailsafePin', full_name='nodeConfig.TDMAConfiguration.fpgaFailsafePin', index=21,
      number=22, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fpgaFifoSize', full_name='nodeConfig.TDMAConfiguration.fpgaFifoSize', index=22,
      number=23, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enablePin', full_name='nodeConfig.TDMAConfiguration.enablePin', index=23,
      number=24, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='statusPin', full_name='nodeConfig.TDMAConfiguration.statusPin', index=24,
      number=25, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='recvAllMsgs', full_name='nodeConfig.TDMAConfiguration.recvAllMsgs', index=25,
      number=26, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='restartDelay', full_name='nodeConfig.TDMAConfiguration.restartDelay', index=26,
      number=27, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pollTimeout', full_name='nodeConfig.TDMAConfiguration.pollTimeout', index=27,
      number=28, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='adminEnable', full_name='nodeConfig.TDMAConfiguration.adminEnable', index=28,
      number=29, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='adminLength', full_name='nodeConfig.TDMAConfiguration.adminLength', index=29,
      number=30, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=524,
  serialized_end=1221,
)


_NODECONFIG_PROTO = _descriptor.Descriptor(
  name='NodeConfig_proto',
  full_name='nodeConfig.NodeConfig_proto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node', full_name='nodeConfig.NodeConfig_proto.node', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='interface', full_name='nodeConfig.NodeConfig_proto.interface', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tdma', full_name='nodeConfig.NodeConfig_proto.tdma', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1224,
  serialized_end=1387,
)

_NODECONFIG_PROTO.fields_by_name['node'].message_type = _NODECONFIGURATION
_NODECONFIG_PROTO.fields_by_name['interface'].message_type = _INTERFACECONFIGURATION
_NODECONFIG_PROTO.fields_by_name['tdma'].message_type = _TDMACONFIGURATION
DESCRIPTOR.message_types_by_name['NodeConfiguration'] = _NODECONFIGURATION
DESCRIPTOR.message_types_by_name['InterfaceConfiguration'] = _INTERFACECONFIGURATION
DESCRIPTOR.message_types_by_name['TDMAConfiguration'] = _TDMACONFIGURATION
DESCRIPTOR.message_types_by_name['NodeConfig_proto'] = _NODECONFIG_PROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NodeConfiguration = _reflection.GeneratedProtocolMessageType('NodeConfiguration', (_message.Message,), {
  'DESCRIPTOR' : _NODECONFIGURATION,
  '__module__' : 'nodeConfig_pb2'
  # @@protoc_insertion_point(class_scope:nodeConfig.NodeConfiguration)
  })
_sym_db.RegisterMessage(NodeConfiguration)

InterfaceConfiguration = _reflection.GeneratedProtocolMessageType('InterfaceConfiguration', (_message.Message,), {
  'DESCRIPTOR' : _INTERFACECONFIGURATION,
  '__module__' : 'nodeConfig_pb2'
  # @@protoc_insertion_point(class_scope:nodeConfig.InterfaceConfiguration)
  })
_sym_db.RegisterMessage(InterfaceConfiguration)

TDMAConfiguration = _reflection.GeneratedProtocolMessageType('TDMAConfiguration', (_message.Message,), {
  'DESCRIPTOR' : _TDMACONFIGURATION,
  '__module__' : 'nodeConfig_pb2'
  # @@protoc_insertion_point(class_scope:nodeConfig.TDMAConfiguration)
  })
_sym_db.RegisterMessage(TDMAConfiguration)

NodeConfig_proto = _reflection.GeneratedProtocolMessageType('NodeConfig_proto', (_message.Message,), {
  'DESCRIPTOR' : _NODECONFIG_PROTO,
  '__module__' : 'nodeConfig_pb2'
  # @@protoc_insertion_point(class_scope:nodeConfig.NodeConfig_proto)
  })
_sym_db.RegisterMessage(NodeConfig_proto)


# @@protoc_insertion_point(module_scope)
