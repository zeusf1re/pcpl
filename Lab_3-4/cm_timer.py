import time

class cm_timer_1:
    def __enter__(self):
        self.start_time = time.time()
        return self 

    def __exit__(self, exc_type, exc_val, exc_tb): # аргументы нужны для вылета с ошибками
        end_time = time.time()
        print(f"time: {end_time - self.start_time}")

with cm_timer_1():
    time.sleep(5.5)
