#include <iostream>
#include <algorithm>
using namespace std;

int main(){
	int N,K,count = 0;
	cin >> N >> K;
	int arr[N];
	for (int i=0; i<N; i++){
		cin >> arr[i];
	}
	for (int i = 0; i < N; i++){
        if (arr[i] == K){
        	count += 1;
        }
	}
	if (count > 0){
    	cout << 1;
    }else{
    	cout << -1;
    }
}