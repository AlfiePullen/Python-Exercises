def list_filter(number_list):
    blank_list = [] #Blank list to add all the desired results
    for i in number_list:
        if i%5==0:#Using % we can find the remainder of a number
            blank_list.append(i)
    return blank_list
