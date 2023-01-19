# Decryption Commandline-Tool
# Simple way just on Linux commandline:
# echo "R2l0aHViQEJyYWluaHViMjQgfCBiYXNlMzIKZWNobyBHaXRodWJAQnJhaW5odWIyNAo=" | base64 -d
# Result: Github@Brainhub24
import argparse
import base64

def decode(encoded_string):
    decoded_string = base64.b64decode(encoded_string)
    print(decoded_string)

parser = argparse.ArgumentParser(description='Decode base64 encoded strings')
parser.add_argument('-d', '--decode', help='decode the base64 string')
parser.add_argument('-e', '--encode', help='encode the plain string')
parser.add_argument('-f', '--file', help='decode the base64 string from file')
args = parser.parse_args()

if args.decode:
    decode(args.decode)
elif args.file:
    with open(args.file, 'r') as f:
        encoded_string = f.read()
        decode(encoded_string)
elif args.encode:
    encoded_string = base64.b64encode(args.encode.encode())
    print(encoded_string)
else:
    parser.print_help()
