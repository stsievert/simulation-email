
from pylab import *
import time

N = 8
x = zeros((N,N))

x[0:N/2] = 1

figure()
imshow(x)

savefig('/Users/scott/Developer/simulation-email/simulation.png')
#show()
