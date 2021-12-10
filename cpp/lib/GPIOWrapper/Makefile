DEFAULT_SRC:=GPIOWrapper.cpp

BBB_SRC:=GPIOWrapper_BBB.cpp \
         BeagleBoneBlack-GPIO/GPIO/manager.cpp \
         BeagleBoneBlack-GPIO/GPIO/const.cpp

RASPI_SRC:=GPIOWrapper_PI.cpp 

TGT:=gpiowrapper
TGT_TYPE:=static_lib
SRC:=$(DEFAULT_SRC) $(BBB_SRC) $(RASPI_SRC)
TGT_DEPS:=
TEST_DRIVER_SRC:=
TEST_SRC:=
CLEANFILES:=
SUBDIRS:=
CFLAGS:=-I.
CPPFLAGS:=
LDFLAGS:=

include ../../rules.mk

# all is defined in rules.mk
.PHONY: all
all: SRC:=$(DEFAULT_SRC)
all: $(TGT)

.PHONY: default
default: SRC:=$(DEFAULT_SRC)
default: $(TGT)

.PHONY: bbb
bbb: SRC:=$(BBB_SRC)
bbb: $(TGT)

.PHONY: pi
pi: SRC:=$(RASPI_SRC)
pi: $(TGT)
