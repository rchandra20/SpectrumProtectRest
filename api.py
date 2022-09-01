import spectrumprotect as sp
import json


username = input("Enter your username: ")
password = input("Enter your password: ")

def formatJson(output):
    r = json.loads(output.read().decode('utf-8'))
    return (r)

protocol = 'https'
tcpaddress = '141.211.12.30'
tcpport = '9028'
instance = 'DUCLAIR.DSC.UMICH.EDU'


# Print Test Command that is Query Status
command = 'q node'
try:
    testCmd = ocInstanceUrl.testConnection(ocInstanceUrl, username, password, command)
    response = formatJson(testCmd)
    print(response)

print(__str__)

"""
try:
    # Running my own command
    print ("\nLet's run your own command now\n")
    myCommand = 'query node *'
    myCmd = ocInstanceUrl.runCmd(ocInstanceUrl, username, password,  myCommand)
    response = formatJson(myCmd)
    print (response)

except OSError:
    print('Ooops, something went wrong... Error: ' + ocerror)
"""