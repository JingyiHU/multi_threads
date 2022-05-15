import concurrent.futures
import blog_spider

# craw
with concurrent.futures.ThreadPoolExecutor() as pool:
    # function, iterables
    # 方法和对应的任务列表
    # <generator object Executor.map.<locals>.result_iterator at 0x1054d0660>
    # 每个html和每个url是一一对应的
    htmls = pool.map(blog_spider.craw, blog_spider.urls)
    htmls = list(zip(blog_spider.urls, htmls))

    for url, html in htmls:
        print(url, len(html))

print("Craw over")

# parse
with concurrent.futures.ThreadPoolExecutor() as pool:
    futures = {}
    # use submit to handle one by one,
    # return a future object
    for url, html in htmls:
        future = pool.submit(blog_spider.parse, html)
        # future 和 url建立关系
        futures[future] = url

    # for future, url in futures.items():
    #     print(url, future.result())

    # using as_complete
    # parse 的时候任务执行顺序不定，谁先执行完，谁完成
    for future in concurrent.futures.as_completed(futures):
        url = futures[future]
        print(url, future.result())


