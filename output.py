#!/usr/bin/env python3
# Instagram Search by Norze


from lib.api import api_instagram
from lib.requests import *
from lib.banner import b1
from lib.colors import *
from lib.session_loader import launch
from lib.phone.phonelookup import *
from lib.emails_gen import gen
import json


async def output(username: str):
    print(b1)
    sessionsId = await launch()

    cookies = {'sessionid': sessionsId}
    headers = {'User-Agent': 'Instagram 64.0.0.14.96'}
    r = Requests(api_instagram(username), headers=headers, cookies=cookies)

    result = await r.sender()

    if result.status_code != 404:
        try:
            data = result.json()

            id = f"[+] ID => {data['logging_page_id'].strip('profilePage_')}"
            
            if data['graphql']['user']['username'] != "":
                name = f"[+] Username => {data['graphql']['user']['username']}"
            else:
                name = "[-] Name not found."
            if data['graphql']['user']['full_name'] != "":
                fullname = f"[+] Fullname => {data['graphql']['user']['full_name']}"
            else:
                fullname = "[-] Fullname not found."

            if data['graphql']['user']['biography'] != "":
                bio = f"[+] Bio => {data['graphql']['user']['biography']}"
            else:
                bio = f"[-] Bio not found."
            
            followers = f"[+] Followers => {data['graphql']['user']['edge_followed_by']['count']}"
            following = f"[+] Following => {data['graphql']['user']['edge_follow']['count']}"

            publication = f"[+] Number of publication => {data['graphql']['user']['edge_owner_to_timeline_media']['count']}"

            if data['graphql']['user']['is_private'] == True:
                private = f"{GREEN}[+] 🔒 Account is private!{WHITE}"
            else:
                private = f"[+] 🔓 Account is public!{WHITE}"

            if data['graphql']['user']['is_business_account'] == True:
                buisness = f"{GREEN}[+] 👨🏻‍💼 Buisness Account!{WHITE}"
            else:
                buisness = f"[-] 🐌 No Buisness Account!{WHITE}"
            
            if data['graphql']['user']['is_verified'] != None:
                verified = f"{GREEN}[+] ☑ Account is verified!{WHITE}"
            else:
                verified = f"[-] ☒ Account is not verified!{WHITE}"

            if data['graphql']['user']['business_email'] != None:
                public_email = f"{GREEN}[+] 📫 Public email ! => {data['graphql']['user']['business_email']}{WHITE}"
            else:
                public_email = f"[-] 📫 No public email."
            
            if data['graphql']['user']['business_phone_number'] != None:
                public_phone = f"{GREEN}[+] 📞 Public phone number ! => {data['graphql']['user']['business_phone_number']}{WHITE}"
            else:
                public_phone = f"[-] 📞 No public phone number."

            if data['graphql']['user']['external_url'] != None:
                external = f"{GREEN}[+] 👋 External url => {data['graphql']['user']['external_url']}{WHITE}"
            else:
                external = f"[-] 👋 No external url."


            print("✍️  Profile:\n")
            print(id)
            print(name)
            print(fullname)
            print(external)
            print(bio)
            print("\n🦉 Account:\n")
            print(private)
            print(buisness)
            print(verified)
            print()
            print(public_email)
            print(public_phone)
            print("\n🛥️  Community:\n")
            print(followers)
            print(following)
            print(publication)
            print("\n🖼️  Picture:")
            print("=>" + data['graphql']['user']['profile_pic_url'])

            print("\n📮 Potentials emails:\n")
            await gen(data['graphql']['user']['username'], data['graphql']['user']['business_email'])

            if data['graphql']['user']['business_phone_number'] != None: 
                await look(phone=data['graphql']['user']['business_phone_number'])

        except (json.JSONDecodeError, KeyError):
            print("[-] Failed to parse response JSON.")

    else:
        print("[-] Non-existent account.")

async def downloader(username: str):
    print(b1)
    sessionsId = await launch()

    cookies = {'sessionid': sessionsId}
    headers = {'User-Agent': 'Instagram 64.0.0.14.96'}
    r = await Requests(api_instagram(username), headers=headers, cookies=cookies).sender()

    data = json.loads(r.text)

    pic = await Requests(data['graphql']['user']['profile_pic_url_hd']).sender()

    with open(f"img/profile_pic_{username}.jpg", "wb") as jpgfile:
        jpgfile.write(pic.content)
        print(GREEN+"[+] Picture of profile is telecharged!"+WHITE)