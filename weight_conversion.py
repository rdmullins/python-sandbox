weight = input("Weight? ")
unit = input("(K)g or (L)bs: ")

if unit == "L" or unit == "l":
    print("Weight in Kg: " + str(float(weight)*0.453592))
elif unit == "K" or unit == "k":
    print("Weight in Lbs: " + str(float(weight)/0.453592))
else:
    print("Invalid unit.")
