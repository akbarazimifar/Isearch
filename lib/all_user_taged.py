from lib.requests import *
from lib.api import api_instagram
from lib.objects import TempPrint
import json

class Finder:
    def __init__(self, data, headers, cookies):
        self.data = data
        self.headers = headers
        self.cookies = cookies

    async def extract_users(self):
            usernames_tag = []
            
            utimeline_media = self.data["graphql"]["user"]["edge_owner_to_timeline_media"]

            for edge in utimeline_media["edges"]:
                tagged_users = edge["node"]["edge_media_to_tagged_user"]["edges"]
                
                for tagged_user in tagged_users:
                    username = tagged_user["node"]["user"]["username"]

                    if username != self.data['graphql']['user']['username']:
                        usernames_tag.append(username)
        
            return usernames_tag

    async def account_to_id(self):
        founds = 0
        users = await self.extract_users()

        already_shown = []

        print()
        TempPrint("-> 🐅 Scraping of all tagged profiles...").TPrint()
        try:
            for user in users:
                if user in already_shown:
                    continue
                else:
                    founds += 1
                    r = await Requests(api_instagram(user), headers=self.headers, cookies=self.cookies).sender()
                    data = json.loads(r.text)

                    user_id = data['logging_page_id'].strip('profilePage_')


                    print(f"\r- Name: @{user}\n   ╚═════ID : {user_id}\n")
                    already_shown.append(user)

            if founds == 0:
                print("[-] The target has not tagged a profile.")

        except:
            pass
