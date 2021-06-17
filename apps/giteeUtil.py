import requests
from app import app

ClientID = "f78fcfce176f2786be6fdc89b3c748544187892b2ba019bf17a715018418373d"
ClientSecret = "80965b1524138d3447b68df60f4b53b7a2347084be841bc185c220ebdcb71f51"
CallbackAuthUrl = "https://api.upkg.net/gitee/callback/authorize/{}"
CallbackTokenUrl = "https://api.upkg.net/gitee/callback/token"


# Authorization callback URL
# https://api.upkg.net/gitee/login

# 文档 https://gitee.com/api/v5/swagger

@app.route("auth/github/")
def getAuth(token):
    callbackUrl = CallbackTokenUrl.format(token)
    ouathUrl = "https://gitee.com/oauth/authorize?client_id={}&redirect_uri={}&response_type=code".format(ClientID,
                                                                                                          callbackUrl)
    # https://api.upkg.net/gitee/login?code=4b6125d570c974d2add766288cbb1bbbb5757553d61f6875b35fb0a9afa5a762


def callback_auth(code):
    code = "4b6125d570c974d2add766288cbb1bbbb5757553d61f6875b35fb0a9afa5a762"
    tokenUrl = "https://gitee.com/oauth/token?grant_type=authorization_code&code={}&client_id={}&client_secret={}&redirect_uri={}" \
        .format(code, ClientID, ClientSecret, CallbackTokenUrl)


