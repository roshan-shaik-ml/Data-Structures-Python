from LeastFrequentUsed import LFU

if __name__ == "__main__":

    lfu = LFU(3)
    lfu.put(1, 1)
    lfu.put(2, 1)
    lfu.put(3, 1)
    for i in range(4):
        lfu.get(1)

    for i in range(3):
        lfu.get(2)
    
    for i in range(5):
        lfu.get(3)

    lfu.diaplayingHeap()
    lfu.put(4, 1)
    lfu.displayHeap()
      
    