from pyzbar import pyzbar
from io import BytesIO
import argparse
from PIL import Image
from tokenfinder import Tokenfinder


def fingerprint_qrcode(path):
    # no need to check for that path as the
    # master script doesn't execute if path specified is not found
    img = Image.open(path)
    try:
        qr_code = pyzbar.decode(img)[0]
        data = qr_code.data.decode("utf-8")
        token = Tokenfinder.find_tokens_in_string(data)
        if token:
            print("The QR code " + path + " is a honeytoken")
        else:
            print("Not a honeytoken")
    except:
        print("Can't decode non QR file")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", "-f", type=str, required=True)
    args = parser.parse_args()
    fingerprint_qrcode(args.file)


if __name__ == "__main__":
    main()