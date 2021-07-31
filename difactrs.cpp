#include <iostream>
#include <iterator>
#include <vector>
#include <algorithm>  
#define DEBUG true
using namespace std;

int main()
{
    int n,ans,count=0;
    std::vector <int> result;
    cin >> n;
    int i = 1;
    while(i <= n) {
        if(n % i == 0) {
            result.push_back(i);
            count++;
        }
        i++;
    }
    cout << count<<endl;
    if(DEBUG) {
        for(int i=0; i<result.size(); i++) {
            cout << result[i] << ' ';
        }
        cout << endl;
    }
    return 0;
}