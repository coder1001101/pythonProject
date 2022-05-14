import platform
import os

oprsys = platform.system()
if (oprsys == 'Linux' ):
    print('Linux os')
    os.system('clear')
    print(f'\tThis is Unix (Linux) Operating System')
    os.getcwd()
elif (oprsys == 'Darwin'):
    print('Darwin os')
    os.system('clear')
    print(f'\tThis is Unix (Darwin) Operating System')
    os.getcwd()
elif(oprsys == 'Windows'):
	print('Windows os')
	os.system('cls')
	print(f'\tThis is Windows Operating System')
elif(oprsys == 'Java'):
	print(f'\tThis is Java Operating System')
else:
    print(f'\tCannot be determined any System/OS.')
    #Returns the system/OS name, such as 'Linux', 'Darwin', 'Java', 'Windows'. An empty string is returned if the value cannot be determined.
	