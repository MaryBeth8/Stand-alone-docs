"""This project takes the weight of a package and determine the cheapest way to ship 
that package with Sal's Shipping. 
There are 3 shipping options: 
Ground shipping, Premium ground shipping, Drone shipping.
"""
# Ground shipping has a small flat charge plus a rate based on the weight of the package. 

def ground_ship_cost(weight):
  cost = 20.00
  if weight <= 2:
    cost += weight * 1.5
  elif weight <= 6:
    cost += weight * 3
  elif weight <= 10:
    cost += weight * 4
  else:
    cost += weight * 4.75
  return cost

# Premium ground shipping is only a flat charge, no charge for weight.

premium_ground_cost = 125.00

# Drone shipping has no flat charge and the rate based on weight is triple the rate of ground shipping.

def drone_ship_cost(weight):
  cost = 0.00
  if weight <= 2:
    cost += weight * 4.5
  elif weight <= 6:
    cost += weight * 9
  elif weight <= 10:
    cost += weight * 12
  else:
    cost += weight * 14.25
  return cost

# Determine the most cost-effective shipping method for a package of a given weight.

def all_shipping_cost(weight):
  if ground_ship_cost(weight) < premium_ground_cost and ground_ship_cost(weight) < drone_ship_cost(weight):
    return 'Ground shipping is the cheapest and it costs $' + str(ground_ship_cost(weight))
  elif premium_ground_cost < drone_ship_cost(weight):
    return 'Premium Ground shipping is the cheapest and it costs $125.00'
  else:
    return 'Drone shipping is the cheapest and it costs $' + str(drone_ship_cost(weight))

print(all_shipping_cost(4.8))
print(all_shipping_cost(41.5))