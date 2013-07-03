def loop_function(x,y):
    
    numbers=[i for i in range(0,x,y)]
    print (numbers)
    i+=y
    print('The numbers are:')
    for num in numbers:
        print(num)

