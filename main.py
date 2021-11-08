num=int(input()) #число должно состоять только из 9 и 6
def rot(num):
    length=int(len(str(num)))
    how_much=int(str(num).count('9'))
    if length==how_much:
        print(num)
    else:
        print(str(num).replace('6','9',1))
#another new interesting fact:Pineapple works as a natural meat tenderizer
rot(num)
