import queue
import blog_spider
import time
import random
import threading


# producer
def do_craw(url_queue: queue.Queue, html_queue: queue.Queue):
    while True:
        url = url_queue.get()
        html = blog_spider.craw(url)
        html_queue.put(html)
        # adding logs
        print(threading.current_thread().name, f"craw {url}",
              "url_queue.size= ", url_queue.qsize())
        time.sleep(random.randint(1, 2))


# consumer
def do_parse(html_queue: queue.Queue, fout):
    while True:
        html = html_queue.get()
        results = blog_spider.parse(html)
        for res in results:
            fout.write(str(res) + '\n')

        time.sleep(random.randint(1, 2))
        # adding logs
        print(threading.current_thread().name, f"results.size= ", len(results),
              "html_queue.size= ", html_queue.qsize())


if __name__ == "__main__":
    url_queue = queue.Queue()
    html_queue = queue.Queue()
    # init url_queue
    for url in blog_spider.urls:
        url_queue.put(url)

    # start producer threads
    for i in range(3):
        t = threading.Thread(target=do_craw, args=(url_queue, html_queue),
                             name=f"craw{i}")
        # start thread
        t.start()

    fout = open("02.data.txt", "w")
    # start consumer threads
    for i in range(2):
        t = threading.Thread(target=do_parse, args=(html_queue, fout),
                             name=f"parse{i}")
        # start thread
        t.start()



