#include <stdio.h>

int main()
{
    int p[10000] = {0}, temp, t;
    for (int i = 1; i < 3000; i++) {
        t = (temp = i * (3 * i - 1) / 2) % 10000;
        while (p[t])
            t++;
        p[t] = temp;
    }
    
    for (int i = 0; i < 9999; i++)
        for (int j = i + 1; j < 10000; j++)
            if (p[i] && p[j] && p[i] < p[j]) {
                t = (temp = p[j] + p[i]) % 10000;
                while (p[t] && p[t] != temp)
                    t++;
                if (p[t] != temp)
                    continue;
                
                t = (temp = p[j] - p[i]) % 10000;
                while (p[t] && p[t] != temp)
                    t++;
                if (p[t] == temp)
                    printf("%d\n", temp);
            }
    
    return 0;
}
