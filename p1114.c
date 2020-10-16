#include <semaphore.h>

typedef struct {
    // User defined data may be declared here.
    sem_t * a;
    sem_t * b;
} Foo;

Foo* fooCreate() {
    Foo* obj = (Foo*) malloc(sizeof(Foo));
    obj->a = malloc(sizeof(sem_t));
    obj->b = malloc(sizeof(sem_t));

    // Initialize user defined data here.
    sem_init(obj->a, 0, 0);
    sem_init(obj->b, 0, 0);
    return obj;
}

void first(Foo* obj) {
    // printFirst() outputs "first". Do not change or remove this line.
    printFirst();
    sem_post(obj->a);
}

void second(Foo* obj) {
    // printSecond() outputs "second". Do not change or remove this line.
    sem_wait(obj->a);
    printSecond();
    sem_post(obj->b);
}

void third(Foo* obj) {
    // printThird() outputs "third". Do not change or remove this line.
    sem_wait(obj->b);
    printThird();
}

void fooFree(Foo* obj) {
    // User defined data may be cleaned up here.
    sem_destroy(obj->a);
    sem_destroy(obj->b);
    free(obj->a);
    free(obj->b);
    free(obj);
}
