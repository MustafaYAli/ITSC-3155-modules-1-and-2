upper_case = ""
lower_case = ""

word = input("Enter a word: ")


for i in word:
    if i.isupper():
        upper_case += i
    elif i.islower():
        lower_case += i

result = lower_case + upper_case

print(result)
