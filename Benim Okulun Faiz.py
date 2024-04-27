year = 1
price = 8000
print('The',year,'.','year price of school is ', price)
perc = 0.03
while year <=4:
    year = year + 1 
    new_price = (price) + (price * perc)
    print('The',year,'.','year price of school is ', format(new_price, '.2f'))
    price = new_price