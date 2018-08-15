from pympler import summary, muppy
import psutil
from resource import resource
import os
import sys

def memory_usage_psutil():

	process = psutil.Process(os.getpid())
	mem = process.get_summary_info()[0] / float(2 ** 20)
	return mem

def memory_usage_resource():

	rusage_denom = 1024
	return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / rusage_denom
