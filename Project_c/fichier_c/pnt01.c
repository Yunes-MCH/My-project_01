#include<stdio.h>
#include <stdlib.h>
void function_sum(int *nb1, int *nb2){
int *sum;
	*sum=*nb1+*nb2;
	printf("la somme de deux nombre est:%d\n",*sum);
}
int main(void)
{
	int nb1=9;
	int nb2=10;
	int *pionteur_nb1=&nb1;
	int *pionteur_nb2=&nb2;
	function_sum(pionteur_nb1,pionteur_nb2);
	
	return 0;
}