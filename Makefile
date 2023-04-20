device=cpu
FELTOR_PATH=../feltor

#configure machine
include $(FELTOR_PATH)/config/default.mk
include $(FELTOR_PATH)/config/*.mk
include $(FELTOR_PATH)/config/devices/devices.mk

INCLUDE+=-I$(FELTOR_PATH)/inc/

all: geometry_diag normalize_params

geometry_diag: geometry_diag.cpp
	$(CC) $(OPT) $(CFLAGS) $< -o $@ $(INCLUDE) $(LIBS) $(JSONLIB) -g

normalize_params: normalize_params.cpp
	$(CC) $(OPT) $(CFLAGS) $< -o $@ $(INCLUDE) $(LIBS) $(JSONLIB) -g

.PHONY: clean

clean:
	rm -f geometry_diag normalize_params
