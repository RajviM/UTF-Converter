# UTF-Converter
Each program to encode in UTF-8


A Python program takes a path to an input file (absolute path name) as the first parameter.  
It will read the file as a binary file, and assume that it contains characters from Unicode's Basic Multilingual Plane (U+0000 to U+FFFF) in UTF-16 encoding (big endian),   that is every 2 bytes correspond to one character and directly encode that character's Unicode code point.   
The program will encode each character in UTF-8 (between 1 and 3 bytes), and write the encoded bytes to a file called utf8encoder_out.txt.  
