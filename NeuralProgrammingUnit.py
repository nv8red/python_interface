import time
import random

#global variables to store data about the network

weights = [0]*512
dataSize = 0
data = [0]*512
ins = 0
outs = 0
layers = 0

#parameters(i: number of inputs, o: number of outputs,
#           h: the number of hidden layers, 
#           a: an array containing the sizes of the hiudden layers)

def parameters(i, o, h, a):
    global ins
    global outs
    global weights
    global layers
    ins = i
    outs = o
    layers = h
    for x in range(0, ins*8):
        weights[x]=weight()
    for x in range(0, layers):   
        for i in range(0, a[x]*8):
            weights[64*(x+1)+i]=weight()
            
#loadData(fileName: the name of the file the data will be pulled from,
#         dsize: number of input-output pairs in the data
    
def loadData(fileName, dsize):
    global ins
    global outs
    global dataSize
    global data
    count1 = 0
    count2 = 0
    if ins==0:
        printf("define parameters")
        return
    dataSize = dsize
    lfile = open(fileName, 'r')
    for x in range(0, dataSize):
        count1 = 0
        count2 = 0
        while count1 < ins:
            data[x*16+count1] = lfile.read(1)
            count1+=1
        while count2 < outs:
            data[x*16+8+count2] = lfile.read(1)
            count2+=1
    data=randomList(data)
    
#writeAll: writes the weights and the data into the npu like this:
# writes a 1 for ready
# writes the weights in order, by node then by layer
# writes the number of input-output pairs
# writes the input-output pairs in a random order, ins-outs-ins-outs etc.
            
def writeAll():
    global weights
    global data
    global dataSize
    write(1)
    for i in range(0, 512):
        write(weights[i])
    write(dataSize)
    for i in range(0, dataSize*16):
        write(data[i])
    
# used to randomize the order of inputs and outputs
    
def randomList(a): 
    global dataSize
    index = 0
    b = [0]*512
    r = list(range(0, dataSize))
    random.shuffle(r)
    for i in range(0, dataSize): 
        for x in range(0, 16):
            b[16*i+x] = a[16*r[i]+x]
    return b

#returns a random weight between 1 and -1

def weight():
    return random.random()*2-1

#write function

def write(input):
    print(input)
    
    