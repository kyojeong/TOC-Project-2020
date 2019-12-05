import os
from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage,ImageSendMessage

import requests 
from bs4 import BeautifulSoup
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

def movie():
    target_url = 'https://movies.yahoo.com.tw/'
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')   
    content = ""
    for index, data in enumerate(soup.select('div.movielist_info h2 a')):
        if index == 6:
            return content       
        title = data.text
        link =  data['href']
        content += '{}\n{}\n'.format(title, link)
    
    return content



"""
def send_button_message(id, text, buttons):
    pass
"""
