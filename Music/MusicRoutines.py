import sys
sys.path.append("..\\")
from LEDCube import LEDCube
from Music.CubeAudio import CubeAudio
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import threading

def FreqCube(cube,n,runtime):
    CHUNK=2**10
    RATE=16000
    TRIM=20
    chunks = cube.discretizeCube(n) #get an array of nxn chunks
    print(chunks)
    c = CubeAudio(chunksize=CHUNK,rate=RATE,trim=TRIM) #Create an instance of CubeAudio named c

    # An amplitude of 10**maxavg or higher will correspond to a max height on the cube.
    # An amplitude of 10**minavg or lower will correspond to 0 height on the cube
    maxavg = 10
    minavg = 8.5

    vdiv = cube.getDimensions()[2] #the height of the cube

    vstep = (maxavg-minavg)/vdiv #break up the area between the minimum and maximum averages into h chunks

    datalength  = len(c.xvalues()) # the length of the farrays

    detrend = [(1/datalength)*i for i in range(datalength)]

    for t in range(runtime):

        farray = np.log10(c.readfourier()) #read an array of fourier transform data and take the log base 10 of it

        farray = farray + detrend #add the line to the data to compensate for lower amplitudes at high frequency

        xstep = int(len(farray)/len(chunks)) #xstep is the size of a subarray.

        chunkz = [] # array into which we will store the z values

        for i in range(len(chunks)):

            subarray = farray[i*xstep:(i+1)*xstep] #create a subarray of length xstep that starts at xstep*i
            avg = np.mean(subarray) #find the average value of the subarray


            z = int(((avg-minavg)*vdiv)/(maxavg-minavg)) #find the z value. Will be = height when avg = maxavg and 0 when avg = minavg
            if (z<0):
                z = 0
            elif (z>vdiv):
                z = vdiv

            chunkz.append(z)

        #clear the cube before we send data
        #Function clearAll: turns off every LED in the cube
        for x in range(cube.getBounds()[5],cube.getBounds()[4]+1):
            for y in range(cube.getBounds()[3],cube.getBounds()[2]+1):
                for z in range(cube.getBounds()[1],cube.getBounds()[0]+1):
                    cube.setPixel([x,y,z],0);

        for i in range(len(chunks)):
            cube.LightColumn(chunks[i],chunkz[i]) #light up our collumns defined by the chunks array to heights stored in chunkz

        #send the data and wait about 1/60 of a second
        cube.sendStream()
        time.sleep((1/30))

def Graphsim(cube):

    n = 2

    CHUNK = 2**10 # we read chunks of 1024 points
    RATE = 16000 # we sample at RATE Hz
    TRIM = 20 #how many low frequency points we want to cut off (tend to have very large noise for unknown reason)

    chunks = cube.discretizeCube(n) #get an array of nxn chunks

    c = CubeAudio(chunksize=CHUNK,rate=RATE,trim=TRIM) #Create an instance of CubeAudio named c
    maxavg = 10
    minavg = 8.3
    # these two will be overwritten shortly

    vdiv = cube.getDimensions()[2] #the height of the cube

    # Matplotlib Housekeeping
    fig = plt.figure() #Create a matplotlib figure
    ax1 = fig.add_subplot(1,1,1) # add a subplot that we can animate (Constantly Update)

    x = np.arange(0,10*len(chunks))


    def animate(i):
        ydata = []

        farray = np.log10(c.readfourier()) #read an array of fourier data and take the log base 10 of it


        #calculate a line that fits the slope of the data. Without this low F is higher amplitude than high F
        detrend = [(1/len(farray))*i for i in range(len(farray))]

        farray = farray + detrend

        vstep = (maxavg-minavg)/vdiv #break up the area between the minimum and maximum averages into h chunks

        xstep = int(len(farray)/len(chunks)) #xstep is the size of a subarray. We will make


        for i in range(len(chunks)):

            subarray = farray[i*xstep:(i+1)*xstep] #create a subarray of length xstep that starts at xstep*i
            avg = np.mean(subarray) #find the average value of the subarray


            z = int(((avg-minavg)*vdiv)/(maxavg-minavg)) #find the z value. Will be = height when avg = maxavg and 0 when avg = minavg

            if (z<0):
                z = 0

            for j in range(10):
                ydata.append(z)

        ax1.clear()
        ax1.set_ylim([0,vdiv])
        ax1.plot(x,ydata)

    ani = animation.FuncAnimation(fig,animate,interval=1) # run our animation with pauses of length interval
    plt.show() # make the window visible

def fouriergraph():
    fig = plt.figure() #Create a matplotlib figure
    ax1 = fig.add_subplot(1,1,1) # add a subplot that we can animate (Constantly Update)

    f = CubeAudio() # start a cubeaudio instance

    x = f.xvalues()   #get the x axis for the plot

    def animate(i):
        y = f.readfourier() # pull some y values
        #reset the plot then plot again
        ax1.clear()
        ax1.set_ylim([0,10**10.5])
        ax1.plot(x,y)

    ani = animation.FuncAnimation(fig,animate,interval=1000/60) # run our animation with pauses of length interval
    plt.show()

def FreqCube_WGraph(cube,n,runtime):

    cubethread = threading.Thread(target = FreqCube, args=(cube,n,runtime))
    cubethread.start()
    fouriergraph()
