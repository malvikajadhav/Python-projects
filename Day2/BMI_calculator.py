ht = input("ENter height: ")
wt = input("ENter weight: ")
bmi = (float(wt)/(float(ht)**2))
value = ""
if bmi<=18.5:
    value = "underweight"
elif 18.5<bmi<=25:
    value = "normal weight"
elif 25<bmi<=30:
    value = "overweight"
elif 30<bmi<=35:
    value = "obese"
else:
    value = "clinically obese"
print(f"Your bmi is {round(bmi,2)}, you are {value}")
