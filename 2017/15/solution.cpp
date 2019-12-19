#include <stdio.h>
#include <iostream>
#include <chrono>

using namespace std;
using namespace std::chrono;

long long int testA = 65;
long long int testB = 8921;

long long int startA = 722;
long long int startB = 354;

long long int factorA = 16807;
long long int factorB = 48271;

long int divider = 2147483647;

long long int generatorA(int source)
{
    return (source * factorA) % divider;
}

long long int generatorB(int source)
{
    return (source * factorB) % divider;
}

int main(void)
{
    auto start = high_resolution_clock::now();

    int result = 0;
    long long int a, b;
    for (int i = 0; i < 40000000; i++)
    {
        startA = generatorA(startA);
        startB = generatorB(startB);
        //cout << "A: " << testA << endl;
        //cout << "B: " << testB << endl;
        a = startA & 0x0000FFFF;
        b = startB & 0x0000FFFF;
        if (a == b)
        {
            result++;
        }
    }
    auto stop = high_resolution_clock::now();

    auto duration = duration_cast<milliseconds>(stop - start);
    cout << duration.count() << endl;
    cout << "Result: " << result << endl;
}