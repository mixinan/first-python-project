import random

num = random.randint(0,100)
while True:
    try:
        guess = int(input('enter 1-100\n'))
    except ValueError as e:
        print("error",e)
        continue
    if guess > num:
        print('猜大了')
    elif guess < num:
        print('猜小了')
    else:
        print('ok')
        break