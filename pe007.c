#include <stdio.h>
#include <stdbool.h>
#include <math.h>

int prime(int n)
{
    int primes[10001] = {2}, p;
    for (int k = 1; k < n; k++) {
        int i = primes[k - 1];
        bool isPrime = false;
        while (!isPrime) {
            i++;
            isPrime = true;
            for (int j = 0, p = primes[j]; j < k; p = primes[++j]) {
                if (p * p > i)
                    break;
                if (i % p == 0) {
                    isPrime = false;
                    break;
                }
            }
        }
        primes[k] = i;
    }
    return primes[n - 1];
}

int main()
{
    printf("%d\n", prime(10001));
    return 0;
}
