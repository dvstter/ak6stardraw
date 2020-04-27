from random import *
from tqdm import *
import numpy as np


def oneshot():
	total = 10
	prob = 0.02
	
	while True:
		star6cnt = len(list(filter(lambda x: x <= prob, [random() for _ in range(10)])))
		if star6cnt:
			break
		total += 10
		if total>=50:
			prob += 0.02
		if total == 300:
			break
			
	return total, star6cnt

def oneshot_super():
	total, cnt = oneshot()
	while not len(list(filter(lambda x: x <= 0.35, [random() for _ in range(cnt)]))):
		tmp, cnt = oneshot()
		total += tmp
		
		if total >= 300:
			total = 300
			break
			
	return total

def run(super=False):
	result = []
	for _ in tqdm(range(1000000)):
		if not super:
			result += [oneshot()[0]]
		else:
			result += [oneshot_super()]
		
	return  result


if __name__ == "__main__":
	result = run(True)
	#for e in result: print(e)
	print("aver: %f, median: %d" % (np.mean(result), np.median(result)))