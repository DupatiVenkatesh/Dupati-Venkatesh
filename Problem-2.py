def print_odd_series(n):
    result = []
    
    # We need 'n' number of odd numbers
    # The formula for the ith odd number is 2*i - 1
    for i in range(1, n + 1):
        val = 2 * i - 1
        result.append(str(val))
        
    # Joining list to match output format: 1, 3, 5...
    print(", ".join(result))

if __name__== "__main__":
    try:
        x = int(input("Enter input a: "))
        print_odd_series(x)
    except ValueError:
        print("Please enter a valid integer.")