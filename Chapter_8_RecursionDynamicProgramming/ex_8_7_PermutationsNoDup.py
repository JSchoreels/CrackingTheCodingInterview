def permutation(string : str):
    if len(string) == 1:
        return [string]
    else:
        first_char = string[0]
        rest = string[1:]
        rec_permutation = permutation(rest)
        result = set() # The set will allow dups to be filtered automatically
        for perm in rec_permutation:
            for i in range(len(perm)+1):
                new_perm = perm[:i] + first_char + perm[i:]
                result.add(new_perm)
        return result

print(permutation("abcd"))