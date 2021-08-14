import json
from linebot import LineBotApi
from linebot.models import TextSendMessage

file = open('info.json', 'r')
info = json.load(file)

CHANNEL_ACCESS_TOKEN = info["CHANNEL_ACCESS_TOKEN"]
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

def main():
    USER_ID = info["USER_ID"]
    msg = TextSendMessage(text = "鍵返しましたか?")
    line_bot_api.push_message(USER_ID, messages=msg)
    
if __name__ == "__main__":
    main()