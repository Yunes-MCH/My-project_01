/*#include<stdio.h>
#include <stdlib.h>
int main(int argc, char const *argv[])
{   
    char z,e,r;
	char *a='y';
	char *b='m';
	char tem;
tem=*a;
*a=*b;
*b=tem;
printf("apres:A=%c et B=%c\n",a,b);
	return 0;
}
*/
#include<stdio.h>
#include<stdlib.h>
int main()
{
    char a,b,*pa,*pb;
   
   pa = &a;
   pb = &b; 
   char tmp;
    printf("Entrez le premier charactere (a): ");
    scanf("%c",pa);
    getchar();
    printf("Entrez le deuxieme charactere (b): ");
    scanf("%c",pb);
    printf("a = %c et b = %c.\n",a,b);
    tmp = *pa;
    *pa = *pb;
    *pb = tmp;
    printf("a = %c et b = %c.\n",a,b);
    system("pause");
    return 0;
}