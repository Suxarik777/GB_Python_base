from progress.bar import Bar
import time #таймер

bar = Bar('Processing', max=20)

for i in range(20):
    time.sleep(1)   # выполняем торможение нашего кода на 1 секунду
    bar.next()
bar.finish()