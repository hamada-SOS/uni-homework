import numpy as np

init = True
first = "first"
second = "Second"
# setting thenumbers of matrix
while init:

    N_matrix = int(input("Enter number of matrices: "))
    count = 1    
    on = True


# taking the input form the user

    while count <= 2:
        print(f'enter the info of the {first if count < 2 else second} matrix. ')
        N_rows = int(input("Enter number of rows: "))
        N_columns = int(input("Enter number of columns: "))
        while on:
            matrix_X =np.zeros((N_rows,N_columns), dtype=int) 
            on = False
        matrix_Y =np.zeros((N_rows,N_columns), dtype=int)
        if count == 1:
            len_rows = len(matrix_X)
        elif count == 2:
            len_rows = len(matrix_Y)


# Sorting the inputs into 2D List

        # the first for loop creates the rows
        for i in range(len_rows):
        # the second row creates the columns
            for j in range(len(matrix_X[i] if count == 1 else matrix_Y[i])):
                try:
                    x = int(input('enter ELEment: '))
                except ValueError:
                    print("You missed the input bye")
                    break
                if (count == 2 ):
                    matrix_Y[i][j] = x
                else:
                    matrix_X[i][j] = x
        if N_matrix == 1:
            count += 2
        elif N_matrix == 2:
            count += 1


# dislying the matrix before the calculation

    if N_matrix == 2:
        print(matrix_X)
        print(matrix_Y)
    elif N_matrix == 1:
        print(matrix_X)


#performig the calculation and and displing the new matrix

    OP = int(input("What op you want to perform?\n1-Addtion.\n2-Subtraction.\n3-Multipication.\n4-Scaller Multipliation.\n5-Transpose.\n"))
    if OP == 1:
        try:
            print(np.add(matrix_X, matrix_Y))
        except ValueError:
            print("dimensions of matrices are not the same")
    elif OP == 2:
        try:
            print(np.subtract(matrix_X, matrix_Y))
        except ValueError:
            print("dimensions of matrices are not the same")
    elif OP == 3:
        try:
            print(np.matmul(matrix_X, matrix_Y))
        except ValueError:
            print("there is a mismatch of the core dimensions(rows)")
    elif OP == 4:
        try:
            multiplyer = int(input("Enter the element:"))
            print(multiplyer*matrix_X)
        except ValueError or NameError:
            print("Enter a valid input ")
    elif OP == 5:
        if N_matrix == 2:
            print("the opreation can performed only one matrix at time")
            pass
        print(np.transpose(matrix_X))


# asking the user to redo the opreation

    try:
        closing = int(input("\nDo you want to perform another calculation?\n1-yes\n2-no\n"))
        if closing == 2:
            init = False
        elif closing == 1:
            init == True
    except ValueError:
            print("Entered invalid input")