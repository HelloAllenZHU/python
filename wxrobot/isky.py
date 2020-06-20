#!/usr/bin/env python3
#coding=utf-8

#导入itchat
import itchat

#导入requests
import requests

#创建房间
def get_createroom():
	#创建房间的url
	url = 'http://192.168.2.102:8001/createroom/'
	
	#创建房间的数据，需要由群主自定义
	data='''{ "uid":		101756,
			"type": 	"zjh",
			"name": 	"%u70B8%u91D1%u82B1",
			"ju":		8,
			"person":	5,
			"mode": 	"fk",
			"detail":	{
							"bitype":	2,
							"bao":		true,
							"shuang":	true,
							"jie": 		false,
							"chao":		false,
							"feng":		5,
							"bi":		1,
							"men":1
						}
			}'''
	
	res = requests.get( url + str( data ) ).json()
	print( res )
	return str( res )

#处理群聊文字消息
@itchat.msg_register( itchat.content.SHARING, isGroupChat = False )
def text_reply_group( msg ):
	#群类型、群开房口令，2者匹配，才能调用创建房间的接口
	#群类型、群开房口令需要保存在数据库中
	'''if ( msg.content.find( '888' ) != -1 ):
		print( '金花开房' );
		return get_createroom()
	#群主收款二维码
	if ( msg.content.find( '二维码' ) != -1 ):
		print( '玩家请求群主收款二维码' )'''

	return msg['Content']

#自动登录
itchat.auto_login( True )

#运行
itchat.run()