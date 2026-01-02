def purchase(buyer, *vegs, **vegquants):
    print(f"Hello {buyer}, here is list of veggies you bought")
    
    for veg in vegs:
        print(veg)

    print("Quantity details")
    for quant in vegquants:
        print(f"{quant} : {vegquants[quant]}")

vegs = ('potato', 'tomato', 'carrot')
vegquants = {'potato': '1kg', 'tomato': '1kg', 'carrot': '1kg'}

purchase("Mr. ABC", *vegs, **vegquants)

print("------------------------------------------")
print("------------------------------------------")

def trip(traveller, place='pune', snaks='bhel'):
    print(f"Hello {traveller}, please enjoy {snaks} which is famous in {place}")

trip("Mr. PQR")
trip("Mr. ABC", 'mumbai', 'vada-pav')
trip("Ms. XYZ", snaks="poha", place="indore")
trip("Ms. LMN", place="kolhapur")
