#include<stdio.h>

int main(void)
{
    int a=0, b=0;
    scanf("%d\n%d", &a, &b);

    printf("%d\n", a * (b % 10));
    printf("%d\n", a * (b % 100 / 10));
    printf("%d\n", a * (b / 100));
    printf("%d\n", a * b);

    return 0;
}