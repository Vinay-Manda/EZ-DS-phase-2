print("Welcome to Vinay's bike showroom........")
name=str(input("enter the bike comapny-name you want to purchase :"))
if name =='hero' or name=='Hero':
    print('you have choosen Hero company bike')
    cc=int(input("enter the cubic capacity of bike :"))
    if cc==150:
        print("you have choosen ",cc,"cc bike")
        colour=str(input("enter colour of the bike :"))
        if colour=='black' or colour=='red' or colour=='green':
            print("you selected a wonderful combination of bike specifications its available..")
        else:
            print("colour is not available in this model,sorry for your inconvinience")
    if cc==200:
        print("you have choosen ",cc,"cc bike")
        colour=str(input("enter colour of the bike :"))
        if colour=='yellow' or colour=='red':
            print("you selected a wonderful combination of bike specifications its available..")
        else:
            print("colour is not available in this model,sorry for your inconvinience")
    else:
        print("cubic capacity you have entered isn't available")
elif name =='yamaha' or name=='Yamaha':
    print('you have choosen Yamaha company bike')
    cc=int(input("enter the cubic capacity of bike :"))
    if cc==150:
        print("you have choosen ",cc,"cc bike")
        colour=str(input("enter colour of the bike :"))
        if colour=='red':
            print("you selected a wonderful combination of bike specifications its available..")
        else:
            print("colour is not available in this model,sorry for your inconvinience")
    if cc==200:
        print("you have choosen ",cc,"cc bike")
        colour=str(input("enter colour of the bike :"))
        if colour=='blue' or colour=='red':
            print("you selected a wonderful combination of bike specifications its available..")
        else:
            print("colour is not available in this model,sorry for your inconvinience")
    if cc==600:
        print("you have choosen ",cc,"cc bike")
        colour=str(input("enter colour of the bike :"))
        if colour=='white':
            print("you selected a wonderful combination of bike specifications its out of stock..")
        else:
            print("colour is not available in this model,sorry for your inconvinience")
    else:
        print("cubic capacity you have entered isn't available")
elif name =='re' or name=='Re':
    print('you have choosen Re company bike')
    cc=int(input("enter the cubic capacity of bike :"))
    if cc==500:
        print("you have choosen ",cc,"cc bike")
        colour=str(input("enter colour of the bike :"))
        if colour=='black':
            print("you selected a wonderful combination of bike specifications its available and is a diesel engine..")
        else:
            print("colour is not available n this model,sorry for your inconvinience")
    else:
        print("cubic capacity you have entered isn't available")
else :
    print("bike company you have entered is not available")
print("please give your feedback")
fb=str(input("good/bad :"))
if fb=="good":
    print("good showroom")
elif fb=="bad":
    print("not that good ")
print("thank you visit again")