# Write a Python program using multiprocessing.Pool to calculate the sum of all even numbers from 1 to n for every number from the given list.

from multiprocessing import Pool
import os

def SumEven(n):

    total = 0

    for i in range(2, n + 1, 2):

        total += i

    print("Process ID :", os.getpid())
    print("Input Number :", n)
    print("Sum of Even Numbers :", total)
    print("---------------------------")

def main():

    Data = [1000000, 2000000, 3000000, 4000000]

    with Pool() as p:
        
        p.map(SumEven, Data)

if __name__ == "__main__":
    main()