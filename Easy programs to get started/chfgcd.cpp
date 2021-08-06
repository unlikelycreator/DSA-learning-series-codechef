#include <iostream>
using namespace std;

int main()
{
	int t,x,y;
	cin >> t;
	int i = 0;
	cin >> x >> y;
	while (i<t){
		if (y%x==0){
			cout << 0;
		}else{
			y+=1;
			if (y%x==0){
				cout << 0;
			}
			t+=1;
		}
		i++;
	}
	return 0;
}
