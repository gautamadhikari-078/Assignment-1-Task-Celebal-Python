from itertools import groupby

def compress_string(s):

    groups = [(len(list(group)), key) for key, group in groupby(s)]
    

    result = " ".join(f"({count}, {digit})" for count, digit in groups)
    
    return result


input_string = input().strip()


print(compress_string(input_string))
