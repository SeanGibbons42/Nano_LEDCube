#from LEDCube import LEDCube
import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

CHUNK = 2**10 # we read chunks of 1024 points
RATE = 16000 # we sample at RATE Hz
TRIM = 20 #how many low frequency points we want to cut off (tend to have very large noise for unknown reason)


p=pyaudio.PyAudio() # start pyaudio
stream=p.open(format=pyaudio.paInt32,channels=1,rate=RATE,input=True,frames_per_buffer=CHUNK) #Startup a stream of pyaudio that reads 32 bit ints

# Matplotlib Housekeeping
fig = plt.figure() #Create a matplotlib figure
ax1 = fig.add_subplot(1,1,1) # add a subplot that we can animate (Constantly Update)

maxf = RATE/2 #maximum frequency calculated by the fourier transform
fstep = maxf/CHUNK #step in the x axis
minf = fstep*TRIM # lowest frequency that will be shown on the plot

x = np.linspace(minf,maxf,(CHUNK/2)-TRIM+1) #precalculate the x axis based on sampling rate, chunk size, and TRIM

window = np.hanning(CHUNK) # calculate a hanning function for smoothing

detrend = [(1/len(x))*i for i in range(len(x))]

def animate(i):
    ydata = np.fromstring(stream.read(CHUNK),dtype=np.int32) #Read one CHUNK from the stream
    #Detrend data, this was suggested on the internet. Moves the wave so it is centered at 0
    data = ydata - np.mean(ydata)
    #Apply a window Function, apparently this makes your data better
    data = data*window

    ytransform = np.abs(np.fft.rfft(data)) #do a real fourier transform on the data
    #x = np.linspace(minf,maxf,len(ytransform[TRIM:]))

    ###LOG PLOT###
    #logdata = np.log10(ytransform[TRIM:])
    #detrenddata = logdata + detrend

    ax1.clear()
    ax1.set_ylim([0,10**10])
    ax1.plot(x,ytransform[TRIM:]) # plot it (we dont include the first element of ytransform because it is just an offset, not real data)


ani = animation.FuncAnimation(fig,animate,interval=10) # run our animation with pauses of length interval
plt.show() # make the window visible

#Close out the program
stream.stop_stream()
stream.close()
p.terminate()
