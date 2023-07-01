import sys, asyncio

def version():
    version = sys.version_info

    if (version < (3, 10)):
        print("[-] Isearch only works with Python 3.10+.")
        print("[+] Go install the most recent version of python -> https://www.python.org/downloads/")
        exit()

    from lib.cli import parser

    asyncio.run(parser())