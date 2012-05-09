#include <stdio.h>

int main()
{
    int max_s = 0, max_i = 0, steps[1000001];
    for (int i = 1; i < 1000001; i++) {
        long long n = i;
        int s = 0;
        while (n != 1) {
            if (n < i) {
                s += steps[n];
                break;
            }
            s++;
            if (n % 2 == 0)
                n /= 2;
            else
                n = 3 * n + 1;
        }
        steps[i] = s;
        if (s > max_s)
            max_s = s, max_i = i;
    }
    printf("%d %d\n", max_i, max_s);
    return 0;
}
