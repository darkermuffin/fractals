from random import randrange, uniform
import math


xns = -1.5
xps = 1.5
yns = -1.5
yps = 1.5

maxi = 1000

r_parr = [[0]*1000 for _ in range(1000)]
g_parr = [[0]*1000 for _ in range(1000)]
b_parr = [[0]*1000 for _ in range(1000)]

iMax = 1000
jMax = 1000
pickpix = 0

def mapval(n, start1, stop1, start2, stop2): 
  return ((n-start1)/(stop1-start1))*(stop2-start2)+start2


while(1): 
    bailout = 0

    #picking randomly from a global scale 
    a = uniform(-2,2);
    b = uniform(-2,2);

    a_ = a
    b_ = b

    n_iter = 0
    #Iterator Variables
    n = 0

    ca = -0.4
    cb = 0.6
    
    #Iterator for till max iterations
    while (n < maxi): 
        Zaa = a_ * a_ - b_ * b_
        Zbb = 2 * a_ * b_
        a_ = Zaa + ca
        b_ = Zbb + cb

        if ((a_ * a_ + b_ * b_) > 16):
            n_iter = n
            bailout = 1
            break
        n=n+1
    
    
    #if bailout recalculate the Z values at c and then color those values depending upon the max_iter
    if (bailout and n_iter > 10):
        a_ = a
        b_ = b

        n = 0

        ca = -0.4
        cb = 0.6
        Zaa = 0
        Zbb = 0

        while (n < maxi): 
            #Calculating z^2
            Zaa = a_ * a_ - b_ * b_
            Zbb = 2 * a_ * b_
            #z^2 + c where c is (a,b)
            a_ = Zaa + ca
            b_ = Zbb + cb
            #mapping points to pixel scale
            m = math.floor(mapval(a_, xns, xps, 0, iMax))
            n = math.floor(mapval(b_, yns, yps, 0, jMax))

            if ((a_ * a_ + b_ * b_) > 16): 
                break

            

            if (m < iMax and n < jMax and m > 0 and n > 0):
                #print str(m)+' '+str(n)
                m = int(m)
                n = int(n)
               #600-650
                if(n_iter < 100):
                    #register in blue 
                    b_parr[m][n] += 1

                #650-750
                if(n_iter > 100 and n_iter < 400):
                    g_parr[m][n] += 1
                #750-1000
                if(n_iter > 400 and n_iter < 1000):
                    r_parr[m][n] += 1

            n = n+1

        
    pickpix = pickpix +1

    if (pickpix % 10000000 == 0):
        print('parr '+ str(pickpix))

        f = open('rjuliaBuddha.txt', 'w')
        for item in r_parr:
            f.write("%s,"%item)
        f.close()

        f = open('gjuliaBuddha.txt', 'w')
        for item in g_parr:
            f.write("%s,"%item)
        f.close()

        f = open('bjuliaBuddha.txt', 'w')
        for item in b_parr:
            f.write("%s,"%item)
        f.close()

    
        
    
