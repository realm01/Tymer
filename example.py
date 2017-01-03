import Tymer
from time import sleep


@Tymer.interval(wait=1)
def print_interval(a, b):
    print('Hello World', a, b)


print_interval.start(2, 4)
print_interval(1, 2)
sleep(5)
print_interval.stop()


@Tymer.timeout(wait=2)
def print_timeout():
    print('Hello Mars')

print_timeout.start()

s = input('press enter to close\n')
