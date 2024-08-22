def net_price(list_price, discount =0, tax = 0.05): #what if the argument being sent to the parameter is always the same, set a default!
    
    return list_price * (1-discount) * (1+tax)

#print(net_price(500))

#print(net_price(500, 0.1)) #if we are passing an argument, then this will OVERRIDE the default value

print(net_price(500, 0.1, 0))