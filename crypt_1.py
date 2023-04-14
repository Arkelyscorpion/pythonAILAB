import itertools

def get_value(word, substitution):
    s = 0
    factor = 1
    for letter in reversed(word):
        s += factor * substitution[letter]
        factor *= 10
    return s

def solve_puzzle(equation):
    solvable = False
    left, right = equation.upper().replace(' ', '').split('=')
    left = left.split('+')
    letters = set(right)
    for word in left:
        for letter in word:
            letters.add(letter)
    letters = list(letters)
    digits = range(10)
    for perm in itertools.permutations(digits, len(letters)):
        sol = dict(zip(letters, perm))
        if sum(get_value(word, sol) for word in left) == get_value(right, sol):
            solvable = True
            print(' + '.join(str(get_value(word, sol)) for word in left) +
                  " = {} (mapping: {})".format(get_value(right, sol), sol))
    if not solvable:
        print("No solution")


string = str(input("Enter the Cryptarithmetic Equation: "))
solve_puzzle(string)
