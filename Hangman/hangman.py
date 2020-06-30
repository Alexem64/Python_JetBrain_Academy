# Write your code here
import random

game_name = ["H A N G M A N"]
solutions = 'python', 'java', 'kotlin', 'javascript'
solution = random.choice(solutions)
current_word = ['-' for letter in solution]
attempts = set()
errors = 0


def check_word(gue, sol):
    return gue == sol


def print_results(gue, sol):
    print("You survived!") if check_word(gue, sol) else print("You are hanged!")


def print_current_word(cur_word):
    print(''.join(cur_word))


def check_letter(guess_lttr, sol, cur_word):
    if guess_lttr not in sol:
        print("No such letter in the word")
        return False
    cur_ind = 0
    for i in range(0, sol.count(guess_lttr)):
        if i == 0:
            cur_ind = sol.find(guess_lttr, cur_ind)
            cur_word[cur_ind] = guess_lttr
        else:
            cur_ind = sol.find(guess_lttr, cur_ind+1)
            cur_word[cur_ind] = guess_lttr
    return True


def precheck_letter(guess_lttr, cur_word):
    if len(guess_lttr) != 1:
        print("You should input a single letter")
        return False
    if not guess_lttr.islower() or not ord(guess_lttr) < 128:
        print("It is not an ASCII lowercase letter")
        return False
    if guess_lttr in cur_word or guess_lttr in attempts:
        print("You already typed this letter")
        return False
    return True

print(game_name)
decision = ""
while decision != "exit":
    decision = input('Type "play" to play the game, "exit" to quit: ')
    if decision == "play":
        while errors < 8 and not check_word(''.join(current_word), solution):
            print()
            print_current_word(current_word)
            guess_letter = input('Input a letter: ')
            if precheck_letter(guess_letter, current_word):
                if not check_letter(guess_letter, solution, current_word):
                    attempts.add(guess_letter)
                    errors += 1
        if errors == 8:
            print("You are hanged!")
            print()
        else:
            print(f"""You guessed the word {solution}!
        You survived!""")
            print()