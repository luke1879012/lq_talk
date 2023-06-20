import time


class ShovelError(Exception):
    msg = "shovel 异常"

    def alert(self):
        print(f"{self.msg=}")


class SlideError(ShovelError):
    msg = "滑块问题"


class RequestsError(ShovelError):
    msg = "请求出现问题"

    def alert(self):
        print("其他曹组")
        print(f"{self.msg=}")

def retry(func):
    times = 3

    def inner():
        for i in range(times):
            try:
                return func()
            except TimeoutError:
                print("有异常，超时了")
                print(f"重试{i + 1}次")
                time.sleep(1)

        raise RequestsError(f"报警，超时了, 重试{times}次还是挂了")

    return inner


@retry
def request():
    print("请求url.....")
    raise TimeoutError("超时了")


# r_request = retry(request)

# r_request()
try:
    request()
except SlideError as e:
    e.alert()
except RequestsError as e:
    e.alert()
except ShovelError as e:
    e.alert()
except Exception as e:
    print("兜不住了")
