def is_magic_square(magic_square):
   magic_rows = False;
   magic_columns = False
   magic_diag = False
   
   x = 0
   y = 2
   
   sum3 = 0
   sum4 = 0
   for i in range(3):
       sum1 = 0
       sum2 = 0
       sum3 += magic_square[i][x]
       sum4 += magic_square[i][y]
       x += 1
       y -= 1
       if sum3 == 15:
           magic_diag = True
       else: magic_diag = False
       for j in range(3):
           sum1 += magic_square[i][j]
           sum2 += magic_square[j][i]
       if sum1 == 15:
           magic_rows = True
       else: magic_rows = False
       if sum2 == 15:
           magic_columns = True
       else: magic_columns = False
       print(magic_rows, sum1, magic_columns, sum2, magic_diag, sum3)
   
   if(magic_columns and magic_rows and magic_diag):
       return True
   else: return False
   
   
magic_square = [[4, 9, 2],[3, 5, 7],[8, 1, 6]]
   
if (is_magic_square(magic_square)):
    print("true")
else: print("false")