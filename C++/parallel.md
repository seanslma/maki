# parallel

## lock
```cpp
#include <iostream>
#include <thread>
#include <mutex>

int v = 1;

void critical_section1(int change_v)
{
    static std::mutex mtx;
    std::lock_guard<std::mutex> lock(mtx);

    // execute contention works
    v = change_v;
    // mtx will be released after leaving the scope
}

void critical_section2(int change_v)
{
    static std::mutex mtx;
    std::unique_lock<std::mutex> lock(mtx);
    // do contention operations
    v = change_v;
    std::cout << v << std::endl;

    // release the lock
    lock.unlock();
    // during this period, others are allowed to acquire v

    // start another group of contention operations        
    lock.lock(); //lock again
    v += 1;
    std::cout << v << std::endl;
}

int main()
{
    //basic
    std::thread t([]() {
        std::cout << "hello world." << std::endl;
    });
    t.join();
    
    //lock
    std::thread t1(critical_section1, 2), t2(critical_section1, 3);
    t1.join();
    t2.join();

    std::cout << v << std::endl;
    return 0;
}
```

## future
```cpp
#include <iostream>
#include <thread>
#include <future>

int main()
{
    // pack a lambda expression that returns 7 into a std::packaged_task
    std::packaged_task<int()> task([]() { return 7; });
    // get the future of task
    std::future<int> result = task.get_future(); // run task in a thread
    std::thread(std::move(task)).detach();
    std::cout << "waiting...";
    result.wait(); //block until future has arrived
    // output result
    std::cout << "done!" << std::endl << "future result: " << result.get() << std::endl;
    return 0;
}
```
