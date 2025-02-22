#include <stdio.h>

int josephus(int n, int k) {
    return (n == 1) ? 0 : (josephus(n - 1, k) + k) % n;
}

int main() {
    int n, k;
    
    // Accepting user input for n
    printf("Enter the number of people (n): ");
    scanf("%d", &n);
    
    // Setting step count (k)
    printf("Enter the step count (k): ");
    scanf("%d", &k);

    // Printing the position of the survivor (1-based index)
    printf("Survivor: %d\n", josephus(n, k) + 1);
    
    return 0;
}
