
import numpy as np
from utils import *
colours={'black':0,'blue':1,'red':2,'green':3,'yellow':4,'gray':5,'pink':6,'orange':7,'light-blue':8,'maroon':9}

def solve_4(pattern): #solve given a pattern
    # @param pattern --> matrix
    # @returns matrix
    new=np.zeros_like(pattern)
    new[0:6,]=pattern
    new[6:,0:3]=pattern[2:5,:]
    return new

def generate_4(): #generate a new pattern and the answer
    c=np.random.randint(0,len(list(colours.keys()))-1)
    canvas = np.zeros((np.random.randint(8,20), np.random.randint(8,20)))
    canvas=draw_shape(canvas)
    canvas[canvas==1]=c
    return canvas



"""m1=generate_4()
m2=solve_4(m1)
display(m1,m2)"""