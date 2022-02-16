import sys
sys.path.insert(1,'/home/lmenode1/Muonmatrix/analisis/Chodigos/lme_fiuna')
from general import *
try:
	p=None
	t=None
	c=None
	csv_to_sql(path=p,table=t,timecol=c)
	print('Done!...')
except:print('Something went wrong...')
print('Shutting down...')
