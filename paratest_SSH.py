import paramiko
import xlrd

def runner(ip, u_name, p_word, komand):
    ssh= paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port=22, username=u_name, password=p_word, timeout=10)
    stdin, stdout, stderr =ssh.exec_command(komand)
    output=stdout.readlines()
    return output

############################################################################
            ############################################################################
numberdots=['0','1','2','3','4','5','6','7','8','9','.']
add_l=[]
mask_l=[]
def addfinder(x):
    slash=x.find('/')
    back=1
    dot=0
    #print(back)
    while True:
        if x[slash-back]=='.':
            #print('dot')
            dot=dot+1
            back=back+1
        elif (x[slash-back] not in numberdots )and (dot==3):

            #print(x[slash-back+1:slash])
            add_l.append(x[slash-back+1:slash])
            if x[slash+3] not in numberdots:
                mask_l.append(x[slash+1:slash+3])
            else:
                mask_l.append(x[slash+1:slash+2])
            break
        elif (x[slash-back] not in numberdots )and (dot !=3):
            #print('none')
            break
        elif back>slash:
            #print('none')
            break
        else:
            #print(x[slash-back])
            back=back+1
############################################################################
            ############################################################################
dest_l=[]
def destfinder(x):
    
    if 'via' in x:
        dest_l.append(x[x.find('via')+4:x.find(',')])

############################################################################
            ############################################################################
codes_d={'connected':'connected', 'static':'static', 'rip':'rip','bgp':'bgp','ospf':'ospf','aggregate':'aggregate', 'kernel remnant':'kernel remnant', 'hidden':'hidden', 'suppressed':'suppressed','unreachable':'unreachable', 'inactive':'inactive', 'C':"Connected", 'S' : 'Static', 'R' : 'RIP', 'B' : 'BGP','O' :'OSPF' ,'IA' : 'InterArea', 'E' : 'External', 'N' : 'NSSA','A' : 'Aggregate', 'K' : 'Kernel Remnant', 'H' : 'Hidden', 'P' : 'Suppressed','U' : 'Unreachable', 'I' : 'Inactive'}
codes=['connected', 'static', 'rip','bgp','ospf','aggregate', 'kernel remnant', 'hidden', 'suppressed','unreachable', 'inactive', 'C', 'S' , 'R' , 'B','O' ,'IA' , 'E', 'N','A' , 'K' , 'H', 'P','U' , 'I']

def learnfinder(x):
    learn_l=[]
    z=0
    for y in range (0,len(codes)):
        if codes[z] in x:
            learn_l.append(codes_d[codes[z]])
            break
        else:
            z=z+1

def distswitch(ip):
    z=runner(ip,'#####','password','show IP route')
    z=z[6:len(x)]
    for x in range (0,len(z)-2):
        if z[x][0:10]==z[x+1][0:10]:
            del z[x+1]
    addfinder(z)
    destfinder(z)
    learnfinder(z)
     
fwcodes=['C', 'S', 'R', 'B','O','A', 'K ', 'H', 'P','U', 'i']
       
def firewall(ip):
    z=runner(ip,'#####','password','show route')
    z=z[6:len(x)]
    for x in range (0,len(z)):
        if z[x][0] not in fwcodes:
            del z[x]
    addfinder(z)
    destfinder(z)
    learnfinder(z)

def loadbalance(ip):
    z=runner(ip,'#####','password','netstat -r')
    z=z[2:len(x)]
    for x in range (0,len(z)):
        if z[x][0] =='d':
            



wb=xlrd.open_workbook('TAC.xlsx')
ws=wb.sheet_by_name("Devices")
t_rows=ws.nrows

for x in range (0,t_rows):
    if 'DS' in ws.cell(x,2).value:
        distswitch(cell.(x,3).value)
    elif 'FW' in ws.cell(x,2).value:
        firewall(cell.(x,3).value)
    elif 'LB' in ws.cell(x,2).value:
        loadbalance(cell.(x,3).value)

'''x=runner('192.168.0.13','admin','password','sh ip int br')
addfinder(z)
destfinder(z)
learnfinder(z)

print(add_l)
print(mask_l)
print(dest_l)
print(learn_l)




ip_l=[]


parse_l=runner('192.168.0.13','admin','password','sh ip int br')


for x in range (0,len(ip_l)):
    parse_l=runner(ip_l[x],'########','########','sh ip route')'''


