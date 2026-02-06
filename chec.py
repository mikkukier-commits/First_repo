import random
from time import sleep


def wait_with_countdown(seconds):
    for remaining in range(seconds, 0, -1):
        print(f"Waiting... {remaining} second(s) left", end="\r")
        sleep(1)
    print(" " * 40, end="\r")  # ← це вирішує проблему


dice_roll = random.randint(1, 6)
wait_with_countdown(3)
print(f"Ви кинули {dice_roll}")
