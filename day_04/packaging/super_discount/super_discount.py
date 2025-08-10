# List Comprehension
prices = [1000,10,200,100,300]

# Convert the numbers into half their original values
discounted_prices = [ int(price /2) for price in prices]
print(discounted_prices)
