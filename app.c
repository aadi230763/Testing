#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

void alpha(char *user) {
    char query[256];
    sprintf(query, "SELECT * FROM users WHERE name='%s'", user);
    printf("%s\n", query);
}

void beta(char *input) {
    char buf[8];
    strcpy(buf, input);
    printf("%s\n", buf);
}

void gamma() {
    char *p = (char*)malloc(20);
    strcpy(p, "hello");
    free(p);
    printf("%s\n", p);
}

void delta() {
    int *p = NULL;
    *p = 10;
}

void epsilon() {
    int *p = (int*)malloc(100 * sizeof(int));
    p[0] = 1;
}

void zeta() {
    int x = INT_MAX;
    int y = x + 5;
    printf("%d\n", y);
}

int main(int argc, char *argv[]) {
    if (argc > 1) {
        alpha(argv[1]);
        beta(argv[1]);
    }

    gamma();
    delta();
    epsilon();
    zeta();

    return 0;
}
