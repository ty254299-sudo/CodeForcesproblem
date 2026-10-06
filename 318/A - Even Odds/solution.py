import sys
 
 
def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
 
    n = int(input_data[0])
    k = int(input_data[1])
 
    # Calculate count of odd numbers in range 1 to n
    odds = (n + 1) // 2
 
    if k <= odds:
        # k-th odd number
        print(2 * k - 1)
    else:
        # (k - odds)-th even number
        print(2 * (k - odds))
 
 
if __name__ == "__main__":
    main()