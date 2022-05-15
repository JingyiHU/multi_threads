import threading
import time

lock = threading.Lock()


class Account:
    def __init__(self, balance):
        self.balance = balance


def draw(account: Account, balance):
    with lock:
        if account.balance >= balance:
            # 即使在sleep的时候切换了第二个线程，但是因为它没有lock，所以也没有办法进入if语句
            # 前面出问题的原因是切换线程的时候都进入了if语句
            # 第二个线程获取了锁进来的时候发现balance已经不够了，所以直接跳到24行，取钱失败
            time.sleep(0.1)
            print(threading.current_thread().name,
                  "取钱成功")
            account.balance -= balance
            print(threading.current_thread().name,
                  "余额", account.balance)
        else:
            print(threading.current_thread().name,
                  "取钱失败，余额不足")


if __name__ == "__main__":
    # init account
    account = Account(1000)
    thread_a = threading.Thread(name="thread_a", target=draw, args=(account, 800))
    thread_b = threading.Thread(name="thread_b", target=draw, args=(account, 800))

    thread_a.start()
    thread_b.start()
