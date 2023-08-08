#include <stdio.h>
#include <math.h>
int main( )
{
     int a, b, c, delta;
     float root1, root2;
     printf("Enter a: ");
     scanf("%d", &a);
     printf("Enter b: ");
     scanf("%d", &b);
     printf("Enter c: ");
     scanf("%d", &c);
     delta = b*b - 4*a*c;
     if (delta >= 0)
     {
     root1 = (-b - sqrt(delta)) / (2*a);
     root2 = (-b + sqrt(delta)) / (2*a);
     printf("Roots are: %.1f %.1f\n", root1, root2);
     }
     
     return 0;
}
