def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

#phone_number = get_phone(1, 123, 456, 7890) #this is positional 
phone_number = get_phone(area=123 , country=1, last=7890 , first=456) #this is keyword, but try to be consistent with the order

print(phone_number)