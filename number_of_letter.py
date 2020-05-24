word = input("Enter a sentences:")
cnt_of_let = {}
for i in word:
    if i not in cnt_of_let:
        cnt_of_let[i] = 1
    else:
        cnt_of_let[i] += 1
print(cnt_of_let)
