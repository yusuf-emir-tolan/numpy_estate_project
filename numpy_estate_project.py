import numpy as np

m2 = np.random.randint(70,201,1000)
nmbr_room = np.random.randint(2,7,1000)
district_code = np.random.randint(0,3,1000)
prices = (m2 * 5000) + (nmbr_room* 15000) + (district_code * 30000)
print (f"\nAverage prices of houses:{np.mean(prices)}")
print (f"\nThe median of prices of houses:{np.median(prices)}")
print (f"\nRisk of prices of houses:{np.std(prices)}")

cheap_filter = (district_code == 0) & (prices < np.mean(prices))

how_many = np.sum(cheap_filter)

print(f"\nOpportunity Houses Count: {how_many}")
 
