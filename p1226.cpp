#include <bits/stdc++.h>

using namespace std;

class DiningPhilosophers {
private:
    mutex forks[5];
public:
    DiningPhilosophers() {
        
    }

    void wantsToEat(int philosopher,
                    function<void()> pickLeftFork,
                    function<void()> pickRightFork,
                    function<void()> eat,
                    function<void()> putLeftFork,
                    function<void()> putRightFork) {
		int left = philosopher;
        int right = (philosopher+1)%5;
        if(philosopher%2 == 1) {
            forks[left].lock();
            forks[right].lock();
        } else {
            forks[right].lock();
            forks[left].lock();
        }
        pickLeftFork();
        pickRightFork();
        eat();
        putLeftFork();
        putRightFork();
        if(philosopher%2 == 1) {            
            forks[right].unlock();
            forks[left].unlock();
        } else {            
            forks[left].unlock();
            forks[right].unlock();
        }
        
    }
};
