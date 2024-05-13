#include <stdio.h>

int main(){
    
    int line;
    
    scanf("%d\n", &line);
    
    for(int i=0; i<line; i++)
    {
        for(int j=line; j>0; j--)
        {
            if(j>i+1)
            {
               printf(" ");
            }
            else { printf("*");}
        }
        printf("\n");
    }
    
    return 0;
}