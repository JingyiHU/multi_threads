import asyncio
import aiohttp
import blog_spider
import time


# 定义一个在超级循环里面可以跑的函数：协程
async def async_craw(url):
    print("craw url: ", url)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            # await： 超级循环不会在这里一直等待，而是直接到下一个url的爬取
            result = await resp.text()
            print(f"craw url: , {url}, {len(result)}")

# 创建超级循环
loop = asyncio.get_event_loop()

# 创建task列表
tasks = [
    loop.create_task(async_craw(url))
    for url in blog_spider.urls]

start = time.time()
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()

print("time cost: ", end - start)
