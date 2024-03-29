#!/usr/bin/python3

import tushare as ts
import pandas as pd

#显示所有列
pd.set_option('display.max_columns', None)

#显示所有行
pd.set_option('display.max_rows', None)

#设置value的显示长度为1000，默认为50
pd.set_option('max_colwidth',1000)

# 打印tushare版本信息
print(ts.__version__)

# token
token = 'd541e8920dbb713d69005acf80e204efc7155152b25f977e1db66397'

# 设置token
ts.set_token( token )

# 初始化
pro = ts.pro_api()

# 获取数据
'''
df = pro.trade_cal( exchange='',            #默认SSE表示上交所
                    start_date='20210501', 
                    end_date='20210525', 
                    fields='exchange,cal_date,is_open,pretrade_date', 
                    is_open='0'
                  )
'''                  

# 获取今日4304只股票的数据
#df = pro.daily(trade_date='20210526')

# 查询当前所有正常上市交易的股票列表
'''
df = pro.stock_basic( exchange='', 
                      list_status='L', 
                      fields='ts_code,symbol,name,area,industry,list_date'
                    )
'''

# 查询当前所有正常上市交易的股票列表
'''
df = pro.query( 'stock_basic', 
                exchange='', 
                list_status='L', 
                fields='ts_code,symbol,name,area,industry,list_date'
              )
'''              

# 获取某只股票指定日期内的基本数据(不包含换手率)
df = pro.daily(ts_code='003032.SZ', start_date='20100101', end_date='20230306')


#查询当前所有正常上市交易的股票列表
#df = pro.stock_basic( exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date' )

#获取日线基本行情
#df = pro.daily( ts_code='600926.SH', start_date='20210319', end_date='20210319' )

#获取通用数据
#df = ts.pro_bar( ts_code='600926.SH', adj='None', start_date='20210319', end_date='20210319', factors=['tor', 'vr'])

#df = ts.pro_bar(ts_code='000001.SZ', start_date='20180101', end_date='20181011', factors=['tor', 'vr'])

print( df )