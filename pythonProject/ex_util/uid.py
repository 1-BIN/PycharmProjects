import uuid
from enum import unique

#universally unique identifier, 범용 고유 식별자
#128비트 길이 3.4 * 10^38
unique_filename = str(uuid.uuid4()) + '.png'
print(unique_filename)
#현재 시간 사용
import time
time_filename = time.strftime('%Y%m%d%H%M%S') + '.png'
print(time_filename)
#random값 추가
import random
time_random_filename = (time.strftime('%Y%m%d%H%M%S') + str(random.ranint(1000,9999))) + '.png'
print(time_random_filename)
#hash
import hashlib
    #현재 시간을 md5해시함수로 변환하여 유니크하게
hash = hashlib.md5(time.strftime('%Y%m%d%H%M%S').encode())
hash_filename = hash.hexdigest() + ".png"
print(hash_filename)