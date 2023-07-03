import json
from lib.objects import TempPrint
from lib.colors import GREEN, WHITE, RED
from lib.banner import b1


async def launch():
    TempPrint("[+] 🤔 Session ID checking...").TPrint()
    with open("data.json", "r") as file:
        data = json.load(file)
        session_id = data['sessionID']

        if session_id == "YOUR_SESSION_ID":
            print("[-] Please enter your session ID in the data.json file.")
            exit()

        elif session_id == "":
            print("[-] Please enter your session ID in the data.json file.")
            exit()

        else:
            TempPrint("[+] 👍 Session ID found.").TPrint()
            print()
            return session_id


async def checker():
    print(b1)

    TempPrint("[+] 🤔 Session ID checking...").TPrint()
    with open("data.json", "r") as file:
        read = json.load(file)

        sessionID = read['sessionID']

    if sessionID != "YOUR_SESSION_ID":
        print(GREEN + "[+] Session ID found! You can use the whole tool." + WHITE)

    elif sessionID != "":
        print(GREEN + "[+] Session ID found! You can use the whole tool." + WHITE)

    else:
        print(RED + "[-] Session ID not found, drop it in the data.json file." + WHITE)
