import json
from lib.objects import TempPrint

async def launch():
    TempPrint("[+] 🤔 Session ID checking...").TPrint()
    with open("data.json", "r") as file:
        data = json.load(file)
        session_id = data['sessionID']

        if session_id == "":
            print("[-] Please enter your session ID in the data.json file.")
            exit()

        else:
            TempPrint("[+] 👍 Session ID found.").TPrint()
            print()
            return session_id
