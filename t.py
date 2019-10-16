from random import randint

A = [list([0] * 4) for i in range(4)]
for i in range(4):
    for j in range(4):
        A[i][j] = i * 4 + (j + 1)

def swap(xS, yS, xE, yE):
    t = A[xS][yS]
    A[xS][yS] = A[xE][yE]
    A[xE][yE] = t

def shuf():
    cX = 3
    cY = 3
    for i in range(200):
        mX = randint(-1,1)
        mY = randint(-1,1)
                  
        if cX >= 3:
            mX = randint(-1,0)
        if cX <= 0:
            mX = randint(0, 1)

        
        if cY >= 3:
            mY = randint(-1, 0)
        if cY <= 0:
            mY = randint(0, 1)
        
        swap(cX + mX, cY + mY, cX, cY)
        cX += mX
        cY += mY

print(A)
shuf()
print(A)
        