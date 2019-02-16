import utilities as util
import numpy as np

class App:
    # Global attributes
    MAX_TEMPO = 140
    MIN_TEMPO = 60
    
    MIN_BEAT_PERIOD = 1/MAX_TEMPO
    MAX_BEAT_PERIOD = 1/MIN_TEMPO

    SAMPLE_RATE = 44100
    SAMPLE_PERIOD = 1/SAMPLE_RATE

    WINDOW_SIZE = 1024
    FREQ_RESOLUTION = SAMPLE_RATE/WINDOW_SIZE
    FREQ_ANALYZE = [60, 500]
    FREQ_LOCAL_RANGE = 50

    HISTORY_SIZE = FREQ_RESOLUTION

    def __init__(self):
        self.signalPing = [0 for t in range(WINDOW_SIZE)]
        self.signalPong = [0 for t in range(WINDOW_SIZE)]
        self.inputSignal = self.signalPing
        self.processSignal = self.signalPong

        self.beatBuffer = np.zeroes((len(FREQ_ANALYZE), HISTORY_SIZE))
        self.sigFreqIndex = 0
        self.sigTimeIndex = 0
        
        self.currentTempo = 120

    def sampleWindow(self):
        # Background thread
        
        # Collect data
        for i in range(WINDOW_SIZE):
            self.inputSignal[i] = readMic()

        # Switch ping-pong buffer
        if self.inputSignal == self.signalPing:
            self.inputSignal = self.signalPong
            self.processSignal = self.signalPing
        else # self.inputSignal == self.signalPong
            self.inputSignal = self.signalPing
            self.processSignal = self.signalPong

    def processWindow(self):
        # Main thread

        # Extracts one time value worth of frequency data
        
        # FFT data
        self.processSignal = np.fft.fft(self.processSignal)
        self.logCompression(self.signal[self.sigEneryIndex])

        for fCount, fValue in enumerate(FREQ_ANALYZE):
            # Extract frequency band
            signalEnergy = sum(self.processSignal[fValue:fValue+FREQ_LOCAL_RANGE]) / FREQ_LOCAL_RANGE
            
            # Load new row with frequency band
            self.beatBuffer[self.sigTimeIndex] = signalEnergy

    def processData(self):
        # Main thread

        # Calcultates most prominent beat

    def getElmtFreq(self, index):
        return index*FREQ_RESOLUTION

    def getFreqElmt(self, freq):
        return int(freq/FREQ_RESOLUTION)

    def fftData(self):
        self.data = np.fft.fft(self.signal)

    def ifftData(self):
        self.data = np.fft.ifft(self.signal)

    def logCompression(self):
        for i in self.data:
            i = np.log(i)

    def processRange(self, start, size):
        pass

    def applyFilter(self):
        pass
