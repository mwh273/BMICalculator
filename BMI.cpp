#include <iostream>

using namespace std;

int main() 
{
  string height = "";
  string height_in = "";
  int weight;

  cout << "Hello this is the start of my BMI Calculator Program: \n";
  cout << "Please enter in your height in feet(ex: 5ft): ";
  cin >> height;
  cout << "\nNext, please enter in your height in inches after feet: (if you are 5 ft 4 in you would enter in 4in): ";
  cin >> height_in;
  cout << "\nFinally, please enter in your weight in pounds (lbs): ";
  cin >> weight;

  cout << "\n" << height << " and " << height_in << " with " << weight <<  "lbs\n";

  cout << "\n";

  return 0;
}
