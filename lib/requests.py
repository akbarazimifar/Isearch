import requests

class Requests:
    def __init__(self, 
                url: str,
                headers=None,
                cookies=None):
        self.url = url
        self.head = headers
        self.cook = cookies

    async def sender(self):
        try:
            return requests.get(url=self.url, headers=self.head, cookies=self.cook)

        except requests.HTTPError as h:
            print(f"[-] HTTP Error! : {h}")