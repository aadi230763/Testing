#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

void alpha(char *input) {
    char buf[10];
    strcpy(buf, input);
    printf("%s\n", buf);
}

void beta() {
    int *p = (int*)malloc(sizeof(int));
    *p = 10;
    free(p);
    printf("%d\n", *p);
}

void gamma() {
    int x = INT_MAX;
    int y = x + 100;
    printf("%d\n", y);
}

void delta(char *input) {
    printf(input);
}

int main(int argc, char *argv[]) {
    if (argc > 1) {
        alpha(argv[1]);
        delta(argv[1]);
    }

    beta();
    gamma();

    return 0;
}
