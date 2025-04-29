import multiprocessing

def contador(numero):
    for i in range(numero):
        print(i)

if __name__ == '__main__':
    for i in range(5):
        p = multiprocessing.Process(target=contador, args=(1000000,))
        p.start()