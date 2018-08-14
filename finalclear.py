import paramiko
import xlrd
#imports

def runner(ip, u_name, p_word, komand): #inputs to SSH and gets output DONE
    try:
        ssh= paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, port=22, username=u_name, password=p_word, timeout=10)
        stdin, stdout, stderr =ssh.exec_command(komand)
        output=stdout.readlines()
        return output
    except:
        #print('sarry')
        return []

#finds out how the path was learned DONE
codes_d={'connected':'connected', 'static':'static', 'rip':'rip','bgp':'bgp','ospf':'ospf','aggregate':'aggregate', 'kernel remnant':'kernel remnant', 'hidden':'hidden', 'suppressed':'suppressed','unreachable':'unreachable', 'inactive':'inactive', 'C':"Connected", 'S' : 'Static', 'R' : 'RIP', 'B' : 'BGP','O' :'OSPF' ,'IA' : 'InterArea', 'E' : 'External', 'N' : 'NSSA','A' : 'Aggregate', 'K' : 'Kernel Remnant', 'H' : 'Hidden', 'P' : 'Suppressed','U' : 'Unreachable', 'I' : 'Inactive'}
codes=['connected', 'static', 'rip','bgp','ospf','aggregate', 'kernel remnant', 'hidden', 'suppressed','unreachable', 'inactive', 'C', 'S' , 'R' , 'B','O' ,'IA' , 'E', 'N','A' , 'K' , 'H', 'P','U' , 'I']
learn_l=[]
def learnfinder(x):
    
    z=0
    for y in range (0,len(codes)):
        if codes[z] in x:
            learn_l.append(codes_d[codes[z]])
            break
        else:
            z=z+1

def Main(): #reads the spread sheet with all the names and ip addresses, then matches the names with the ip address DONE
    wb=xlrd.open_workbook('TAC.xlsx')
    ws=wb.sheet_by_name("Devices")
    t_rows=ws.nrows
    for x in range (0,t_rows):
        if 'DS' in ws.cell(x,2).value:
            distswitch(cell(x,3).value)
        elif 'FW' in ws.cell(x,2).value:
            firewall(cell.(x,3).value)
        elif 'LB' in ws.cell(x,2).value:
            loadbalance(cell.(x,3).value)

def distswitch():
    z=runner(ip,'jshi','password','show IP route')
    z=z[6:len(x)]
    for x in range (0,len(z)-2):
        if z[x][0:10]==z[x+1][0:10]:
            del z[x+1]
    addfinder(z)
    destfinder(z)
    learnfinder(z)

#runner('ip', 'u_name', 'p_word', 'komand')
