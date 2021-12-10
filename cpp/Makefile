COMM_CONTROL_SRC:=commControl

COMM_SRC:=comm/utilities.cpp \
     comm/radio.cpp \
     comm/udpRadio.cpp \
     comm/commands.cpp \
     comm/msgParser.cpp \
     comm/xbeeRadio.cpp \
     comm/li1Radio.cpp \
     comm/fpgaRadio.cpp \
     comm/crc_8.cpp \
     comm/crc_16.cpp \
     comm/checksum.cpp \
     comm/SLIPMsg.cpp \
     comm/SLIPMsgParser.cpp \
     comm/serialComm.cpp \
     comm/formationClock.cpp \
     comm/cmdHeader.cpp \
     comm/command.cpp \
     comm/nodeMsgProcessor.cpp \
     comm/tdmaMsgProcessor.cpp \
     comm/commandUtils.cpp \
     comm/nodeCmds.cpp \
     comm/tdmaCmds.cpp \
     comm/tdmaComm.cpp \
     comm/tdmaComm_fpga.cpp \
     comm/commControl.cpp \
     node/nodeState.cpp \
     node/nodeConfig.cpp \
     node/nodeParams.cpp \
     node/nodeInterface.cpp \
     node/nodeInterface.pb.cpp \
     node/nodeController.cpp \
     node/nodeExecutive.cpp \
     node/nodeControl.cpp
     #node/pixhawk/pixhawkCmds.cpp

NODE_SRC:=node/nodeCmds.cpp \
     node/nodeController.cpp \
     node/nodeExecutive.cpp \
     node/nodeControl.cpp

TEST_DRIVER_SRC:=runTest.cpp

TEST_SRC:=tests/radio_UT.cpp \
          tests/nodeConfig_UT.cpp \
          tests/cmdHeader_UT.cpp \
          tests/command_UT.cpp \
          tests/nodeCmds_UT.cpp \
          tests/tdmaCmds_UT.cpp \
          tests/commandUtils_UT.cpp \
          tests/msgParser_UT.cpp \
          tests/SLIPMsg_UT.cpp \
          tests/SLIPMsgParser_UT.cpp \
          tests/nodeMsgProcessor_UT.cpp \
          tests/tdmaMsgProcessor_UT.cpp \
          tests/serialComm_UT.cpp \
          tests/tdmaComm_UT.cpp
          #tests/xbeeRadio_UT.cpp \
          #tests/li1Radio_UT.cpp \
          #tests/commBuffer_UT.cpp \
          #tests/commProcessor_UT.cpp \
          #comm/testMsgProcessor.cpp \
          #tests/crc_UT.cpp \
          #tests/checksum_UT.cpp \
          #tests/serialComm_UT.cpp \
          #tests/formationClock_UT.cpp \
          #tests/nodeConfig_UT.cpp \
          #tests/nodeParams_UT.cpp \

INTERFACE_PROTO_SRC:=../interface/nodeInterface.proto \
                     ../interface/nodeConfig.proto

NODE_PBS:=node/nodeInterface.pb.h \
          node/nodeInterface.pb.cpp

SP:=./

LIBDIR:=./lib
JSONDIR:=$(LIBDIR)/rapidjson
GPIODIR:=$(LIBDIR)/GPIOWrapper
GTESTINCDIR:=/usr/local/include
GTESTLIBDIR:=/usr/local/lib

TGT:=gpiowrapper
TGTTYPE:=static_lib
SRC:=$(DEFAULT_SRC) $(BBB_SRC) $(RASPI_SRC)
TEST_SRC:=
CLEANFILES:=
SUBDIRS:=
CFLAGS:=
CPPFLAGS:=
LDFLAGS:=

TGT:=commControl
TGTTYPE:=application
SRC:=$(COMM_CONTROL_SRC) $(COMM_SRC) $(NODE_SRC) 
CLEANFILES:=$(DEFAULT_SRC) $(BBB_OBJS) $(RASPI_OBJS)

SERIAL_CFLAGS:=
ifdef serial_DIR
SERIAL_CFLAGS+=-I$(serial_DIR)/include
endif
CFLAGS:=$(SERIAL_CFLAGS) -I. -I$(LIBDIR) -I$(GPIODIR) -I$(JSONDIR) -I$(GTESTINCDIR) #-DXPRINT_LOCATION #-DPRINT_DEBUG

CPPFLAGS:=

LDFLAGS:=
LOCAL_LIB_LD_FLAGS=-L$(JSONDIR) -lrapidjson -L$(GPIODIR) -lgpiowrapper -L$(GTESTLIBDIR) -lgtest
LOCAL_LIBS=$(JSONDIR)/librapidjson.a $(GPIODIR)/libgpiowrapper.a
SERIAL_LD_FLAGS:=
ifdef serial_DIR
SERIAL_LD_FLAGS:=-L$(serial_DIR)/lib
endif
SERIAL_LD_FLAGS+=-lserial
LDFLAGS+=$(LOCAL_LIB_LD_FLAGS) -lprotobuf $(SERIAL_LD_FLAGS) -lm -lcrypto  -lstdc++

SUBDIRS:=$(JSONDIR) $(GPIODIR)


CPPFLAGS:=-std=c++11



pi: LDFLAGS+=-lwiringPi $(TGT)

commControl: SRC:=$(COMM_CONTROL_SRC) SRC+=$(COMM_OBJS) $(LOCAL_LIBS)
	$(CPP) -o $@ $^ $(LDFLAGS)

deps: $(LOCAL_LIBS) $(INTERFACE_PBS)

clean_deps:
	rm -f $(LOCAL_LIBS) $(INTERFACE_PBS)

.PHONY comm
comm: $(COMM_OBJS) $(TGT)

.PHONY node
node: $(SUBDIRS) $(AR_OBJS) $(TGT)

.PHONY node_pb
node_pb: $(NODE_PBS)

.PHONY pb
pb: $(INTERFACE_PBS)

.PHONY clean_pb
clean_pb:
	rm -f $(INTERFACE_PBS)
	rm -f node/*.pb.*


include $(SP)rules.mk
