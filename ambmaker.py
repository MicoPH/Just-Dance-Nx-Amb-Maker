import os
import struct
print('Just Dance Nx Amb Maker Made By MicoPH')

try:
    os.mkdir('input//tempwav/')
except:
    pass
for audiofilename in os.listdir("input//"):
    if(".wav" in audiofilename):
        os.system('ffmpeg -i input//' + audiofilename +  '  -f wav -bitexact -acodec pcm_s16le -ar 48000 -ac 2 -loglevel quiet input//tempwav//temp.wav')
    if(os.path.isfile("input//tempwav/temp.wav")):
        with open("input//tempwav/temp.wav", "rb") as f:
            print('Encoding... '+ audiofilename +'.ckd')
            f.read(43)
            filesize = (os.path.getsize("input/tempwav/temp.wav") - 72).to_bytes(3, byteorder="little")
            rakiheader = b'\x52\x41\x4B\x49\x0B\x00\x00\x00\x4E\x78\x20\x20\x70\x63\x6D\x20\x48\x00\x00\x00\x48\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x66\x6D\x74\x20\x38\x00\x00\x00\x10\x00\x00\x00\x64\x61\x74\x61\x48\x00\x00\x00'
            rakiheader1 = b'\x00\x01\x00\x02\x00\x80\xBB\x00\x00\x00\xEE\x02\x00\x04\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            rakiend = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            audiofile = f.read()
        os.remove("input/tempwav/temp.wav")
        os.rmdir("input//tempwav")

        denc = open("output//" + audiofilename + ".ckd", "wb")
        denc.write(rakiheader)
        denc.write(filesize)
        denc.write(rakiheader1)
        denc.write(rakiend)
        denc.write(audiofile)
        print("DONE: " + audiofilename + ".ckd")
