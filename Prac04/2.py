usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
'swei45''BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

name = str(input("Enter your name:"))

if name not in usernames:
    print("Access denied")
else:
    print("Access granted")
