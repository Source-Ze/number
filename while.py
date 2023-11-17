from owns import send_shell
import time
 
l = ['su.py', 'bh.py','om.py','ku.py','ar.py']

while True:
    for i in l:
        try:
            send_shell('python3', i)
        except:
            pass

    time.sleep(3)