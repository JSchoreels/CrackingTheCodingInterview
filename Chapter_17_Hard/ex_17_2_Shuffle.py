import time
import random

def shuffle(cards):
    assert len(cards) == 52
    for i in range(1,52):
        pick = random.randint(0,i)
        cards[i], cards[pick] = cards[pick], cards[i]
    return cards

avg = 0
for i in range(100):
    start = time.time()
    print(shuffle([i for i in range(52)]))
    duration = time.time()-start
    avg = avg * (i) / (i+1) + duration / (i+1)
    print(duration)
print(avg)