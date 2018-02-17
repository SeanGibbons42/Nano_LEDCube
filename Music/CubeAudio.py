import pyaudio
import numpy as np
class CubeAudio(object):
    def __init__(self,chunksize=2**10,rate=16000,trim=20):

        self.RATE = rate
        self.CHUNK = chunksize
        self.TRIM = trim

        self.p = pyaudio.PyAudio() # start pyaudio
        self.stream = self.p.open(format=pyaudio.paInt32,channels=1,rate=self.RATE,input=True,frames_per_buffer=self.CHUNK) #Startup a stream of pyaudio that reads 32 bit ints

        self.maxf = self.RATE/2 #maximum frequency calculated by the fourier transform
        self.fstep = self.maxf/self.CHUNK #step in the x axis
        self.minf = self.fstep*self.TRIM # lowest frequency that will be shown on the plot

        self.window = np.hanning(self.CHUNK) # calculate a hanning function for smoothing


    ##################################
    #SETTERS
    def setrate(self,rate):
        self.RATE = rate
        self.stream=self.p.open(format=pyaudio.paInt32,channels=1,rate=self.RATE,input=True,frames_per_buffer=self.CHUNK) #Startup a stream of pyaudio that reads 32 bit ints
        self.maxf = self.RATE/2 #maximum frequency calculated by the fourier transform
        self.fstep = self.maxf/self.CHUNK #step in the x axis
        self.minf = self.fstep*self.TRIM # lowest frequency that will be shown on the plot

    def setchunksize(self,chunksize):
        self.CHUNK = chunksize
        self.stream=self.p.open(format=pyaudio.paInt32,channels=1,rate=self.RATE,input=True,frames_per_buffer=self.CHUNK) #Startup a stream of pyaudio that reads 32 bit ints
        self.maxf = self.RATE/2 #maximum frequency calculated by the fourier transform
        self.fstep = self.maxf/self.CHUNK #step in the x axis
        self.minf = self.fstep*self.TRIM # lowest frequency that will be shown on the plot
        self.window = np.hanning(self.CHUNK) # calculate a hanning function for smoothing

    def settrim(self,trim):
        self.TRIM = trim
        self.stream=self.p.open(format=pyaudio.paInt32,channels=1,rate=self.RATE,input=True,frames_per_buffer=self.CHUNK) #Startup a stream of pyaudio that reads 32 bit ints
        self.maxf = self.RATE/2 #maximum frequency calculated by the fourier transform
        self.fstep = self.maxf/self.CHUNK #step in the x axis
        self.minf = self.fstep*self.TRIM # lowest frequency that will be shown on the plot

    def setstream(self,newstream):
        self.stream = newstream



    ###################################
    #GETTERS
    def getrate(self):
        return self.RATE

    def getchunksize(self):
        return self.CHUNK

    def gettrim(self):
        return self.TRIM

    def getstream(self):
        return self.stream


    ###################################
    #Other Functions

    def readfourier(self):
        '''Reads a CHUNK of data from the pyaudio stream then performs a fourier transform and returns that array trimmed at low frequency by TRIM points'''

        ydata = np.fromstring(self.stream.read(self.CHUNK),dtype=np.int32) #Read one CHUNK from the stream
        #Detrend data, this was suggested on the internet. Moves the wave so it is centered at 0
        data = ydata - np.mean(ydata)
        #Apply a window Function, apparently this makes your data better
        data = data*self.window

        ytransform = np.abs(np.fft.rfft(data)) #do a real fourier transform on the data

        return ytransform[self.TRIM:]

    def readrawdata(self):
        data = np.fromstring(self.stream.read(self.CHUNK),dtype=np.int32)
        return data

    def xvalues(self):
        '''gives an array of x values (frequency values) that match readfourier for plotting purposes'''
        x = np.linspace(self.minf,self.maxf,(self.CHUNK/2)-self.TRIM+1) # x axis based on sampling rate, chunk size, and TRIM

        return x

    def shutdown(self):
        # Closes out pyaudio

        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
