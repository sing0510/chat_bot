from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

## input heroku login in CMD

app = Flask(__name__)

line_bot_api = LineBotApi('Al4IQ5iIYP3EU1/QOH1d2iXMTyWkl1BV+RqabYMg01kpT9MPoV/3zlPYTM7sJNFbxKUECRdF7AdHwwtwiyxX4y+FZk0JK+R2e0/J79QYzv1p08P/Kd41sIqDfbga56gWTIQscKkaWNPoL18tMDYe2gdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('c3f549de7027b87a6678ace83dec5d7a')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()

## "git push heroku HEAD:master" for pushing the file to heroku