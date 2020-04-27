from random import *
from tqdm import *
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter


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
	for _ in tqdm(range(10000000)):
		if not super:
			result += [oneshot()[0]]
		else:
			result += [oneshot_super()]
		
	return  result

def main():
	result = run(True)
	# for e in result: print(e)
	
	print("aver: %f, median: %d" % (np.mean(result), np.median(result)))
	
	# draw image
	d = dict(Counter(result))
	draw_times = d.keys()
	performance = [d[x] for x in draw_times]
	
	fig = plt.figure(figsize=(8, 8))
	plt.bar(draw_times, performance, align="center", width=5)
	plt.xlabel('Counter')
	plt.title('Designated 6* draw times')
	fig.savefig("result.png", dpi=200)


if __name__ == "__main__":
	#main()
	
	# data have got
	d = {60: 856200, 50: 795954, 210: 124524, 20: 631636, 170: 197197, 30: 590732, 260: 68718, 10: 678202, 300: 385762,
	 40: 550493, 70: 759561, 80: 609916, 220: 109995, 130: 326589, 140: 288631, 150: 252886, 100: 419289, 110: 386257,
	 290: 48044, 120: 360324, 180: 175860, 160: 221233, 90: 487394, 230: 97708, 200: 139514, 240: 86991, 270: 61051,
	 190: 157477, 250: 77541, 280: 54321}
	s = sum(d.values())
	
	# process data
	draw_times = list(d.keys())
	draw_times = sorted(draw_times)
	performance = [d[x] for x in draw_times]
	ratios = []
	for i in draw_times:
		ratios.append(d[i] / s)
	
	fig, ax1 = plt.subplots(figsize=(8, 8))
	color = "tab:blue"
	ax1.bar(draw_times, performance, align="center", width=5)
	ax1.tick_params(axis="y", labelcolor=color)
	ax1.set_ylabel("frequency", color=color)
	ax1.set_xlabel("times")
	
	ax2 = plt.twinx()
	color = "tab:red"
	ax2.set_ylabel("percentage", color=color)
	ax2.tick_params(axis='y', labelcolor="tab:red")
	ax2.plot(draw_times, ratios, color=color)

	plt.title("Designated 6* draw times")
	fig.savefig("result.png", dpi=200)
