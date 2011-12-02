#!/usr/bin/python
import sys
from datetime import datetime

n = datetime.now()

if n.month == 12 and n.day >= 25:
    print u'\U00002721'
else:
    print u'\U00005B50'
    #print u'\U0000884C'
    #print u'\U000003B2'
