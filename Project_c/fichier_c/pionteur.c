#include<stdio.h>
#include<stdlib.h>
int inverser_nombres(int *pnt_A,int  *pnt_B)
{
	int temporaire=0;
        temporaire = *pnt_B;
	*pnt_B = *pnt_A;
	*pnt_A = temporaire;
	
	//printf("FONCTION APRES: A = %d et B = %d\n",nombreA, nombreB );
return *pnt_A;
}
int main(void){
	int nombreA = 15;
	int nombreB = 28;

	int *pionteursurnombreA=&nombreA;
	int *pionteursurnombreB=&nombreB;

	printf("AVANT: A = %d et B = %d\n", nombreA, nombreB );
	inverser_nombres( pionteursurnombreA,pionteursurnombreB);
	printf("APRES : A = %d et B = %d\n", nombreA, nombreB );
	return 0;
}
