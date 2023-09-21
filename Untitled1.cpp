#include <bits/stdc++.h> // header file includes every Standard library
using namespace std;

int main() {

	// Your code here
	int t;
	cin>>t;
	int nums[t];
	if(t>=1 && t<=10){
	for(int i=0; i<t; i++){
		int num;
		cin>>num;
		int prod1 = 1;
		for(float temp=1; temp<=100000000000000000; temp++){
			int testnum, r, prod=1, k;
			testnum=temp;
			for(k=testnum; k>0; k=k/10){
				r = k%10;
				prod = prod*r;
			}
	if(prod==num){
		prod1 = temp;
		break;
	}
	
		}
		nums[i] = prod1;
	}

	for(int j=0; j<t; j++){
		cout<<nums[j]<<endl;
	}
	}
	return 0;
}
