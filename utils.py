import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage,ImageSendMessage


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)

    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))
  
    return "OK"


def send_image_url(reply_token,image_url,text):
    
    line_bot_api = LineBotApi(channel_access_token)
   
    line_bot_api.reply_message(reply_token,[ImageSendMessage(original_content_url=str(image_url), preview_image_url=str(image_url)),TextSendMessage(text=text)] )
        
    return "OK"

def send_image(reply_token,image_url):
    
    line_bot_api = LineBotApi(channel_access_token)
   
    line_bot_api.reply_message(reply_token,ImageSendMessage(original_content_url=str(image_url), preview_image_url=str(image_url)) )
        
    return "OK"



"""
def send_button_message(id, text, buttons):
    pass
"""
