from obdt import *
import sys

obdt = OrderBookDataTool()
input_files = ['/proj/kanniain/data/trading_physics_raw/spy/20130102-SPY.csv',
	'/proj/kanniain/data/trading_physics_raw/spy/20130111-SPY.csv']
output_folders = ['/proj/kanniain/data/trading_physics_oct2/spy/20130102',
	'/proj/kanniain/data/trading_physics_oct2/spy/20130111']
job = int(sys.argv[1])-1
mode = 'w'
obdt.convert(input_files[job],output_folders[job],mode) # convert data to oct2 format