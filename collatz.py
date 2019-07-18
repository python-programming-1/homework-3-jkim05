# Joshua Kim
# Homework 3
# collatz.py

# my solution

def collatz(num):
    try:
        while num != 1:
            if num % 2 == 0:
                new_num = num // 2
                print(new_num)
                if new_num == 1:
                    break
            else:
                new_num = num * 3 + 1
                print(new_num)
                if new_num == 1:
                    break
            num = new_num
        if num == 1:
            print(num)
    except (ValueError, TypeError):
        print("Maybe consider writing in a positive integer?")