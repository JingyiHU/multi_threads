import flask
from concurrent.futures import ProcessPoolExecutor
import math
import json

# flask's name take cur file's name
app = flask.Flask(__name__)


# 模拟cpu密集型计算
# cpu bound, no io
def is_prime(num):
    # num can only be divided by 1 and himself
    if num < 2:
        return False

    if num % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(num)))

    for i in range(3, sqrt_n + 1, 2):
        if num % i == 0:
            return False

    return True


@app.route("/is_prime/<numbers>")
def api_is_prime(numbers):
    nums_list = [int(x) for x in numbers.split(",")]
    res = process_pool.map(is_prime, nums_list)
    return json.dumps(dict(zip(nums_list, res)))


if __name__ == "__main__":
    # 这个必须放在最下面，每个进程之间是相互隔离的
    # 对于多线程，变量定义在哪里都很灵活，因为它们共享当前环境中的所有变量
    # 但是对于多进程，在flask中，必须在main函数中，且在apprun之前初始化pool
    # 然后所有进程都可以用这个pool了
    process_pool = ProcessPoolExecutor()
    app.run()


