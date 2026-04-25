#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <pthread.h>
#include <unistd.h>

int shared = 0;

void func1(char *input) {
    char buf[8];
    strcpy(buf, input);
}

void func2() {
    char *p = (char*)malloc(8);
    strcpy(p, "AAAAAAAAAAAAAAAAAAAA");
    free(p);
}

void func3() {
    func3();
}

void func4() {
    int *p = (int*)malloc(sizeof(int));
    *p = 5;
    free(p);
    printf("%d\n", *p);
}

void func5(char *input) {
    printf(input);
}

void func6() {
    int x = INT_MAX;
    int y = x + 1;
    printf("%d\n", y);
}

void func7(char *user) {
    char cmd[128];
    sprintf(cmd, "ls %s", user);
    system(cmd);
}

void func8(char *file) {
    char path[256];
    sprintf(path, "/tmp/%s", file);
    FILE *f = fopen(path, "r");
    if (f) fclose(f);
}

void func9(char *user) {
    char query[256];
    sprintf(query, "SELECT * FROM users WHERE name='%s'", user);
    printf("%s\n", query);
}

void func10() {
    int *p = NULL;
    printf("%d\n", *p);
}

void func11() {
    int *p = malloc(100 * sizeof(int));
}

void *func12(void *arg) {
    for (int i = 0; i < 100000; i++) {
        shared++;
    }
    return NULL;
}

void func13(char *file) {
    FILE *f = fopen(file, "r");
    char buf[128];
    if (f) {
        fread(buf, 1, sizeof(buf), f);
        fclose(f);
    }
}

int main(int argc, char *argv[]) {
    if (argc > 1) {
        func1(argv[1]);
        func5(argv[1]);
        func9(argv[1]);
        func7(argv[1]);
        func8(argv[1]);
    }

    func2();
    func6();
    func4();
    func11();
    func10();

    pthread_t t1, t2;
    pthread_create(&t1, NULL, func12, NULL);
    pthread_create(&t2, NULL, func12, NULL);
    pthread_join(t1, NULL);
    pthread_join(t2, NULL);

    func13("input.txt");

    return 0;
}
