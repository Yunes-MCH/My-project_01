
#include<stdio.h>
#include<stdlib.h>
int main()
{
    int a,b,s;
    int *pa,*pb,*ps;
    pa = &a;
    pb = &b;
    ps = &s;
    printf("donnez deux entiers:\n");
    scanf("%d%d",pa,pb);
    *ps = *pa + *pb;
    printf("la somme est %d.\n",s);
    system("pause");
    return 2;
}
