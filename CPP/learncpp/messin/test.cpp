#include<iostream>

int get_value(){
	int x;
	std::cout << "Enter a number: ";
	std::cin >> x;
	return x;
}

int main(){
	std::cout << get_value() << std::endl;
	return 0;
}
