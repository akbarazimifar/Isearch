import argparse
from output import *
from lib.banner import b2
from lib.session_loader import checker


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
    parser.add_argument(
        "-t", "--tagged",
        nargs="?",
        type=str,
        default=None,
        help="displays all profiles that have been tagged by the target"
    )
    parser.add_argument(
        "-f", "--follows",
        nargs="?",
        type=str,
        default=None,
        help="shows the number of followers and following"
    )
    parser.add_argument(
        "-c", "--checker",
        action='store_true',
        help="checks if you have correctly submitted your session ID"
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

    elif args.tagged:
            username = args.tagged
            await tagged(username)
            exit()

    elif args.follows:
            username = args.follows
            await follows(username)
            exit()

    elif args.checker:
            await checker()
            exit()

    else:
        print(b2)
        exit()
