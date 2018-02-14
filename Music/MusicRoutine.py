import sys
sys.path.append("..\\")
from LEDCube import LEDCube
from CubeAudio import CubeAudio
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def discretizeCube(cube,n):
    # Create nxn chunks in the XY plane of the cube
    '''returns a list of squares. squares are lists of x,y points'''

    dims = cube.getDimensions
    xmax,xmin,ymax,ymin,zax,zmin = cube.getBounds()

    CHUNKS = [] # The array that we will use to store the nxn CHUNKS
    # A Chunk will be stored as a n length array of tuples of (x,y) points in the cube
    # Z values are not stored in the CHUNKs and need to be assigned later

    # makechunk takes in a starting x and y position and returns a all the points in a square with corners (x,y) and (x+n-1,y+n-1)
    def makechunk(x,y,n):
        c = []
        for i in range(n):
            for j in range(n):
                c.append((x+i,y+j))
        return c


    # We iterate the starting x and y points for makechunk starting at the minimums and going to the maximums in steps of size n
    for x in range(xmin,xmax,n):
        for y in range(ymin,ymax,n):
            CHUNKS.append(makechunk(x,y,n))

    return CHUNKS


def LightCollumn(cube,square,z):
    '''Square needs to be a list of x,y points. Z is just a number'''

    for point in square:
        j = 0
        x = point[0] #extract the x value
        y = point[1] #extract the y value
        while (j<z):
            setPixel((x,y,j),1)
            j+=1


def FreqCube(cube,n,runtime,CHUNK=2**10,RATE=16000,TRIM=20):
    chunks = cube.discretizeCube(n) #get an array of nxn chunks

    c = CubeAudio(chunksize=CHUNK,rate=RATE,trim=TRIM) #Create an instance of CubeAudio named c

    # An amplitude of 10**maxavg or higher will correspond to a max height on the cube.
    # An amplitude of 10**minavg or lower will correspond to 0 height on the cube
    maxavg = 10
    minavg = 8.5

    vstep = (maxavg-minavg)/vdiv #break up the area between the minimum and maximum averages into h chunks

    vdiv = cube.getDimensions()[2] #the height of the cube

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
            print(z)

            chunkz.append(z)

        for i in range(len(chunks)):
            LightCollumn(cube,chunks[i],chunkz[i]) #light up our collumns defined by the chunks array to heights stored in chunkz


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

        x = np.arange(0,len(farray))

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

    ani = animation.FuncAnimation(fig,animate,interval=10) # run our animation with pauses of length interval
    plt.show() # make the window visible


cube = LEDCube([7,7,7])

Graphsim(cube)
