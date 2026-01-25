# DOOMBUDS

This is firmware for the Pinebuds Pro earbuds that contains a port of [doomgeneric](https://github.com/ozkl/doomgeneric)  
Huge thanks to the [OpenPineBuds](https://github.com/pine64/OpenPineBuds/graphs/contributors) team for maintaining the firmware, go say hi to them on [discord](https://discord.com/invite/pine64)!

## Build

To build & flash your PineBuds you will need a system with Docker setup at the minimum.  
If you are using Windows:
- Enable WSL2 and install a distro (I used Ubuntu 20.04)
- Install Docker Desktop and enable WSL integration in its settings
- Use [this](https://gitlab.com/alelec/wsl-usb-gui) program to connect your buds to your distro (tick bound and then attach it)


```bash
./start_dev.sh # This will cause docker to start your working environment; this should take roughly 1-3 minutes depending on your network speed

# Once you are inside the container, your console will look akin to "root@ec5410d0a265:/usr/src#"

./build.sh # This will run make and build the fiurmware. If you have weird build errors try running clean.sh or rm -rf'ing the out folder first

# You may need to take the buds out of the case, wait three seconds, then place them back.
# This wakes them up and the programmer needs to catch this reboot.
# You'll know it worked when you see the lights on the case flash.

# You can run the following to program each bud.
# Flashing both of them is not necessary.
# In my experience, ttyACM1 is the right earbud, while ttyACM0 is the left one, YMMV.
bestool write-image out/open_source/open_source.bin --port /dev/ttyACM0
bestool write-image out/open_source/open_source.bin --port /dev/ttyACM1
```
Once you've flashed the earbuds, you can use [DOOMBUDS-JS](https://github.com/arin-s/DOOMBUDS-JS)'s standalone package to play DOOM on the earbud through your browser.

https://github.com/user-attachments/assets/bb55a771-02e3-4869-a142-99a35d51b17a
