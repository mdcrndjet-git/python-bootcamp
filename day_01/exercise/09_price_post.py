# Multiple String Formatting using placeholder

# Price notification template
price_notification = "The price of {} is ${}."

# Post: Latte($3.50)
coffee = "Latte"
price = "3.50"
message = price_notification.format(coffee,price)
print(message)

# Price Espresso($2.75)
coffee = "Espresso"
price = "2.75"
message = price_notification.format(coffee,price)
print(message)

# Price Cappuccino($4.00)
coffee = "Cappuccino"
price = "4.00"
message = price_notification.format(coffee,price)
print(message)