def display_invoice(username, amount, due_date):
    
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}") #the .2f will only show 2 decimal places
    
    
display_invoice("Khalid", 50.645, "6-12")