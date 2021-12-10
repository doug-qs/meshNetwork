# Importing file should define:
# * TGT             - basename of library or application
# * TGT_TYPE        - $(TGT) type
#                     supported types: static_lib, application
# * SRC             - all source files to build for $(TGT)
#                 	  supported types: .cpp, .c
# * TGT_DEPS        - additional prerequisites of the target, not produced from $(SRC)
# * TEST_DRIVER_SRC - the file containing the test driver
#                     supported types: .cpp
# * TEST_SRC        - the source files containing google tests
#                     supported types: .cpp
# * CLEANFILES      - files to remove during "clean", in addition to $(TGT) and the objects (.o) from $(SRC) and $(TEST_SRC)
# * SUBDIRS         - subdirectories in which to execute make for the current target(s)
# Importing file should define base state (even if it is empty) for:
# * CFLAGS
# * CPPFLAGS
# * LDFLAGS

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

# rules.mk is in the base directory
BASE_DIR := $(dir $(lastword $(MAKEFILE_LIST)))

CFLAGS+=-O2
CPPFLAGS+=$(CFLAGS) -g -Wall

SYSTEM:=$(shell uname)
ARCH:=$(shell uname -m)
SYS_CYGWIN:=CYGWIN_NT-5.1
SYS_MINGW:=MINGW32_NT-5.1
SYS_LINUX:=Linux
SYS_DARWIN:=Darwin

OBJS:=$(patsubst %.cpp, %.o, $(SRC))
OBJS:=$(OBJS:%.c=%.o)

DEPS:=$(patsubst %.cpp, %.d, $(SRC))
DEPS:=$(DEPS:%.c=%.d)

PBS:=$(patsubst %.proto, %.pb.h, $(PROTOS))
PBS+=$(patsubst %.proto, %.pb.cc, $(PROTOS))

TEST_DRIVER_OBJS:=$(patsubst %.cpp, %.o, $(TEST_DRIVER_SRC))
TEST_DRIVER_DEPS+=$(patsubst %.cpp, %.d, $(TEST_DRIVER_SRC))
TEST_OBJS:=$(patsubst %.cpp, %.o, $(TEST_SRC))
TEST_DEPS+=$(patsubst %.cpp, %.d, $(TEST_SRC))

ifeq ($(TGT_TYPE), static_lib)
# Target is a static library
TGT:=lib$(TGT).a
LDFLAGS+=-lrt -ldl -lpthread
# Build rule for static library $(TGT)
$(TGT): $(OBJS) $(TGT_DEPS)
	$(AR) rcs $@ $^
else
ifeq ($(TGT_TYPE), application)
ifeq ($(SYSTEM),$(SYS_CYGWIN))
# Target is a Windows application
TGT:=$(TGT).exe
else
ifeq ($(SYSTEM),$(SYS_MINGW))
# Target is a Windows application
TGT:=$(TGT).exe
else
# Target is a non-Windows application
TGT:=$(TGT)
LDFLAGS+=-ldl -lpthread
endif
endif
endif
# Build rule for executable $(TGT)
$(TGT): $(OBJS) $(TGT_DEPS)
	$(CPP) -o $@ $^ $(LDFLAGS)
endif
LDFLAGS+=-lstdc++

## Targets
.PHONY: all
all: $(SUBDIRS) $(TGT)

GTEST_DIR:=$(BASE_DIR)/lib/gtest
TEST_DRIVER:=run_test
$(TEST_DRIVER): CPPFLAGS+=-DASSERT_THROWS_EXCEPTION -I$(GTEST_DIR)/include \
                -L$(GTEST_DIR)/cmake -lgtest_main -lgtest
$(TEST_DRIVER): $(SUBDIRS) $(TEST_DRIVER_OBJS) $(TEST_OBJS) $(OBJS)
	$(CPP) -o $@ $(CPPFLAGS) $(TEST_DRIVER_OBJS) $(TEST_OBJS) $(OBJS) $(TEST_DEPS) $(LDFLAGS)
.PHONY: test
test: $(TEST_DRIVER)

SUBDIR_MAKECMDGOALS:=$(filter $(MAKECMDGOALS),clean all test)
.PHONY: $(SUBDIRS)
$(SUBDIRS):
	$(MAKE) -C $@ $(SUBDIR_MAKECMDGOALS)
	
.PHONY: subdirs
subdirs: $(SUBDIRS)

.PHONY: clean_subdirs
clean_subdirs:
	$(foreach d, $(SUBDIRS), $(MAKE) -C $d clean;)

.PHONY: pbs
pbs: $(PBS)

.PHONY: clean_pbs
clean_pbs:
	rm -f $(PBS)

.PHONY: deps	
deps: $(TGT_DEPS)

.PHONY: clean_deps
clean_deps:
	rm -f $(TGT_DEPS)

.PHONY: clean
clean: $(SUBDIRS)
	rm -f *.o $(OBJS) $(DEPS) $(TGT) \
	      $(TEST_DRIVER_OBJS) $(TEST_DRIVER_DEPS) $(TEST_OBJS) $(TEST_DEPS) $(TEST_DRIVER) \
          $(CLEANFILES) *.stackdump *~

%.o:%.d

%.d:%.cpp
	$(CPP) -MM $(CPPFLAGS) -MT $*.o $< -o $@

%.pb.h %.pb.cc:%.proto
	protoc -I=$(@D) --cpp_out=$(@D) $<

ifeq ("",$(filter $(MAKECMDGOALS),subdirs clean_subdirs pbs clean_pbs clean_deps clean))
-include $(COMM_DEPS)
-include $(TEST_DEPS)
endif
