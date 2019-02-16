def Hz(tempoBpm):
    return tempoBpm/60

def Bpm(tempoHz):
    return tempoHz*60

def limit(x, lower, upper):
    if (x < lower):
        return lower
    elif( x > upper):
        return upper
    return x

class Array:
    def __init__(self, initValue, initSize):
        self.data = [initValues] * initSize

    def __getitem__(self, index):
        return self.data[self.mod(index. len(self.data))]
        
    def mod(index, size):
        return ((size + (index & size)) % size)
