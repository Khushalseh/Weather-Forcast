import string
import math
import random  

def calculate_entropy(password):
    character_set_size = sum([1 for c in string.printable if c in password])
    entropy = math.log2(character_set_size) * len(password)
    return entropy

def suggest_strong_password():
    suggestion = ''.join([
        string.ascii_uppercase,
        string.ascii_lowercase,
        string.digits,
        string.punctuation
    ])
    return ''.join(random.sample(suggestion, k=16))

password = input("Enter password: ")
upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
special = any([1 if c in string.punctuation else 0 for c in password])
digits = any([1 if c in string.digits else 0 for c in password])

characters = [upper_case, lower_case, special, digits]

score = 0

with open("C:\\Users\\ninja\\Desktop\\10-million-password-list.txt", 'r') as f:
    common = f.read().splitlines()

if password.lower() in common:
    print("Password was found in a common list: 0/12")
    print("Suggestion for a stronger password:", suggest_strong_password())
    exit()
    
length = len(password)

if length > 20:
    score += 4
elif length >= 17:
    score += 3
elif length > 12:
    score += 2
elif length >= 8:
    score += 1

print(f"Password length is {str(length)}, adding {str(score)} points")

if sum(characters) > 3:
    score += sum(characters) - 3

print(f"Password has {str(sum(characters))} different character types, adding {str(sum(characters) - 3)} points")

if any(c.isdigit() for c in password) and any(c.isalpha() for c in password):
    score += 2
    print("Password contains both letters and digits, adding 2 points")

if any(c.isupper() for c in password) and any(c.islower() for c in password):
    score += 2
    print("Password contains both uppercase and lowercase letters, adding 2 points")

if any(c in string.punctuation for c in password):
    score += 2
    print("Password contains special characters, adding 2 points")

entropy = calculate_entropy(password)
print(f"Password entropy is {entropy:.2f}, adding {int(entropy/10)} points")

if score < 4:
    print(f"Password is weak! Score: {str(score)}/12")
    print("Suggestion for a stronger password:", suggest_strong_password())

elif 4 <= score < 8:
    print(f"Password is moderate! Score: {str(score)}/12")

elif 8 <= score < 12:
    print(f"Password is strong! Score: {str(score)}/12")

elif score >= 12:
    print(f"Password is very strong! Score: {str(score)}/12")