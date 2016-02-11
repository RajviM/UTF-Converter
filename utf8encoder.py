import binascii
import sys

f=open(sys.argv[1],"rb")
f1=open("utf8encoder_out.txt","wb")
def padhexa(s):
    return '0x' + s[2:].zfill(8)
try:
    byte = f.read(1)
    byte2 =f.read(1)
    i=0
    while byte != "":
        # Do stuff with byte.
        p = bytearray([byte,byte2])
        q = '0x'+binascii.hexlify(bytearray(p))


            ##q = padhexa(q)

        r = int(q,16)


        a = int('0x00000000',16)
        b= int('0x0000007F',16)
        c= int('0x00000080',16)
        d=int('0x000007FF',16)
        e=int('0x00000800',16)
        g=int('0x0000FFFF',16)



        if 1==1 :
            if a <= r <= b :
                value = bin(r) [2:]
                b1 = value [-7:].zfill(7)
                b1 = '0'+b1

                one = int(b1,2)

                f1.write(chr(one))



            if c <= r <= d :
                value = bin(r) [2:]
                b1 = value [-6:].zfill(6)
                b1 = '10'+b1
                b2 = value [:-6].zfill(5)
                b2 ='110'+b2

                one = int(b1,2)
                two = int (b2,2)

                f1.write(chr(two))
                f1.write(chr(one))
                

            if e <= r <= f :
                value = bin(r) [2:]
                b1 = value [-6:].zfill(6)
                b1 = '10'+b1
                b2 = value [-12:-6].zfill(6)
                b2 ='10'+b2
                b3 = value [:-12].zfill(4)
                b3 = '1110'+b3
                one = int(b1,2)
                two = int (b2,2)
                three = int(b3,2)
                f1.write(chr(three))
                f1.write(chr(two))
                f1.write(chr(one))




       
        byte = f.read(1)
        byte2 = f.read(1)


        ##f1.write(byte)

finally:
    f1.close()
    f.close()
