file = open("dialogs.txt", "r")


conversations = []
for line in file.readlines():
    conversations.append(line.split("\n"))


cases = []
for i in range(len(conversations)):
    for j in range(len(conversations[i])):
        temp = conversations[i][j].split("\t")
        print(temp)

print(cases)
