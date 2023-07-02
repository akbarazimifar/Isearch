BASE_URL = "https://www.instagram.com/"

def api_instagram(username: str):

    api = f"{BASE_URL}{username}/?__a=1&__d=dis"

    return api
