#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: nikolas.schnellbaecher@bioquant.uni-heidelberg.de
# date: 2018-04-26
# file: mp_pool_apply_async_calling_python.py
##########################################################################################

import time
import datetime
import os
import sys
import math
import numpy as np
import multiprocessing as mp

now = datetime.datetime.now()
now = "%s-%s-%s" %(now.year, str(now.month).zfill(2), str(now.day).zfill(2))

BASEDIR = os.path.dirname(os.path.abspath(__file__))

def workerThread(threadID):
    
    print "threadID = ", threadID
    
    ################
    # DO WORK HERE #
    ################
    
    time.sleep(10) # delays for 10 seconds
	
    return threadID
   
if __name__ == '__main__':

	batchIterable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	results = []
	    
	NUMCPUS = mp.cpu_count() - 1
	pool = mp.Pool(NUMCPUS)

	for i in range(len(batchIterable)):
	    
	    results.append(pool.apply_async(workerThread, (batchIterable[i],)))

	pool.close()
	pool.join()

	results = [r.get() for r in results if r.get() is not None]
	print results

