# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 21:42:38 2020

@author: kevin01258511
"""

import pttCrawler
import pandas as pd
import sys

html = pttCrawler.getForum("CVS")
dict = pttCrawler.forum_to_data(html)
df = pd.DataFrame(dict)
df.head()