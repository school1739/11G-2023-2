zad_anie = open("24-2.txt", "r")
with open("24-1.txt") as zad_anie:
    stroka = zad_anie.read()
zad_anie.close()

string = stroka
l = []
otvet = []
string = string.split("A")
for i in string:
  if i == '' or i == " " or i == "" or i == ' ':
     string.remove(i)



for i in range(len(string)- 1550):
  l.append(string[i][0])

print(l)