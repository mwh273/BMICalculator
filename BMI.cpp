#include <iostream>
#include <string>
#include <sstream>

using namespace std;

int main() 
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
  


  cout << "Hello this is the start of my BMI Calculator Program: \n";
  cout << "Please enter in your height in feet(ex: 5ft): ";
  cin >> height;
  cout << "\nNext, please enter in your height in inches after feet: (if you are 5 ft 4 in you would enter in 4in): ";
  cin >> height_in;
  cout << "\nFinally, please enter in your weight in pounds (lbs): ";
  cin >> weight;

  cout << "\n" << height << " and " << height_in << " with " << weight <<  "lbs\n";

  new_weight = weight * 0.45;
  ftss << height[0];
  ftss >> ft;
  inss << height_in[0];
  inss >> in;
  //cout << ft << "\t" << in << "\n";
  new_height = ((ft * 12) + in) * 0.025;
  new_height = new_height * new_height;
  BMI = new_weight / new_height;

  cout << "\nThe BMI is: " << BMI << "\n";

  if(BMI >= 30)
    cout << "You are Obese.\n";
  else if(BMI < 30 && BMI >= 25)
    cout << "You are Overweight.\n";
  else if(BMI < 25 && BMI >= 18.5)
    cout << "You are Normal weight.\n";
  else if(BMI < 18.5)
    cout << "You are Underweight.\n";

  return 0;
}
