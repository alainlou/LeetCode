#include <semaphore.h>

typedef struct {
    int n;
    sem_t a;
    sem_t b;
} FooBar;

FooBar* fooBarCreate(int n) {
    FooBar* obj = (FooBar*) malloc(sizeof(FooBar));
    obj->n = n;
    sem_init(&obj->a, 0, 0);
    sem_init(&obj->b, 0, 1);
    return obj;
}

void foo(FooBar* obj) {

    for (int i = 0; i < obj->n; i++) {
        sem_wait(&obj->b);
        // printFoo() outputs "foo". Do not change or remove this line.
        printFoo();
        sem_post(&obj->a);
    }
}

void bar(FooBar* obj) {

    for (int i = 0; i < obj->n; i++) {
        sem_wait(&obj->a);
        // printBar() outputs "bar". Do not change or remove this line.
        printBar();
        sem_post(&obj->b);
    }
}

void fooBarFree(FooBar* obj) {
    sem_destroy(&obj->a);
    sem_destroy(&obj->b);
    free(obj);
}
