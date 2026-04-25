#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <fstream>
#include <thread>
#include <climits>

using namespace std;

void bufferOverflow(const char* input) {
    char buffer[10];
    strcpy(buffer, input);
}

void heapOverflow() {
    char* ptr = (char*)malloc(10);
    strcpy(ptr, "This string is too long for heap");
    free(ptr);
}

void stackOverflow() {
    stackOverflow();
}

void useAfterFree() {
    int* ptr = new int(10);
    delete ptr;
    cout << *ptr << endl;
}

void formatString(char* userInput) {
    printf(userInput);
}

void integerOverflow() {
    int a = INT_MAX;
    int b = a + 1;
    cout << b << endl;
}

void commandInjection(const string& user) {
    string cmd = "ls " + user;
    system(cmd.c_str());
}

void pathTraversal(const string& filename) {
    ifstream file("/var/www/" + filename);
}

void sqlInjection(const char* username) {
    char query[256];
    sprintf(query, "SELECT * FROM users WHERE name='%s'", username);
    cout << query << endl;
}

void nullPointer() {
    int* ptr = nullptr;
    cout << *ptr << endl;
}

void memoryLeak() {
    int* ptr = new int[100];
}

int shared = 0;
void raceCondition() {
    for (int i = 0; i < 100000; i++) {
        shared++;
    }
}

void unsafeDeserialization(const string& file) {
    ifstream in(file);
    string data;
    in >> data;
}

int main(int argc, char* argv[]) {
    if (argc > 1) {
        bufferOverflow(argv[1]);
        formatString(argv[1]);
        sqlInjection(argv[1]);
        commandInjection(argv[1]);
        pathTraversal(argv[1]);
    }

    heapOverflow();
    integerOverflow();
    useAfterFree();
    memoryLeak();
    nullPointer();

    thread t1(raceCondition);
    thread t2(raceCondition);
    t1.join();
    t2.join();

    unsafeDeserialization("input.txt");

    return 0;
}
