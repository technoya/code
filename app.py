from flask import Flask
from flask import request
from flask import Response
import requests
import json

app=Flask(__name__)


def message1(message):
   print("msg",message)
   chat_id=message['message']['chat']['id']
   txt=message['message']['text']
   print('chatid->',chat_id)
   print('text',txt)
   return chat_id,txt

def tel_send_image(chat_id,a):
    url = "https://api.telegram.org/bot6352678677:AAF_KLce8szMVlGNjMP5hiVnEwMmsJR8cew/sendPhoto"
    payload = {
        'chat_id': chat_id,
        'photo': a,
        'caption': "profile"
    }
 
    r = requests.post(url, json=payload)
    return r

def sendmessage(chat_id,txt):
   url='https://api.telegram.org/bot6352678677:AAF_KLce8szMVlGNjMP5hiVnEwMmsJR8cew/sendMessage'
   payload={
        'chat_id':chat_id,
        'text':txt 
      }
   r=requests.post(url,json=payload)
   return r


@app.route('/', methods=['GET','POST'])

def index():
   if request.method=='POST':
       msg=request.get_json()
       

       chatid,txt=message1(msg)
       user=txt
       sendmessage(chatid,txt)
       
       return Response('ok',status=200)
       
   else:
      return "<h1> hello </h1>"
      
