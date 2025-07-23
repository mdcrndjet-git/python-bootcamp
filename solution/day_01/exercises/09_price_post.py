# Price notification template
price_notification = "The price of {} is ${}."

# Post: Latte ($3.50)
print(price_notification.format("Latte", 3.50))

# Post: Espresso ($2.75)
print(price_notification.format("Espresso", 2.75))

# Post: Cappuccino ($4.00)
print(price_notification.format("Cappuccino", 4.00))
