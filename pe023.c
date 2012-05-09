#include <stdio.h>
#include <stdbool.h>
#include <math.h>

#define M 28124

bool abundant(int n)
{
    int temp = 1, sq = sqrt(n);
    for (int i = 2; i <= sq; i++) {
        if (n % i == 0) {
            temp += i;
            if (i < n / i)
                temp += n / i;
        }
    }
    return temp > n;
}

int main()
{
    int a[M] = {}, aa = 0;
    for (int i = 1; i < M; i++) {
        if (abundant(i))
            a[aa++] = i;
    }
    
    bool b[M] = {};
    for (int i = 0; i < aa; i++) {
        for (int j = i; j < aa; j++) {
            if (a[i] + a[j] < M)
                b[a[i] + a[j]] = true;
        }
    }
    
    int sum = 0;
    for (int i = 1; i < M; i++)
        if (!b[i])
            sum += i;
    printf("%d\n", sum);
    return 0;
}
