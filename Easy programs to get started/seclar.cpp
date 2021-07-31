#include <iostream>

using namespace std;

int main()
{
    int a,b,c;
    cin >> a;
    cin >> b;
    cin >> c;
    if (a>b & a>c){
        if (b>c){
            cout << b;
        }else{
            cout << c;
        }
    }
    if (b>a & b>c){
        if (a>c){
            cout << a;
        }else{
            cout << c;
        }
    }
    if (c>a & c>b){
        if (b>a){
            cout << b;
        }else{
            cout << a;
        }
    }
    return 0;
}