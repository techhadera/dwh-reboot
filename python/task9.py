# Python 3.9.7
import threading
import time

class Worker(threading.Thread):
  def __init__(self, thread_name, daemon = True) -> None:
    super().__init__()
    self.setName(thread_name)
  
  def run(self) -> None:
    print(f'{self.getName()} starting...')
    for i in range(10,0,-1):
      print(f'Thread name: {self.getName()}, counter: {i}')
      time.sleep(1)
    print(f'{self.getName()} end')

worker_1 = Worker('Thread_1')
worker_1.start()
worker_2 = Worker('Thread_2')
worker_2.start()