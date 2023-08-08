#include <stdio.h>
#include <math.h>
int main( )
{
        int     a, b, c, delta;
        float   t, r1, r2;
        printf("Enter a: ");
        scanf("%d", &a);
        printf("Enter b: ");
        scanf("%d", &b);
        printf("Enter c: ");
        scanf("%d", &c);
        if  (a==0)
                printf ("Coefficient a should be non-zero.\n");
        else {
                delta = b*b - 4*a*c;
                if (delta < 0)
                        printf("complex roots !\n");
                else {
                        t = sqrt(delta);
                        r1 = (-b - t) / (2*a);
                        r2 = (-b + t) / (2*a);
                        printf("Roots are: %.1f %.1f\n", r1, r2);
                }
        }
        return 0;
}
