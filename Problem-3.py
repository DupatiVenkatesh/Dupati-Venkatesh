def generate_Pattern(a):
    ans = []
    # Loop 'a' times to get 'a' number of odd values
    for i in range(a):
        # Formula for odd number: 2*i + 1
        val = (2 * i) + 1
        ans.append(str(val))
    
    print(", ".join(ans))

if __name__ == "__main__":
    try:
        x = int(input("Enter integer a: "))
        generate_Pattern(x)
    except ValueError:
        print("Please enter a valid number")