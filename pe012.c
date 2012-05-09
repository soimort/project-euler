#include <stdio.h>

int main()
{
    int n = 0, s = 1, m, t;
    while (s <= 500) {
        n++;
        t = m = (n + 1) * n / 2;
        s = 1;
        
        int p = 2, counter = 0;
        while (t % p == 0) {
            counter++;
            t /= p;
        }
        s *= counter + 1;
        
        p = 1;
        while (p * p <= m) {
            p += 2;
            counter = 0;
            while (t % p == 0) {
                counter++;
                t /= p;
            }
            s *= counter + 1;
        }
    }
    printf("%d\n", m);
    return 0;
}