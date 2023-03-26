#include<stdio.h>
#include<stdlib.h>
int factorial(int n)
{
    int retval=1;
    while(n!=0){
        retval*=n--;
    }
    return retval;
}
int main(void){
int n;
printf("Donner un nombre:\n");
scanf("%d",&n);
int val = factorial(n);
printf("%d! = %d\n",n,val);
printf("%d! = %d\n",n-1,factorial(n-1));
printf("%d! = %d\n",n-2,factorial(n-2));

return 0;
}
