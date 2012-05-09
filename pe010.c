#include <stdio.h>
#include <stdbool.h>

int main()
{
    int k = 0, i = 2, primes[1000000] = {}, p;
    long long sum = 0;
    while (i < 2000000)  {
        sum += (primes[k++] = i);
        i = primes[k - 1];
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
    }
    printf("%ld\n", sum);
    return 0;
}
