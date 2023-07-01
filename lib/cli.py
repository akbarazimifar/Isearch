import argparse
from output import *
from lib.banner import b2


async def parser():
    """
    Menu format : cli 

    - this function serves to used commands with argparse
    - (asynchrone function)
    """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "name",
        nargs="?",
        type=str,
        default=None,
        help="search public informations on target"
    )
    parser.add_argument(
        "-d", "--download",
        nargs="?",
        type=str,
        default=None,
        help="download the profile picture of the target"
    )

    args = parser.parse_args()

    if args.name:
            username = args.name
            await output(username)
            exit()

    elif args.download:
            username = args.download
            await downloader(username)
            exit()

    else:
        print(b2)
        exit()