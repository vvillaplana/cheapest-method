#This function calculates the cost of Ground Shipping
def ground_shipping(weight):
  flat_charge = 20
  if weight <= 2:
    variable_cost = weight * 1.5
  elif weight > 2 and weight <= 6:
    variable_cost = weight * 3
  elif weight > 6 and weight <= 10:
    variable_cost = weight * 4
  else:
    variable_cost = weight * 4.75
  cost = flat_charge + variable_cost
  return cost

#This is the fixed prize of Premium Ground Shipping
premium_ground_shipping = 125

#This function calculates the cost of Drone Shipping
def drone_shipping(weight):
  flat_charge = 0
  if weight <= 2:
    variable_cost = weight * 4.5
  elif weight > 2 and weight <= 6:
    variable_cost = weight * 9
  elif weight > 6 and weight <= 10:
    variable_cost = weight * 12
  else:
    variable_cost = weight * 14.25
  
  cost = flat_charge + variable_cost
  return cost

#This function calculates which is the cheapest shipping method
def cheapest_shipping(weight):
  ground = ground_shipping(weight)
  drone = drone_shipping(weight)
  if ground < drone and ground < premium_ground_shipping:
    print("Ground Shipping is the cheapest method.")
    print("The cost is " + str(ground) + " USD.")
  if drone < ground and drone < premium_ground_shipping:
    print("Drone Shipping is the cheapest method.")
    print("The cost is " + str(drone) + " USD.")
  if premium_ground_shipping < ground and premium_ground_shipping < drone:
    print("Premium Ground Shipping is the cheapest method.")
    print("The cost is " + str(premium_ground_shipping) + " USD.")
  if ground == drone and ground < premium_ground_shipping:
    print("Ground Shipping and Drone Shipping are the cheapest methods.")
    print("The cost is " + str(ground) + " USD.")
  if ground == drone and ground > premium_ground_shipping:
    print("Premium Ground Shipping is the cheapest method.")
    print("The cost is " + str(premium_ground_shipping) + " USD.")
  if ground == premium_ground_shipping and ground < drone:
    print("Ground Shipping and Premium Ground Shipping are the cheapest methods.")
    print("The cost is " + str(ground) + " USD.")
  if ground == premium_ground_shipping and ground > drone:
    print("Drone Shipping is the cheapest method.")
    print("The cost is " + str(drone) + " USD.")
  if drone == premium_ground_shipping and drone < ground:
    print("Ground Shipping and Drone Shipping are the cheapest methods.")
    print("The cost is " + str(premium_ground_shipping) + " USD.")
  if drone == premium_ground_shipping and drone > ground:
    print("Ground Shipping is the cheapest method.")
    print("The cost is " + str(ground) + " USD.")
  else:
    print("Error! Please try again")

#Here some examples for testing
cheapest_shipping(4.8)
cheapest_shipping(41.5)
cheapest_shipping(0)
cheapest_shipping(0.1)
cheapest_shipping(1)
cheapest_shipping(12)
cheapest_shipping(25.7)
cheapest_shipping(100)
cheapest_shipping(1000)