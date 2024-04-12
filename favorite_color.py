ranking = {}
answer = None

while answer != "":
    answer = input("Enter your favorite color: \n")
    
    # if answer is not empty
    if answer:
        if answer in ranking:
            ranking[answer] += 1
        else:
            ranking[answer] = 1

print(f"Here are the favorite users' colors : ")

# sorts values in descending order
sorted_dico = sorted(ranking.items(), key=lambda x:x[1], reverse=True)
conv_dico = dict(sorted_dico)

for key, value in conv_dico.items():
    print(key, ":", value, "vote(s)")
