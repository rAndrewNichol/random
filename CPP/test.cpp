#include <iostream>
using namespace std;

int sumSquares(int num1 = 0, int num2 = 0){
	int sum = 0;
	for(int i = num1 + 1; i<num2; i++){
		sum += i*i;
	}
	return(sum);
}
/*
int length(int array[] = NULL){
	int l = 0;
	while(array[i] != NULL){
		l ++;
	}
	return(l);
}
*/

int main(){
	int list[5] = {1,2,3,4,5};
	cout << "sumSquares: " << sumSquares(1,5) << endl;
//	cout << "length: " << length(list) << endl;
}
