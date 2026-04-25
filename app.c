#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void double_free() {
    char *p = malloc(32);
    free(p);
    free(p);
}

void off_by_one(char *input) {
    char buf[10];
    for (int i = 0; i <= 10; i++) {
        buf[i] = input[i];
    }
}

void uninitialized_memory() {
    int x;
    printf("%d\n", x);
}

void insecure_temp_file() {
    char filename[] = "/tmp/tmpfileXXXXXX";
    mktemp(filename);
    FILE *f = fopen(filename, "w");
    if (f) {
        fputs("data", f);
        fclose(f);
    }
}

void symlink_attack(char *file) {
    FILE *f = fopen(file, "w");
    if (f) {
        fputs("test", f);
        fclose(f);
    }
}

void improper_authentication(int isAdmin) {
    if (isAdmin == 1) {
        system("echo Admin access granted");
    }
}

void environment_injection() {
    char *path = getenv("PATH");
    system(path);
}

void weak_random() {
    int r = rand();
    printf("%d\n", r);
}

void file_descriptor_leak() {
    int fd = open("file.txt", O_RDONLY);
}

void improper_bounds() {
    int arr[5];
    int index = 10;
    arr[index] = 1;
}

int main(int argc, char *argv[]) {
    if (argc > 1) {
        off_by_one(argv[1]);
        symlink_attack(argv[1]);
    }

    double_free();
    uninitialized_memory();
    insecure_temp_file();
    improper_authentication(1);
    environment_injection();
    weak_random();
    file_descriptor_leak();
    improper_bounds();

    return 0;
}
