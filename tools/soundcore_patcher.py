import sys
import os

def patch_firmware(boot_path, fw_path, out_path):
    if not os.path.exists(boot_path):
        print(f"ota_boot not found at {boot_path}")
        sys.exit(1)
    if not os.path.exists(fw_path):
        print(f"firmware not found at {fw_path}")
        sys.exit(1)

    with open(boot_path, "rb") as f:
        bootloader = f.read()

    with open(fw_path, "rb") as f:
        firmware = f.read()

    if len(firmware) < 8:
        print("firmware binary is too small to patch!")
        sys.exit(1)

    fw_trimmed = firmware[4:-4]
    final_binary = bootloader + fw_trimmed


    with open(out_path, "wb") as f:
        f.write(final_binary)

    print(f"patched and saved to: {out_path}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("usage: python soundcore_patcher.py <bootloader.bin> <firmware.bin> <output.bin>")
        sys.exit(1)
    patch_firmware(sys.argv[1], sys.argv[2], sys.argv[3])