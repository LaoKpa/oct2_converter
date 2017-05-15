# What is OCT2 converter?
OCT2 Converter is a Python3.6 limit order book data tool, converter and feature extractor that allow the order flow data to be downloaded and converted to a more research friendly OCT2-format. This project has initially been coducted as a part of the "Big data in finance" -project http://bigdatafinance.eu/, and subsequently released under GPLv3 licence.

## Input data format
See Trading Physics input file specs here: http://www.tradingphysics.org/Resources/Specifications/HistoricalItch.aspx#CSV

## OCT2-format
Output is hdf5-format (https://support.hdfgroup.org/HDF5/). A detailed description of the cointained tables can be found in oct2_tables.pptx.

# Installation
None required. Just run from either converter.ipynb or obdt.py.

# Basic Usage
## Step 1: Input file download
Download raw data to be converted. You will need an trading physics account and your customer number and pw hash and some available download credits.

```python
dl_path = '/data/input' # target folder 
ticker = 'SPY' # ticker min_date = '2014-05-26' # first date to get 
max_date = '2015-01-01' # first date not to get 
c_num = '111-222-333' # trading physics account customer number 
pw_hash = 'XXXXXXXXXXXXXXXXXXXXXX' # trading physics account password hash 
obdt = tools.OrderBookDataTool() # create order book data tools object obdt.getdata(ticker,min_date,max_date,c_num,pw_hash,dl_path)
```

## Step 2: Initial conversion
Convert csv file(s) to oct2-hdf5 format.

```python
input_folder = '/data/input' # input data path
output_folder = '/data/output' # output data path
mode = 'w' # use over(w)rite or (a)ppend mode
obdt = tools.OrderBookDataTool() # create order book data tools object 
obdt.convert(input_folder,output_folder,mode) # convert data to oct2 format
```

## Step 3: Feature calculation
Calculate additional features to append the OCT2 data into OCT2+ format.

```python
input_file = '/data/output/SPY_OCT2.h5’ # file from initial conversion
output_file = '/data/output_plus/SPY_OCT2_PLUS.h5’ # file path for output
date = ’2013_01_11’
ticker = ’SPY’
debug_mode = False # set true to skip most of the work for testing purposes
ob = OrderBook(ticker,input_file)
ob.build_features(date,output_file,debug_mode)
```

# Use with CSC Taito array jobs
Files with names starting: 'obdt_csc...' contain a usage example of using the converter with CSC taito array jobs (https://research.csc.fi/taito-array-jobs) to convert a large batch of input files concurrently utilizing the clusters resources. 

