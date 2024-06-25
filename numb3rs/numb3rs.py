import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    #reg expression pattern
    pattern = re.compile(r'^(?!0\d)\d{1,3}\.(?!0\d)\d{1,3}\.(?!0\d)\d{1,3}\.(?!0\d)\d{1,3}$')
    matches = pattern.match(ip)
    if matches:
        #chech if its octet is between 0-255
        for octet in ip.split("."):
            if not 0<= int(octet) <=255:
                return False
        return True
    return False


if __name__ == "__main__":
    main()
