#include <cstring>
#include <iostream>
#include <sstream>
#include <algorithm>
using namespace std;
 
int main(){
	string words[10];
	int j = 0;
    string str = "A-computer-science-portal-for-geeks";
    for (int i = 0; i < str.length(); ++i) {
        if (str[i] == '-') {
            str[i] = ' ';
        }
    }
    stringstream ssin(str);
    while (ssin.good() && j < str.length()){
        ssin >> words[j];
        ++j;
    }
    sort(words,words+str.length(),greater<int>()); 
    for(int i = 0; i < str.length(); i++){
        cout << words[i] << endl;
    }
    return 0;
}