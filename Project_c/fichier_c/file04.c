#include<stdio.h>
#include<stdlib.h>
int main(void){

int t[5][2]={{1,0},{12,2},{11,3},{10,4},{9,5}};
int i,j;
printf("le tableux est t[5][2]={{1,0},{12,2},{11,3},{10,4},{9,5}}\n");

for(i=0;i<5;i++){
    for(j=0;j<2;j++){
printf("le tableuax est t[%d][%d]=%d\n",i,j,t[i][j]);
}
}





return 0;
}
