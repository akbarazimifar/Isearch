from lib.colors import *
from lib.objects import TempPrint
import json

# Eyes 👀 
# Asynchrone scraping

class Eyes:
    """
    Scrap each post username and highlight those that do not match the targeted profile
    """
    def __init__(self, data):
        self.data = data

    async def extract(self) -> list:
        usernames = []
        try:
            edges = self.data['graphql']['user']['edge_owner_to_timeline_media']['edges']

            for edge in edges:
                node = edge['node']

                if 'owner' in node:
                    username = node['owner']['username']
                    usernames.append(username)

        except (KeyError, json.JSONDecodeError):
            print("[-] The account has no post.")

        return usernames

    async def matcher(self):
        count = 0

        extracted_usernames = await self.extract()

        target_username = self.data['graphql']['user']['username']

        try:
            TempPrint("\n[EYES] 🎭 Search of possible secondary accounts...", temp=3).TPrint()
            for name in extracted_usernames:
                if name.lower() != target_username.lower():
                    count += 1
                    print(f"{GREEN}[+] {count} Account{'s' if count > 1 else ''} found having participated in a publication-> @{name}{WHITE}")

            if count == 0:
                print(f"[-] Eyes could not find any accounts that participated in a post.")

        except Exception as ex:
            print(ex)
