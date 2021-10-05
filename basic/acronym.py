user_input = str(input("Enter a Phrase: "))
text = list(user_input)
a = ""
print(text)
for i in reversed(text):
    a = a+str(i[0]).upper()
print(a)