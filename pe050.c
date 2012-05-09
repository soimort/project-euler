#include <stdio.h>
#include <stdbool.h>

void generate_primes(int *primes, int stop_at)
{
    int primes_size = 0;
    for (int n = 2; n < stop_at; n++) {
        bool isComposite = false;
        for (int i = 0; i < primes_size; i++) {
            int p = primes[i];
            if (n % p == 0) {
                isComposite = true;
                break;
            } else if (p * p > n) {
                break;
            }
        }
        if (!isComposite)
            primes[primes_size++] = n;
    }
    return;
}

int sum(int *p, int start, int count)
{
    int temp = 0;
    for (int i = start; i < start + count; i++) {
        temp += p[i];
    }
    return temp;
}

bool in(int s, int *p, int p_size)
{
    for (int i = 0; i < p_size; i++)
        if (s == p[i])
            return true;
    return false;
}

int main()
{
    int objective = 1000000;
    int p[objective];
    generate_primes(p, objective);
    
    for (int k = 2000; ; k--) {
        int s = sum(p, 0, 2 * k + 2);
        if (in(s, p, objective)) {
            printf("%d %d\n", s, 2 * k + 2);
            return 0;
        }
        for (int i = 1; s <= objective; i++) {
            s = sum(p, i, 2 * k + 1);
            if (in(s, p, objective)) {
                printf("%d %d\n", s, 2 * k + 1);
                return 0;
            }
        }
    }
    return 0;
}
