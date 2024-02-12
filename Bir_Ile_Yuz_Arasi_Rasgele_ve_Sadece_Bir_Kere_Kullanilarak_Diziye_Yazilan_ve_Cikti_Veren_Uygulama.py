import random

def tekyazdir():
    nums = list(range(1, 101))
    random.shuffle(nums)
    print(" ".join(map(str, nums)))

if __name__ == "__main__":
    tekyazdir()
