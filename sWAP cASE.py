def swap_case(s):
    result = '';
    for char in s:
        if(char.isupper()==True):
            result = result + (char.lower());
        elif(char.islower()==True):
            result = result + (char.upper());
        else:
            result = result + char;
    return result;

if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result
