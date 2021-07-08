# django
from django.shortcuts import render
from django.http import HttpResponseForbidden,HttpResponse
from .models import infection,prefecture

#csrf無効化
from django.views.decorators.csrf import csrf_exempt

# linebot関連
from linebot import LineBotApi,WebhookHandler
from linebot.models import MessageEvent,TextMessage,TextSendMessage,FollowEvent

# .env関連
import os
from os.path import join, dirname
from dotenv import load_dotenv

# error関連
from linebot.exceptions import InvalidSignatureError

# Load .env
load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
CHANNEL_SECRET = os.environ.get('CHANNEL_SECRET')

line_bot_api = LineBotApi(ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

@csrf_exempt
def webhook(request):
    # signatureの取得
    signature = request.META['HTTP_X_LINE_SIGNATURE']
    body = request.body.decode('utf-8')

    try:
        # 署名の検証を行い、成功した場合にhandleされたメソッドを呼び出す
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        return HttpResponseForbidden()

    return HttpResponse('送信完了')


# テキストメッセージが送信された時のハンドルイベント
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    prefecture_obj = prefecture.objects.filter(name=event.message.text).first()
    if prefecture_obj == None:
        reply_text = "都道府県を正式名称で入れてください。"
    else:
        latest_infection = infection.objects.filter(prefecture=prefecture_obj).order_by('date').reverse().first()
        if latest_infection == None:
            reply_text = '感染者情報が取得できませんでした。'
        else:
            reply_text = f'{prefecture_obj.name}の感染者数は、{latest_infection.date_string}で、{latest_infection.infection}人です。'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply_text)
    )

# 友達追加した際のイベントを仮組で追加
@handler.add(FollowEvent)
def handle_follow(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='追加してくれてありがとう!')
    )
