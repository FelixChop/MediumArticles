"""
100 light bulbs are turned off.
100 prisoners consecutively walk through the bulbs and click on the switch.
The switch turns on the bulb if it was turned off, and inversely.
The first prisoner clicks the switch of every bulb.
The second clicks the switch of the 2nd, 4th, 6th and so on till the 100th bulb.
The third clicks the switch of the 3rd, 6th, and so on.
After the 100th prisoner takes its turn, the question is:
how many bulbs are turned on?
"""
n = 100
bulbs = {i:False for i in list(range(1,n+1))} # False means turned off

def prisoner(keys, bulbs):
	for key in keys:
		bulbs[key] = not bulbs[key]

# prisoner i acts => all multiples of i are changed
def function_is_divider(i):
	def is_divider(n):
		return n % i == 0
	return is_divider

def round(i):
	prisoner(filter(function_is_divider(i), bulbs), bulbs)

a = list(map(round, bulbs.keys()))

# Magic
sum(val for val in bulbs.values())

import random
random.seed(42)

# Turn on the light with a probability p
import pandas as pd
from scipy.stats import bernoulli
X = bernoulli(0.5)

def prisoner(keys, bulbs, X):
	for key in keys:
		if X.rvs():
			bulbs[key] = not bulbs[key]

def random_event(X):
	bulbs = {i:False for i in list(range(1,n+1))}
	def round(i): prisoner(filter(function_is_divider(i), bulbs), bulbs, X)
	a = list(map(round, bulbs.keys()))
	return pd.DataFrame([bulbs.values()])


from tqdm import tqdm

simulations = 1000

results = pd.DataFrame([
	(x, pd.concat([random_event(bernoulli(x/simulations)) for i in range(100)]).reset_index(drop=True).sum(axis=1).mean())
	for x in tqdm(range(simulations+1))
	])
