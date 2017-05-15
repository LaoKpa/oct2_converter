from obdt import *
import sys

input_paths = ['/proj/kanniain/data/trading_physics_oct2/spy/20130102/SPY_OCT2.h5',
	'/proj/kanniain/data/trading_physics_oct2/spy/20130111/SPY_OCT2.h5']
output_paths = ['/proj/kanniain/data/trading_physics_oct2plus/spy/20130102/SPY_OCT2_PLUS.h5',
	'/proj/kanniain/data/trading_physics_oct2plus/spy/20130111/SPY_OCT2_PLUS.h5']
dates = ['2013_01_02','2013_01_11']
ticker = 'SPY'
job = int(sys.argv[1])-1
ob = OrderBook(ticker,input_paths[job])
ob.build_features(dates[job],output_paths[job],debug_mode=True) # convert data to oct2 format