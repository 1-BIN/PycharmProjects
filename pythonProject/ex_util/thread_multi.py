import threading
import time

def worker(number):
    print(f"스레드 {number} 작업 시작")
    time.sleep(1)
    print(f"스레드 {number} 작업 완료")

threads = []
#5개 스레드 생성 실행
for i in range(5):
    #스레드 생성
    thread = threading.Thread(target=worker, args=(i,))
    threads.append(thread)
    #실행
    thread.start()
#스레드가 종료될 때까지 기다림
for thread in threads:
    thread.join()
print("모든 작업 종료")