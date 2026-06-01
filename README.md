# DOOMcore

this is firmware for the soundcore life q35 headphones that contains a port of [doomgeneric](https://github.com/ozkl/doomgeneric). 

based on arin-s [DOOMBuds](https://github.com/arin-s/DOOMBuds) project. a lots of thanks to him and check his work too!
also thanks to the [openpinebuds](https://github.com/pine64/OpenPineBuds/graphs/contributors) team for the SDK!!!

## build (text from DOOMBuds, but a bit corrected for soundcores)

to build & flash your soundcores you will need a system with Docker setup at the minimum.  
if you are using windows:
- enable WSL2 and install a distro
- install Docker Desktop and enable WSL integration in its settings
- use [this](https://gitlab.com/alelec/wsl-usb-gui) program to connect your headphones to your distro (tick bound and then attach it)

and first of all, please read my [flashing guide](https://github.com/nnonickreal/openqore/blob/main/docs/FLASHING.md) and make a [backup](https://github.com/nnonickreal/openqore/blob/main/docs/READING.md)!

after reading (backuping) the flash, put the flash dump image in the "tools" folder and rename it to "firmware.bin"

```bash
./start_dev.sh # this will cause docker to start your working environment; this should take roughly 1-3 minutes depending on your network speed

# once you are inside the container, your console will look akin to "root@ec5410d0a265:/usr/src#"

./build.sh # this will run make and build the firmware. if you have weird build errors try running clean.sh or rm -rf'ing the out folder first

# assuming that your serial port is 0, run the following to program the headphones.
bestool write-image out/oqdoom/oqdoom.bin --port /dev/ttyACM0
```
## using
once you've flashed the headphones, you can use arin's [DOOMBUDS-JS](https://github.com/arin-s/DOOMBUDS-JS)'s to play DOOM on the headphones.

will say it again, a lots of thanks to arin's [DOOMBuds](https://github.com/arin-s/DOOMBuds) and [openpinebuds](https://github.com/pine64/OpenPineBuds/graphs/contributors) team! 

DOOMcore is based on these projects. say hi to pine64 on [discord](https://discord.com/invite/pine64) :)
