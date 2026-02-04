import time


for x in range(1,9999):
    count = 0
    print(f"For number {x}:")
    while True:
        try:
            print(x)
            if x == 1:
                break
            if x%2 == 1:
                x = x*3+1
            if x%2 == 0:
                x = x/2
                time.sleep(0.1)
            count += 1
        except:
            print("error")
    print(f"rounds: {count}")
