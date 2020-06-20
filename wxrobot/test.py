#coding=utf-8
import itchat

import requests
def get_response(msg):
    apiUrl = 'http://192.168.2.102:8000/createroom'
    data = {
        'key': 'c44dbcdb15bb40a8a8353beaebe5aa9f',  # Tuling Key,替换为你自己的
        'info': msg,  # 这是我们发出去的消息
        'userid': 'wechat-robot',  # 这里你想改什么都可以
    }
    # 我们通过如下命令发送一个post请求
    r = requests.post(apiUrl, data=data).json()
    return r.get('text')
@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    return get_response(msg['Text'])

#处理群聊文字消息
@itchat.msg_register( itchat.content.TEXT, isGroupChat = True )
def text_reply_group( msg ):
	if ( msg.content.find( '888' ) != -1 ):
		print( '金花开房' );
		print( msg['FromUserName'] );
		print( msg['ActualNickName'] );
	if ( msg.isAt ):	#判断消息是否@我
		itchat.send_msg( '收到来自{0}的消息: {1}{2}'.format( msg['ActualNickName'], msg['Text'], '(本消息来自聊天机器人)' ), toUserName = msg['FromUserName'] )
'''
@itchat.msg_register(itchat.content.TEXT)
def proc_msg(msg):
	return u'您好！主人暂时离开，稍后会给您回复...(本消息来自聊天机器人)
'''

itchat.auto_login(True)
itchat.run()