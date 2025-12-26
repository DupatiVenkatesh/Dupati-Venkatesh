def count_multiples(numbers):
    divisors = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Creating a dictionary to store counts: {1:0, 2:0...}
    counts = {d: 0 for d in divisors}

    for num in numbers:
        for d in divisors:
            # Check if num is divisible by d without a remainder
            if num % d == 0:
                counts[d] += 1
    return counts

if __name__ == "__main__":
    print("--- Multiple Counter (1 to 9) ---")
    
    # Method 1: Ask the user for input
    user_input = input("Enter numbers separated by spaces (e.g., 1 2 8 9 12): ")
    
    # Convert the string input into a list of integers
    try:
        # We split the string by spaces and convert each part to an int
        data = [int(x) for x in user_input.split()]
        
        if not data:
            print("No numbers entered. Using default list.")
            data = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]

        # Get and print results
        result = count_multiples(data)
        print("\nInput List:", data)
        print("Output Counts:", result)
        
    except ValueError:
        print("Error: Please enter only integers separated by spaces.")