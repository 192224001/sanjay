def lexo(my_string):
    words =my_string.split()
    words.sort()
    for i in words:
        print( i )
if __name__=='__main__':
    my_string = "my name is joyce mary"\
    " i am studying python"
lexo(my_string)
