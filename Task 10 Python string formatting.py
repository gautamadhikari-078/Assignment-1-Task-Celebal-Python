def print_formatted(number):
    # your code goes here

    width = len(bin(number)[2:])  # Calculate the width based on binary representation of number
    
    for i in range(1, number + 1):
        dec = str(i)
        octal = oct(i)[2:]  # oct() gives octal string with '0o' prefix, so slice it off
        hexa = hex(i)[2:].upper()  # hex() gives hexadecimal string with '0x' prefix, so slice it off and capitalize
        binary = bin(i)[2:]  # bin() gives binary string with '0b' prefix, so slice it off
        
        # Print formatted values in one line
        print(f"{dec:>{width}} {octal:>{width}} {hexa:>{width}} {binary:>{width}}")


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
