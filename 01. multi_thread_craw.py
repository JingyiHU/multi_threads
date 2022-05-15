import blog_spider
import threading
import time


def single_thread():
    print("single thread begin")
    for url in blog_spider.urls:
        blog_spider.craw(url)
    print("single thread end")


def multi_thread():
    print("multi threads begin")
    threads = []
    for url in blog_spider.urls:
        threads.append(
            # 元组，所以是(url,)
            # target只写函数名字即可，args是参数
            threading.Thread(target=blog_spider.craw, args=(url,))
        )

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("multi threads end")


if __name__ == "__main__":
    start = time.time()
    single_thread()
    end = time.time()

    print("single thread costs: ", end - start, "seconds")

    start = time.time()
    multi_thread()
    end = time.time()

    print("multi threads costs: ", end - start, "seconds")
