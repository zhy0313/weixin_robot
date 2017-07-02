import requests
import itchat

KEY = 'af65b04282aa4d02a642a5dd74491302'


def get_response(msg):
    apiurl = 'http://www.tuling123.com/openapi/api'
    data ={
        'key': KEY,
        'info': msg,
        'userid': 'wechat-robot'
    }
    try:
        r = requests.post(apiurl, data=data).json()
        return r.get('text')
    except:
        return None


@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    default_reply = 'I received:' + msg['Text']
    reply = get_response(msg['Text'])
    return reply or default_reply

itchat.auto_login(hotReload=True)
itchat.run()
