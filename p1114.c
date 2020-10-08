typedef struct {
    // User defined data may be declared here.
    int state;
} Foo;

Foo* fooCreate() {
    Foo* obj = (Foo*) malloc(sizeof(Foo));
    // Initialize user defined data here.
    obj->state = 0;
    return obj;
}

void first(Foo* obj) {
    // printFirst() outputs "first". Do not change or remove this line.
    printFirst();
    obj->state += 1;
}

void second(Foo* obj) {
    while (obj->state < 1) { }
    // printSecond() outputs "second". Do not change or remove this line.
    printSecond();
    obj->state += 1;
}

void third(Foo* obj) {
    while (obj->state < 2) { }
    // printThird() outputs "third". Do not change or remove this line.
    printThird();
}

void fooFree(Foo* obj) {
    // User defined data may be cleaned up here.
}
