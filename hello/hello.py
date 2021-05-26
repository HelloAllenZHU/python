#!/usr/bin/python3

import tushare as ts

# 打印tushare版本信息
print(ts.__version__)

# token
token = 'df191c6281ef517ce65eedad01592cf08c7614e350706d630f848b7d'

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
df = pro.daily(ts_code='601789.SH', start_date='20210501', end_date='20210526')

print( df )