from queue import PriorityQueue

if __name__ == "__main__":

    queue = PriorityQueue()
    queue.put((99, 'Roshan'))
    queue.put((2, 'Siva'))
    queue.put((8, 'Rajesh'))
    queue.put((7, 'Hari'))

    while not queue.empty():
        print(queue.get())