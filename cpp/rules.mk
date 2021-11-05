CC:=gcc
CPP:=g++
CXX:=g++
LD:=g++
AR:=ar

#CC:=/home/aerom/test/gcc-linaro-6.3.1-2017.05-x86_64_arm-linux-gnueabihf/bin/arm-linux-gnueabihf-gcc
#CPP:=/home/aerom/test/gcc-linaro-6.3.1-2017.05-x86_64_arm-linux-gnueabihf/bin/arm-linux-gnueabihf-g++
#CXX:=/home/aerom/test/gcc-linaro-6.3.1-2017.05-x86_64_arm-linux-gnueabihf/bin/arm-linux-gnueabihf-g++
#LD:=/home/aerom/test/gcc-linaro-6.3.1-2017.05-x86_64_arm-linux-gnueabihf/bin/arm-linux-gnueabihf-g++
#AR:=/home/aerom/test/gcc-linaro-6.3.1-2017.05-x86_64_arm-linux-gnueabihf/bin/arm-linux-gnueabihf-ar
#CPLUS_INCLUDE_PATH=-I/usr/local/include/ -I/usr/include/

BASEDIR:=$(SP)
LDFLAGS:=
ifdef serial_DIR
CFLAGS+=-I$(serial_DIR)/include
LDFLAGS+=-L$(serial_DIR)/lib
endif
CFLAGS+=-O2
CPPFLAGS+=$(CFLAGS) -g -Wall

SYSTEM:=$(shell uname)
ARCH:=$(shell uname -m)
SYS_CYGWIN:=CYGWIN_NT-5.1
SYS_MINGW:=MINGW32_NT-5.1
SYS_LINUX:=Linux
SYS_DARWIN:=Darwin

## Object and fependency files
# Comm object and dependency files
COMM_OBJS:=$(patsubst %.cpp, %.o, $(COMM_SRC))
COMM_DEPS:=$(patsubst %.cpp, %.d, $(COMM_SRC))

# Node object and dependency files
NODE_OBJS:=$(patsubst %.cpp, %.o, $(NODE_SRC))
NODE_DEPS:=$(patsubst %.cpp, %.d, $(NODE_SRC))

# Test object and dependency files
TEST_OBJS:=$(patsubst %.cpp, %.o, $(TEST_SRC))
TEST_DEPS+=$(patsubst %.cpp, %.d, $(TEST_SRC))

# Node pb.h and pb.cpp files
INTERFACE_PBS:=$(patsubst %.proto, %.pb.h, $(INTERFACE_PROTO_SRC))
INTERFACE_PBS+=$(patsubst %.proto, %.pb.cc, $(INTERFACE_PROTO_SRC))

## Targets
.PHONY: all pi comm node clean $(SUBDIRS)

all: $(SUBDIRS) comm $(TGT)

comm: $(COMM_OBJS) commControl

node: $(SUBDIRS) $(COMM_OBJS) $(NODE_OBJS) $(TGT)

node_pb: $(NODE_PBS)

pb: $(INTERFACE_PBS)

clean_pb:
	rm -f $(INTERFACE_PBS)
	rm -f node/*.pb.*

$(SUBDIRS):
	$(MAKE) -C $@ $(MAKECMDGOALS)

%.a: $(COMM_OBJS) $(NODE_OBJS)
	$(AR) rcs $@ $(COMM_OBJS) $(NODE_OBJS)

%.d:%.cpp
	$(CPP) -MM $(CPPFLAGS) -MT $*.o $< -o $@

%.pb.h %.pb.cc:%.proto
	protoc -I=$(@D) --cpp_out=$(@D) $<

node/%.pb.h:../interface/%.pb.h
	cp $< $@

node/%.pb.cpp:../interface/%.pb.cc
	cp $< $@

ifeq ($(TGTTYPE), static_lib)
TGT:=lib$(TGT).a
LDFLAGS+=-lrt -ldl -lpthread
endif

ifeq ($(TGTTYPE), application)
ifeq ($(SYSTEM),$(SYS_CYGWIN))
TGT:=$(TGT).exe
else
ifeq ($(SYSTEM),$(SYS_MINGW))
TGT:=$(TGT).exe
else
TGT:=$(TGT)
LDFLAGS+=-ldl -lpthread
endif
endif
endif

clean: $(SUBDIRS)
	rm -f *.o $(COMM_OBJS) $(NODE_OBJS) $(COMM_DEPS) $(NODE_DEPS) $(TEST_OBJS) $(TEST_DEPS) $(TGT) $(TEST_DRIVER) \
          $(EXTRA_CLEAN) gtest* *.stackdump *~

ifeq ("",$(filter $(MAKECMDGOALS),clean clean_pb, pb, node_pb))
-include $(COMM_DEPS)
-include $(TEST_DEPS)
endif
