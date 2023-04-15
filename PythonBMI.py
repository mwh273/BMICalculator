print("Hello this is the start of my BMI Calculator Program: \n")
  
height = input("Please enter in your height in feet(ex: 5ft): ")
  
height_in = input("\nNext, please enter in your height in inches after feet: (if you are 5 ft 4 in you would enter in 4in): ")
  
weight = input("\nFinally, please enter in your weight in pounds (lbs): ")

print("\n" + height + " and " + height_in + " with " + weight +  "lbs\n")

new_weight = int(weight) * 0.45;

ft = height[0]

inches = height_in[0];

new_height = ((int(ft) * 12) + int(inches)) * 0.025;
new_height = new_height * new_height;

BMI = new_weight / new_height;

print("\nThe BMI is: " + str(BMI) + "\n")

if BMI >= 30:
  print("You are Obese.\n")
elif BMI < 30 and BMI >= 25:
  print("You are Overweight.\n")
elif BMI < 25 and BMI >= 18.5:
  print("You are Normal weight.\n")
elif BMI < 18.5:
  print("You are Underweight.\n")



