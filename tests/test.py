import qstock as qs

#获取沪深A股最新行情指标
df=qs.realtime_data()
#查看前几行
print(df.head())

tt = qs.realtime_data(code=['中国平安','300684','锂电池ETF','BK0679','上证指数'])
print(tt)

df=qs.realtime_change('60日新高')
#查看前几行
print(df.head())

#个股code_list可以输入代码或简称或多个股票的list
#获取中国平安2022年9月28日至今的5分钟数据，默认前复权
df=qs.get_data('中国平安',start='20220928',freq=5)
print(df.tail())


df=qs.stock_holder_top10('中国平安', n=2)
print(df)


df=qs.macro_data('gdp')
print(df)


#获取中国平安2022年至今前复权的数据
df=qs.get_data('中国平安',start='2022-06-01',end='2022-10-20')
df.tail()

#使用默认参数
qs.kline(df)