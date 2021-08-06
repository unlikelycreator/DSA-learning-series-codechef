#include <iostream>
using namespace std;

int main(){
	int N;
	cin >> N;
	
}

n = int(input())
m,c = [],[]
l = [i for i in range(1,5*(n+1))]
for i in range(n):
	m.append(l[i*5:(i+1)*5])
for i in range(n):
	if i%2!=0:
		m[i]=m[i][::-1]
for i in m:
	for j in i:
		print(j,  end= " ")
	print()