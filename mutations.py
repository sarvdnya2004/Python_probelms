def mutate_string(string, position, character):
    li=list(string)
    li[position]=character
    return ''.join(li) 

if __name__ == '__main__':
    s = input("enter the name")
    i= int (input("enter the location to be changed"))
    c = input("enter the new character")
    s_new = mutate_string(s, i, c)
    print(s_new)