from random import *
from tqdm import *


def oneshot():
	total = 10
	prob = 0.02
	while not [x for x in filter(lambda x: x <= prob, [random() for _ in range(10)])]:
		total += 10
		if total>=50:
			prob += 0.02
		if total == 300:
			break
			
	return total

def oneshot_super():

	
def run():
	result = []
	for _ in tqdm(range(1000000)):
		result += [oneshot()]
		
	return  result


if __name__ == "__main__":
	result = run()
	#for e in result: print(e)
	print("aver: ", sum(result)  / len(result))