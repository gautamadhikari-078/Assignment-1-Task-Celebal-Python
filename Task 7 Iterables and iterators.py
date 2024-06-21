import itertools

def probability_of_letter_a(n, letters, k):
    total_combinations = 0
    combinations_with_a = 0
    
    # Generate all combinations of indices of length k
    index_combinations = itertools.combinations(range(n), k)
    
    for indices in index_combinations:
        total_combinations += 1
        contains_a = False
        for index in indices:
            if letters[index] == 'a':
                contains_a = True
                break
        if contains_a:
            combinations_with_a += 1
    
    # Calculate probability
    probability = combinations_with_a / total_combinations
    
    return probability

# Reading input
n = int(input().strip())  # length of the list
letters = input().strip().split()  # list of letters
k = int(input().strip())  # number of indices to select

# Calculate probability
result = probability_of_letter_a(n, letters, k)

# Print result formatted to 4 decimal places
print(f"{result:.4f}")
