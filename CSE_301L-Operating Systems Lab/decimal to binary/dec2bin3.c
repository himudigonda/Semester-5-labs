#include<stdio.h>

int dec2bin(unsigned int num)
{
	unsigned int mask=32768;
	while(mask > 0)
   		{
	   	if((num & mask) == 0 )
        	 	printf("0");
	   	else
        		printf("1");
		mask = mask >> 1 ;
   		}
	return 0;
}

int main(){
	int a[10], n,i;
	n = 10;
	dec2bin(n);
	printf(" ");
	return 0;
}


