#include<stdio.h>
#include<stdlib.h>



int main(void){

int var =1999;
int *ptr;
int **pptr;
ptr=&var;
pptr=&ptr;

printf("la valeur de var=%d\n",var);
printf("le valeour de *ptr=%d\n",*ptr);
printf("la valeur de **ptr=%d\n",**pptr);

return 0;
}
