"""Case Study:
Carly's Clippers, the newest hair salon on the block, is planning for future 
business operations and is asking for help analyzing the shop's data from last week.
Carly provided 3 lists of data for the analysis: haircuts, prices, last_week
"""

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
#the prices list corresponds to the haircuts list, 8 cuts and 8 prices

last_week = [2, 3, 5, 8, 4, 4, 6, 2]
#The number of haircuts purchased at each price last week

#Calculate the average price of a haircut

total_price = 0

for price in prices:
  total_price += price
  
average_price = total_price / len(prices)
print('Average Haircut Price: ' + str(average_price))

#Lower the price of all haircuts by $5

new_prices = [price - 5 for price in prices]
print(new_prices)

#Calculate the total revenue from last week

total_revenue = 0

for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print('Total Revenue: ' + str(total_revenue))

#Calculate the average daily revenue from last week

average_daily_revenue = total_revenue / 7
print('Average Daily Revenue: ' + str(average_daily_revenue))

#Print a list of all the haircuts that cost less than $30

cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print(cuts_under_30)
