URL_MAIN = "https://www.instagram.com/"

def api_instagram(username: str):

    api = f"{URL_MAIN}{username}/?__a=1&__d=dis"

    return api