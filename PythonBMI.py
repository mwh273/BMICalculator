void main() 
{
  stringstream ftss;
  stringstream inss;
  string height = "";
  string height_in = "";
  int weight;
  int ft = 0;
  int in = 0;
  float new_weight = 0.0;
  float new_height = 0.0;
  float BMI = 0.0;
  


  print("Hello this is the start of my BMI Calculator Program: \n")
  
  height = input("Please enter in your height in feet(ex: 5ft): ")
  
  height_in = input("\nNext, please enter in your height in inches after feet: (if you are 5 ft 4 in you would enter in 4in): ")
  
  weight = input("\nFinally, please enter in your weight in pounds (lbs): ")

  print("\n" + height + " and " + height_in + " with " + weight +  "lbs\n")

  new_weight = weight * 0.45;
  ftss << height[0];
  ftss >> ft;
  inss << height_in[0];
  inss >> in;
  # cout << ft << "\t" << in << "\n";
  new_height = ((ft * 12) + in) * 0.025;
  new_height = new_height * new_height;
  BMI = new_weight / new_height;

 print("\nThe BMI is: " + BMI + "\n")

  if BMI >= 30:
    print("You are Obese.\n")
  elif BMI < 30 and BMI >= 25:
   print("You are Overweight.\n")
  elif BMI < 25 and BMI >= 18.5:
    print("You are Normal weight.\n")
  elif BMI < 18.5:
    print("You are Underweight.\n")

  return 0;
}

