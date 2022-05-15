import flask
import json
import time
from concurrent.futures import ThreadPoolExecutor


# name is cur file's name
app = flask.Flask(__name__)
# 初始化一个全局的pool就行
pool = ThreadPoolExecutor()


# 写一个访问接口
# 这个方法对应的链接是根目录
def read_file():
    time.sleep(0.1)
    return "file result"


def read_db():
    time.sleep(0.2)
    return "db result"


def read_api():
    time.sleep(0.3)
    return "api result"


@app.route("/")
def index():
    # 模拟web读取文件，数据库，api的操作
    # 用submit获取一个future对象，然后用result获取结果
    result_file = pool.submit(read_file)
    result_db = pool.submit(read_db)
    result_api = pool.submit(read_api)

    return json.dumps({
        "result_file": result_file.result(),
        "result_db": result_db.result(),
        "result_api": result_api.result(),
    })


# 启动flask
if __name__ == "__main__":
    app.run()


