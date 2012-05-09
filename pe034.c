#include <stdio.h>
int fac(int n)
{
    if (n == 0)
        return 1;
    return n * fac(n - 1);
}
int main()
{
    int f[10];
    for (int i = 0; i < 10; i++)
        f[i] = fac(i);
    int sum = 0;
    for (int i = 10; i < 10000000; i++) {
        int s = 0, t = i;
        do {
            s += f[t % 10];
        } while(t /= 10);
        if (i == s)
            sum += i;
    }
    printf("%d\n", sum);
    return 0;
}
