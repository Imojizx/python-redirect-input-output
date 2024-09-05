import sys
fout=open("input.txt",'rt')
sys.stdin=fout
fout=open("output.txt",'wt')
sys.stdout=fout
while True:
    numbers=input("~>").strip().split(" ")
    if numbers[0]=="add":
        print(int(numbers[1])+int(numbers[2]))
    if numbers[0]=="mul":
        print(int(numbers[1])*int(numbers[2]))
    if numbers[0]=="div":
        print(int(numbers[1])/int(numbers[2]))
    if numbers[0]=="min":
        print(int(numbers[1])-int(numbers[2]))
        