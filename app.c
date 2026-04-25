#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

void processA(char *input) {
    char buf[16];
    strcpy(buf, input);
    printf("%s\n", buf);
}

void processB() {
    int *p = (int*)malloc(sizeof(int));
    *p = 42;
    free(p);
    printf("%d\n", *p);
}

void processC() {
    int x = INT_MAX;
    int y = x + 10;
    printf("%d\n", y);
}

void processD() {
    char *arr = (char*)malloc(10);
    for (int i = 0; i < 20; i++) {
        arr[i] = 'A';
    }
    free(arr);
}

void processE() {
    int *p = NULL;
    printf("%d\n", *p);
}

void processF(char *input) {
    printf(input);
}

int main(int argc, char *argv[]) {
    if (argc > 1) {
        processA(argv[1]);
        processF(argv[1]);
    }

    processB();
    processC();
    processD();
    processE();

    return 0;
}
