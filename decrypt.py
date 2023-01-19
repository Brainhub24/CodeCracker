# Decryption Commandline-Tool
# Simple way just on Linux commandline:
# echo "R2l0aHViQEJyYWluaHViMjQgfCBiYXNlMzIKZWNobyBHaXRodWJAQnJhaW5odWIyNAo=" | base64 -d
# Result: Github@Brainhub24
import base64

encoded_string = "R2l0aHViQEJyYWluaHViMjQgfCBiYXNlMzIKZWNobyBHaXRodWJAQnJhaW5odWIyNAo="
decoded_string = base64.b64decode(encoded_string)
print(decoded_string)
