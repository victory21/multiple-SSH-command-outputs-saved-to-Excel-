import paramiko
import time

ssh= paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.116.180.53', port=22, username='admin', password='password', timeout=100)

#stdin, stdout, stderr =ssh.exec_command('sh ip int br')
#output=stdout.readlines()
#print('\n'.join(output))


console=ssh.invoke_shell()

console.send('en\n')
time.sleep(.1)

console.send('password\n')
time.sleep(.1)

console.send('sh ip int br\n')
time.sleep(.1)

output = console.recv(999999999)

putput=output.decode("utf-8") 

string=putput.split('\r\n')


print(string)

