onumbers={}
enumbers={}
while True:
    user_input=input("Enter a number (or 'over' to exit):")
    if user_input.lower()=='over':
        break
    else:
        number=int(user_input)
        if number%2!=0:
            onumbers[number]=(number**2,number**3)
        else:  
            enumbers[number]=(number**2,number**3)
print("odd dictionary is:",onumbers)
print("even dictionary is:",enumbers)
