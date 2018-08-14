import paramiko
import xlrd
import xlwt

#ROW, COLLOUMN
#wb=xlrd.open_workbook('TEST.xlsx')
#ws=wb.sheet_by_name("Sheet1")
#t_rows=ws.nrows
workbook= xlwt.Workbook()
ws =workbook.add_sheet('test')

at_row_num=1

def runner(ip, u_name, p_word, komand): #inputs to SSH and gets output DONE
    try:
        ssh= paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, port=22, username=u_name, password=p_word, timeout=10)
        stdin, stdout, stderr =ssh.exec_command(komand)
        output=stdout.readlines()
        #print(output[4].find(' '))
        #print(output[4].find(' ',output[4].find(' ')))
        return output
    except:
        #print('sarry')
        return []
ip_list=['172.23.13.3','172.23.45.3','172.23.77.3','172.23.109.3']
known_ints=[]

#lol=[]
for y in range (0,len(ip_list)):
    sh_ip_LIST=runner(ip_list[y],'jshi695','7UJM,ki8','list net self')
    
    for x in range(0,len(sh_ip_LIST)):
        if sh_ip_LIST[x]=='}':
            int_name=sh_ip_LIST[x-1].split()[1]

            if int_name not in known_ints:
                known_ints.append(int_name)
                ws.write(at_row_num,0,int_name)
                at_row_num=at_row_num+1
                
        elif 'address' in sh_ip_LIST[x]:
            ip_name=sh_ip_LIST[x].split()[1]

            ws.write(known_ints.index(int_name)+1,y+1,ip_name)

workbook.save('output.xls')

wb=xlrd.open_workbook('output.xls')
ws=wb.sheet_by_name("test") #READING FROM THIS
num_rows=ws.nrows
num_cols=ws.ncols



#st.pattern.pattern_fore_colour = 1

workbook= xlwt.Workbook()
wr =workbook.add_sheet('Sheet1') #wr WORKBOOK WRITE

for x in range (1,num_rows):
    alarm=0
    #st.pattern.pattern_fore_colour = 1
    for y in range (1, num_cols-1):
        try:
            #print (alarm)
            f=int(ws.cell(x,y).value.split('.')[2])
            #print(f)
            try:
                s=int(ws.cell(x,y+1).value.split('.')[2])
                #print (alarm)
                if s!=f+32:
                    alarm=1
                    break
            except:
                alarm=1
                break
        except:
            alarm=1
            break

    print (alarm)
    if alarm==0:

        #print("hi")
        for y in range (1, num_cols):
            wr.write(x,y,ws.cell(x,y).value)
    elif alarm==1:
        st = xlwt.easyxf('pattern: pattern solid;')
        st.pattern.pattern_fore_colour = 2
        #print('hi')
        for y in range (1, num_cols):
            wr.write(x,y,ws.cell(x,y).value,st)

for y in range (0,len(ip_list)):
    wr.write(0,y+1,ip_list[y])

for x in range (0,num_rows):
    wr.write(x,0,ws.cell(x,0).value)
    
            
workbook.save('final.xls')

    
    
