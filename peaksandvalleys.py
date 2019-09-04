#filename: peaksandvalleys.py

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def findPeaks(data):
    peaks = []
    
    for i in range(1, len(data)-1):

        if data[i-1] < data[i] > data[i+1]:
            peaks.append(i)

    
    return peaks
    

def findValleys(data):
    valleys = []

    for i in range(1, len(data)-1):
        if data[i-1] > data[i] < data[i+1]:
            valleys.append(i)

        

    return valleys

def peakValley(peaks,valleys):
    peaksAndValleys = []
    
    for i in range(len(peaks)):
        peaksAndValleys.append(peaks[i])
    for i in range(len(valleys)):
        peaksAndValleys.append(valleys[i])
         
    peaksAndValleys.sort()
    return peaksAndValleys

def drawMap(data):
    for i in range(9,0,-1):
        rowlist = []
        for el in range(len(data)):
            if data[el] >= i:
                rowlist.append('X')
            else:
                rowlist.append(' ')
        print(' '.join(rowlist))      

print(peakValley(findPeaks(data),findValleys(data)))
drawMap(data)



