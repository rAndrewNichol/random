#include <iostream>
using namespace std;

int rec_tri(int max, int i = 0, int summ = 0){
	cout << summ + i << endl;
	if(i == max){
		return 0;
	}
	else{
		return rec_tri(max, i+1, summ + i);
	}
}

int main(){
	rec_tri(15);
	return 0;
}

