#include<stdio.h>

int dec2bin(n){
	int binary = 0;
	int remainder, i;

	for(i = 1; n != 0; i = i * 10)
	{
		remainder = n % 2;
		n /= 2;
		binary += remainder * i;
	}
	return binary;
}


int main(){
	int n = 10;
	printf("binary number: %d\n", dec2bin(n));
	return 0;
}
