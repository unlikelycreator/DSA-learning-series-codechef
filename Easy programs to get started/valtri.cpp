#include <iostream>

using namespace std;

int main(){
	int N,ans;
	cin >> N;
	if ((N%5 == 0) || (N%6 == 0)){
		cout << "YES";
	}else{
		cout << "NO";
	}
}