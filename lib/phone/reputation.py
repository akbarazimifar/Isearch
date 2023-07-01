from bs4 import BeautifulSoup
from lib.requests import *
from lib.colors import *

"""
👁️ Inspector -> https://github.com/N0rz3/Inspector
"""

class Main:

    async def check(phone):

        try:
  
            response = await Requests(f"https://www.tellows.fr/num/{phone}").sender()

            html = BeautifulSoup(response.text, "html.parser")
            html_cs = html.find("div", {"class": "col-lg-9"}).findAll("h1")


            try:
                infos = html_cs[0].text.strip()
                info = f"[{GREEN}+{WHITE}] Phone number reputed for {GREEN}->{WHITE} {infos}"

            except:
                info = f"[{RED}-{WHITE}] Phone number not reputation"

            print(f"""
\n{GREEN}> {WHITE}Reputation{GREEN}
---------------------------------------------------{WHITE}

{info}
            """)

        except:
            return None