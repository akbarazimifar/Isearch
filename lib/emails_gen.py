import random, string
from .objects import *
from .colors import *
from .domains import email_domains

async def gen(username: str, email: str):

    def variations():


        upp = username.upper() + "@" + random.choice(email_domains)
        low = username.lower() + "@" + random.choice(email_domains)
        num = (
            username.replace("1", "i")
            .replace("3", "e")
            .replace("4", "a")
            .replace("8", "b")
            .replace("0", "o") + "@" + random.choice(email_domains)
        )
        lett = (
            username.replace("i", "1")
            .replace("e", "3")
            .replace("a", "4")
            .replace("b", "8")
            .replace("o", "0") + "@" + random.choice(email_domains)
        )
        a = (
            username.replace(".", "")
            .replace("-", "")
            .replace("_", "") + "@" + random.choice(email_domains)
        )
        no_num = (
            username.replace("1", "")
            .replace("2", "")
            .replace("3", "")
            .replace("4", "")
            .replace("5", "")
            .replace("6", "")
            .replace("7", "")
            .replace("8", "")
            .replace("9", "")
            .replace("0", "") + "@" + random.choice(email_domains)
        )

        ett = (
            username.upper().replace("I", "1")
            .replace("E", "3")
            .replace("A", "4")
            .replace("B", "8")
            .replace("O", "0") + "@" + random.choice(email_domains)
        )

        dedede = username + "$$" + "@" + random.choice(email_domains)

        r = username + "".join(random.choices(string.digits + string.digits + string.digits + string.digits + string.digits + string.digits + string.digits)) + "@" + random.choice(email_domains)

        off = username + ".off" + "@" + random.choice(email_domains) 

        return upp, low, num, lett, a, no_num, ett, r, dedede, off

    var = variations()

    msg = TempPrint("[+] 🧠 Generation of variations of target email...", temp=3)
    msg.TPrint()

    list = []

    for v in var:

        if v in list:
            print(f"[+] {v} {BLACK}[Already shown]{WHITE}")
            continue
        else:
            list.append(v)

            if email != None or "":
                if v == email:
                    print(f"{GREEN}[+] 📭 Email found -> {v}")
                else:
                    print(f"[+] {v}")
            else:
                print(f"[+] {v}")