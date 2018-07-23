import random
class Matrix():
    def __init__(self,name):
        self.name = name
        self.row = int(input("Enter {} matrix's rows:".format(name)))
        self.col = int(input("Enter {} matrix's cols:".format(name)))

    def Show(self):
        print("Matrix {}({}, {}):".format(self.name,self.row,self.col))
        self.mat = []
        for i in range(self.row):
            tmp_row = []
            for j in range(self.col):
                num = random.randint(0,9)
                tmp_row.append(num)
            self.mat.append(tmp_row)
        self.Print(self.mat)
    def Print(self,mat):
        for i in range(self.row):
            for j in range(self.col):
                print(mat[i][j],end=' ')
            print('\n',end='')
    def check_size(self,B):
        if self.row != B.row or self.col != B.col:
            print("Matrix's size must be the same size") 
            return False
        else:
            return True
    def check_size_mult(self,B):
        if self.col == B.row:
            return True
        else:
            print("Matrix's size are illegal") 
            return False
    def Add(self,B):
        print("======A+B======")
        if self.check_size(B):    
            for i in range(self.row):
                for j in range(self.col):
                    print(self.mat[i][j]+B.mat[i][j],end=' ')
                print('\n',end='')
    def minus(self,B):
        print("======A-B======")
        if self.check_size(B):    
            for i in range(self.row):
                for j in range(self.col):
                    print(self.mat[i][j]-B.mat[i][j],end=' ')
                print('\n',end='')

    def Mult(self,B):
        if self.check_size_mult(B):
            print("======A*B======")
            out = []
            for i in range(self.row):
                tmp_row = []
                for j in range(B.col):
                    # sum of the matirx element multiply
                    num = 0
                    for idx in range(self.col):
                        num += self.mat[i][idx]*B.mat[idx][j]
                    tmp_row.append(num)
                out.append(tmp_row)
            self.Print(out)
        else:
            return None
    def Trans(self,B):
        if self.check_size_mult(B):
            print("=====the transporse of A*B=====")
            out = []
            for i in range(self.row):
                tmp_row = []
                for j in range(B.col):
                    # sum of the matirx element multiply
                    num = 0
                    for idx in range(self.col):
                        num += self.mat[i][idx]*B.mat[idx][j]
                    tmp_row.append(num)
                out.append(tmp_row)
            self.Print(list(map(list, zip(*out))))


        else:
            return None

A = Matrix('A')
A.Show()
B = Matrix('B')
B.Show()
A.Add(B)
A.minus(B)
A.Mult(B)
A.Trans(B)

        