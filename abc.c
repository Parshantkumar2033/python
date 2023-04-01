#include<stdio.h>
int main()
{
    int i, j, n;
    char spaces;
    int count;
    printf("Enter the no. lines you want to print = ");
    scanf("%d", &n);

    
    for(i = 0; i<n; i++)
    {
        printf("%d", spaces);
        for(j = 0; j <= i; j++)
        {
            printf("*");
        }
    }
}




