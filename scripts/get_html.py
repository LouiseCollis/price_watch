#!/bin/env python
import urllib2
from datetime import datetime

site = 'http://www.fuel-prices-europe.info/'
fh = urllib2.urlopen(site)
lines = fh.readlines()
fh.close()
now = datetime.now()
my_str_date = now.strftime('%Y%m%d')
outdir = '/Users/scollis/tmp/'
prefix = 'fuel'
postfix = '.html'
ofh = open(outdir+prefix+my_str_date+postfix, 'w')
ofh.writelines(lines)
ofh.close()

