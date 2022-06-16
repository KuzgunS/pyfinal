

# secret_word= "zulul"
#
#
# guess = ""
#
# while secret_word != guess :
#     guess = input("Enter your guess: ")
#     if secret_word != guess :
#         print("Guess again")
#     else:
#         print("You got it ! The secret word was: " + guess)
#         break

# ya da doğruyu bulmadan while çıkamayacağı için direkt
# while doğruyu bulup çıkınca you win yazılabilirdi.


secret_word= "zulul"

guess = ""
guess_count=1
num_of_tries=5

print("You have " + str(num_of_tries) + " number of tries")

while secret_word != guess :
    guess = input("Enter your guess: ")
    if secret_word != guess:
        guess_count += 1
        if guess_count > num_of_tries:
            print("You are out of guesses, game over.")
            break
        print("Guess again, you've left " + str(num_of_tries-guess_count+1) + " tries")

    else:
        print("congrats, you won when you've already had " + str(num_of_tries-guess_count+1) + " number of tries!")

# ya da videodaki, daha sade görünen yöntem

secret_word= "zulul"

guess = ""
guess_count=1
num_of_tries=5
out_of_guesses=False

while guess!=secret_word and not(out_of_guesses):
    if guess_count < num_of_tries:
        guess=input("Enter guess ")
        guess_count += 1
    else:
        out_of_guesses=True

if out_of_guesses:
    print("Out of guesses, game over")
else:
    print("You won!")











