def say_hi():
    print('hi!')

say_hi()

def wash(dry=False, water=8):
    print('加水', water, "分滿")
    print('baby bear')
    print('spin!')
    if dry:
        print('dryer')

wash(water = 10)

def add(x, y):
    print(x + y)
add(3, 4)

def avg(numbers):
    return sum(numbers) / len(numbers)

print(avg([1, 2, 3]))