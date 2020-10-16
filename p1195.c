#include <semaphore.h>

typedef struct {
    int i;
    int n;
    sem_t f;
    sem_t b;
    sem_t fb;
    sem_t special;
} FizzBuzz;

FizzBuzz* fizzBuzzCreate(int n) {
    FizzBuzz* obj = (FizzBuzz*) malloc(sizeof(FizzBuzz));
    obj->i = 1;
    obj->n = n;
    sem_init(&obj->f, 0, 0);
    sem_init(&obj->b, 0, 0);
    sem_init(&obj->fb, 0, 0);
    sem_init(&obj->special, 0, 0);
    return obj;
}

// printFizz() outputs "fizz".
void fizz(FizzBuzz* obj) {
    for(int i = 0; i < obj->n/3; ++i) {
        sem_wait(&obj->f);
        sem_wait(&obj->f);
        sem_wait(&obj->f);
        if (obj->i%5 != 0) {
            printFizz();
            sem_post(&obj->special);
        }
    }
}

// printBuzz() outputs "buzz".
void buzz(FizzBuzz* obj) {
    for(int i = 0; i < obj->n/5; ++i) {
        sem_wait(&obj->b);
        sem_wait(&obj->b);
        sem_wait(&obj->b);
        sem_wait(&obj->b);
        sem_wait(&obj->b);
        if (obj->i%3 != 0)  {
            printBuzz();
            sem_post(&obj->special);
        }
    }
}

// printFizzBuzz() outputs "fizzbuzz".
void fizzbuzz(FizzBuzz* obj) {
    for(int i = 0; i < obj->n/15; ++i) {
        sem_wait(&obj->fb);
        sem_wait(&obj->fb);
        sem_wait(&obj->fb);
        sem_wait(&obj->fb);
        sem_wait(&obj->fb);
        sem_wait(&obj->fb);
        sem_wait(&obj->fb);
        sem_wait(&obj->fb);
        sem_wait(&obj->fb);
        sem_wait(&obj->fb);
        sem_wait(&obj->fb);
        sem_wait(&obj->fb);
        sem_wait(&obj->fb);
        sem_wait(&obj->fb);
        sem_wait(&obj->fb);
        printFizzBuzz();
        sem_post(&obj->special);
    }
}

// You may call global function `void printNumber(int x)`
// to output "x", where x is an integer.
void number(FizzBuzz* obj) {
    for(int i = 1; i <= obj->n; ++i) {
        sem_post(&obj->f);
        sem_post(&obj->b);
        sem_post(&obj->fb);
        if (i%3 == 0 || i%5 == 0)
            sem_wait(&obj->special);
        else
            printNumber(i);
        ++obj->i;
    }
}

void fizzBuzzFree(FizzBuzz* obj) {
    sem_destroy(&obj->f);
    sem_destroy(&obj->b);
    sem_destroy(&obj->fb);
    sem_destroy(&obj->special);
    free(obj);
}
