#include <semaphore.h>

typedef struct {
    // User defined data may be declared here.
    sem_t h;
    sem_t o;
} H2O;

H2O* h2oCreate() {
    H2O* obj = (H2O*) malloc(sizeof(H2O));
    // Initialize user defined data here.
    sem_init(&obj->h, 0, 0);
    sem_init(&obj->o, 0, 0);
    return obj;
}

void hydrogen(H2O* obj) {
    sem_post(&obj->h);
    sem_wait(&obj->o);
    // releaseHydrogen() outputs "H". Do not change or remove this line.
    releaseHydrogen();
}

void oxygen(H2O* obj) {
    sem_wait(&obj->h);
    sem_wait(&obj->h);
    // releaseOxygen() outputs "O". Do not change or remove this line.
    releaseOxygen();
    sem_post(&obj->o);
    sem_post(&obj->o);
}

void h2oFree(H2O* obj) {
    // User defined data may be cleaned up here.
    sem_destroy(&obj->h);
    sem_destroy(&obj->o);
    free(obj);
}
