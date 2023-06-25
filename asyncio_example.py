# Код для Python < 3.4

import asyncio


# # # -------------------------------------------------------
# Декоратор для заміру часу виконання функції

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Функція {func.__name__} виконалася за {execution_time} секунд")
        return result
    return wrapper

# -------------------------------------------------------


@asyncio.coroutine
def async_worker(number, divider):
    print('Async Worker started with values: {} / {}'.format(number, divider))
    yield from asyncio.sleep(3)
    print(number / divider)


@timer
def main():
    event_loop = asyncio.get_event_loop()
    task_list = [
        event_loop.create_task(async_worker(1, 10)),    event_loop.create_task(async_worker(2, 11)),
        event_loop.create_task(async_worker(3, 12)),    event_loop.create_task(async_worker(4, 13)),
        event_loop.create_task(async_worker(5, 14)),    event_loop.create_task(async_worker(6, 15)),
        event_loop.create_task(async_worker(7, 10)),    event_loop.create_task(async_worker(8, 9)),
        event_loop.create_task(async_worker(9, 8)),     event_loop.create_task(async_worker(10, 7)),
        event_loop.create_task(async_worker(11, 6)),    event_loop.create_task(async_worker(12, 5)),
        event_loop.create_task(async_worker(13, 4)),    event_loop.create_task(async_worker(14, 3)),
        event_loop.create_task(async_worker(15, 2)),    event_loop.create_task(async_worker(16, 1)),
        event_loop.create_task(async_worker(17, 2)),    event_loop.create_task(async_worker(18, 3)),
        event_loop.create_task(async_worker(19, 4)),    event_loop.create_task(async_worker(20, 5)),
        event_loop.create_task(async_worker(21, 6)),    event_loop.create_task(async_worker(22, 7)),
        event_loop.create_task(async_worker(23, 8)),    event_loop.create_task(async_worker(24, 9))
    ]
    tasks = asyncio.wait(task_list)
    event_loop.run_until_complete(tasks)


if __name__ == '__main__':
    main()