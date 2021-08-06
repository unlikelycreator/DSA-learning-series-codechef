#include<iostream>
using namespace std;

int main()
{
	int side1, side2, side3;
	cin >> side1 >> side2 >> side3;
	if ((b+c) > a & (a+c) > b & (a+b) > c){
		if(side1 == side2 && side2 == side3){
	  		cout << 1;
	  	}
	  	else if(side1 == side2 || side2 == side3 || side1 == side3){
	  		cout << 2;
		}
	  	else if (side1 != side2 != side3){
	    	cout << 3;
	  	}
	}else{
		cout << -1;
	}
 	return 0;
}