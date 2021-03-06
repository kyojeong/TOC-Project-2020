import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv,find_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from fsm import TocMachine
from utils import send_text_message
import graphviz


dotenv_path = os.path.join(os.path.dirname(__file__), 'example.env')
load_dotenv(dotenv_path)

machine = TocMachine(
    states=["user", "hello","movie"
            ,"q1","q2","q3","q4","q5","q6","q7","q8","q9","q10","q11","q12","q13","q14"
            ,"q15","q16","q17","q18","q19","q20","q21","q22"
            ,"a1","a2","a3","a4","a5","a6","a7","a8","a9","a10","a11","a12","a13","a14","a15"
            ],
    transitions=[
        {"trigger": "advance","source": "user","dest": "hello","conditions": "is_going_to_hello"},        
        {"trigger": "go_back", "source":"hello", "dest": "user"},
        
        
        {"trigger": "advance","source": "user","dest": "movie","conditions": "is_going_to_movie"},        
        {"trigger": "go_back", "source":"movie", "dest": "user"},
        
        
        {"trigger": "advance","source": "user","dest": "q1","conditions": "is_going_to_q1"},        
        
        {"trigger": "advance","source": "q1","dest": "q2","conditions": "is_going_to_q2"},              
        {"trigger": "advance","source": "q1","dest": "q3","conditions": "is_going_to_q3"},        
        
        {"trigger": "advance","source": "q2","dest": "q4","conditions": "is_going_to_q4"},        
        {"trigger": "advance","source": "q2","dest": "q5","conditions": "is_going_to_q5"},  
        
        {"trigger": "advance","source": "q3","dest": "q6","conditions": "is_going_to_q6"},        
        {"trigger": "advance","source": "q3","dest": "q7","conditions": "is_going_to_q7"},
        
        {"trigger": "advance","source": "q4","dest": "q8","conditions": "is_going_to_q8"},        
        {"trigger": "advance","source": "q4","dest": "q9","conditions": "is_going_to_q9"},
        
        {"trigger": "advance","source": "q5","dest": "q10","conditions": "is_going_to_q10"},        
        {"trigger": "advance","source": "q5","dest": "q11","conditions": "is_going_to_q11"},
        
        {"trigger": "advance","source": "q6","dest": "q12","conditions": "is_going_to_q12"},        
        {"trigger": "advance","source": "q6","dest": "q11","conditions": "is_going_to_q11"}, 
        
        {"trigger": "advance","source": "q7","dest": "q11","conditions": "is_going_to_q11"},        
        {"trigger": "advance","source": "q7","dest": "q10","conditions": "is_going_to_q10"}, 
        
        {"trigger": "advance","source": "q8","dest": "q13","conditions": "is_going_to_q13"},        
        {"trigger": "advance","source": "q8","dest": "q14","conditions": "is_going_to_q14"},
        
        {"trigger": "advance","source": "q9","dest": "q15","conditions": "is_going_to_q15"},        
        {"trigger": "advance","source": "q9","dest": "q16","conditions": "is_going_to_q16"},
        
        {"trigger": "advance","source": "q10","dest": "q17","conditions": "is_going_to_q17"},        
        {"trigger": "advance","source": "q10","dest": "q18","conditions": "is_going_to_q18"},
        
        {"trigger": "advance","source": "q11","dest": "q19","conditions": "is_going_to_q19"},        
        {"trigger": "advance","source": "q11","dest": "q20","conditions": "is_going_to_q20"},
        
        {"trigger": "advance","source": "q12","dest": "q21","conditions": "is_going_to_q21"},        
        {"trigger": "advance","source": "q12","dest": "q22","conditions": "is_going_to_q22"},
        
        {"trigger": "advance","source": "q13","dest": "a15","conditions": "is_going_to_a15"},        
        {"trigger": "advance","source": "q13","dest": "a10","conditions": "is_going_to_a10"}, 
        
        {"trigger": "advance","source": "q14","dest": "a12","conditions": "is_going_to_a12"},        
        {"trigger": "advance","source": "q14","dest": "a15","conditions": "is_going_to_a15"},
        
        {"trigger": "advance","source": "q15","dest": "a7","conditions": "is_going_to_a7"},        
        {"trigger": "advance","source": "q15","dest": "a4","conditions": "is_going_to_a4"}, 
        
        {"trigger": "advance","source": "q16","dest": "a1","conditions": "is_going_to_a1"},        
        {"trigger": "advance","source": "q16","dest": "a2","conditions": "is_going_to_a2"},
        
        {"trigger": "advance","source": "q17","dest": "a9","conditions": "is_going_to_a9"},        
        {"trigger": "advance","source": "q17","dest": "a1","conditions": "is_going_to_a1"},
        
        {"trigger": "advance","source": "q18","dest": "a6","conditions": "is_going_to_a6"},        
        {"trigger": "advance","source": "q18","dest": "a10","conditions": "is_going_to_a10"}, 
        
        {"trigger": "advance","source": "q19","dest": "a3","conditions": "is_going_to_a3"},        
        {"trigger": "advance","source": "q19","dest": "a5","conditions": "is_going_to_a5"}, 
        
        {"trigger": "advance","source": "q20","dest": "a14","conditions": "is_going_to_a14"},        
        {"trigger": "advance","source": "q20","dest": "a9","conditions": "is_going_to_a9"},
        
        {"trigger": "advance","source": "q21","dest": "a8","conditions": "is_going_to_a8"},        
        {"trigger": "advance","source": "q21","dest": "a7","conditions": "is_going_to_a7"},
        
        {"trigger": "advance","source": "q22","dest": "a11","conditions": "is_going_to_a11"},        
        {"trigger": "advance","source": "q22","dest": "a13","conditions": "is_going_to_a13"}, 
        
        
        {"trigger": "go_back", "source":"a1", "dest": "user"},
        {"trigger": "go_back", "source":"a2", "dest": "user"},
        {"trigger": "go_back", "source":"a3", "dest": "user"},
        {"trigger": "go_back", "source":"a4", "dest": "user"},
        {"trigger": "go_back", "source":"a5", "dest": "user"},
        {"trigger": "go_back", "source":"a6", "dest": "user"},
        {"trigger": "go_back", "source":"a7", "dest": "user"},
        {"trigger": "go_back", "source":"a8", "dest": "user"},
        {"trigger": "go_back", "source":"a9", "dest": "user"},
        {"trigger": "go_back", "source":"a10", "dest": "user"},
        {"trigger": "go_back", "source":"a11", "dest": "user"},
        {"trigger": "go_back", "source":"a12", "dest": "user"},
        {"trigger": "go_back", "source":"a13", "dest": "user"},
        {"trigger": "go_back", "source":"a14", "dest": "user"},
        {"trigger": "go_back", "source":"a15", "dest": "user"},
  
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET")
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")

if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
       
    except InvalidSignatureError:
        abort(400)
        

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
         
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        #print(f"\nFSM STATE: {machine.state}")
        #print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            send_text_message(event.reply_token, "你說什麼？")

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT")
    app.run(host="0.0.0.0", port=port, debug=True)
