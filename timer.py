import time

count_seconds = int(input("Enter your time limit for timer: "))
gap = float(input("Enter the time gap between\n\033[1mYou can enter floating numbers for millisecond difference too\033[0m: "))
# Here we have used an escape sequence to highlight words in between a print statement i.e,
# \033[1m................\033[0m
n = int(input("Press 0 for printing all\nPress 1 for only odd\nPress other 0 and 1 for only even: "))

if n == 1:
    for i in reversed(range(count_seconds + 1)):
        if i%2 == 1:
            print(i, end = '\n', flush = True)
            time.sleep(gap)
elif n == 0:
    for i in reversed(range(count_seconds + 1)):
        if i > 0:
            print(i, end = '\n', flush = True)
            time.sleep(gap)
else:
    for i in reversed(range(count_seconds + 1)):
        if i%2 == 0:
            print(i, end = '\n', flush = True)
            time.sleep(gap)            