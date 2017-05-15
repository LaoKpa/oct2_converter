from obdt import *

tool = OrderBookDataTool()
dl_path = '/proj/kanniain/data/trading_physics_raw/spy' # target folder
ticker = 'SPY' # ticker
min_date = '2015-01-01' # first date to get
max_date = '2015-01-07' # first date not to get
c_num = '111-222-333' # trading physics account customer number
pw_hash = 'xxx' # trading physics account password hash
tool.getdata(ticker,min_date,max_date,c_num,pw_hash,dl_path)