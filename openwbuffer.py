inputFile = open ('myimage.jpeg', 'rb')
outputFile = open ('myoutputimage.jpeg', 'wb')

msg = inputFile.read(10)

while len(msg):
    outputFile.write(msg)
    msg = inputFile.read(10)

inputFile.close()
outputFile.close()
