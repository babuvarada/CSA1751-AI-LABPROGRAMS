import itertools
def is_valid_solution(assignment, words, result):
    letter_to_digit = {letter: digit for letter, digit in zip(assignment[0], assignment[1])}
    def word_to_num(word):
        return int("".join(str(letter_to_digit[letter]) for letter in word))
    word_sum = sum(word_to_num(word) for word in words)
    return word_sum == word_to_num(result)
def solve_cryptarithmetic(words, result):
    letters = set("".join(words + [result]))
    if len(letters) > 10:
        print("Too many unique letters to solve.")
        return
    for perm in itertools.permutations(range(10), len(letters)):
        if is_valid_solution((letters, perm), words, result):
            solution = {letter: digit for letter, digit in zip(letters, perm)}
            print("Solution found:", solution)
            return solution
    print("No solution found.")
def main():
    words = ["SEND", "MORE"]
    result = "MONEY"
    solve_cryptarithmetic(words, result)
if __name__ == "__main__":
    main()
