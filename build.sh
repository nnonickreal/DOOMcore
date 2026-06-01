#!/usr/bin/env sh

if make -j "$(nproc)" T=oqdoom DEBUG=1 NOAPP=1 MCU_HIGH_PERFORMANCE_MODE=1 NO_SLEEP=1 CALIB_SLOW_TIMER=1 FLASH_LOW_SPEED=1 PSRAM_LOW_SPEED=0 DOOMBUDS=1 V=1 LARGE_RAM=1 ANC_APP=0 SOUNDCORE_PATCH=1 >log.txt 2>&1; then
	echo "build success"
else
	echo "build failed and call log.txt"
	grep "error:" log.txt
fi
