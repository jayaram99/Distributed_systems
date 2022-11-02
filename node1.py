import threading
import socket
import time
import pandas as pd
l=[0,0,0,0,0]
p1=0
p2=0
p3=0
def timer():
    print("prep msg for node",l[4])
    if l[4]==2:
        print("waiting for 1 minute for nodes response")
        time.sleep(60)
        print("After waiting...")
        if l[3]!=2:
            raise ValueError("did not receive yes from both")
        elif l[3]==2:
            f = open("TC.txt","r")
            print("committed")
            print(f.read())
            l[4]=0
            l[3]=0
def send(p1):
    pm="prepare"
    while(1):
        pck="prepare"
        print(" To which process do you want to send? 2 or 3?")
        n=int(input())
        if n==1:
            num+=1
            l.insert(0,num)
        elif n==2:
            print("p1-->p2")
            sock1 = socket.socket()

            host1 = socket.gethostname()
            sock1.connect((host1, 1026))
            #print("vector clock before sending to p2",l)
            while(1):
                data=input()
            
                if pck or '-' not in data:
                    data=list(data)
                    df = pd.DataFrame({'message':[data]})
                    print("dataframe",df )
                    df.to_csv(index=False)
##                    f.write(data)
##                    f.write("\n")
##                    f.close()
                pmc=data[1:]
                tid=data[0]
                data=list(data)
                data+='#'
                
                if '-' not in data:
                    l[0]=l[0]+1
                    data.append(l)
                    
                print(*data[0:len(data)-2])
                my_new_list = [str(x) for x in data]
                my_new_list=str(my_new_list)
                
                if '-' in my_new_list :
                    #print("vector clock after sending to p2",l)
                    break
                else:
                    data=bytes(my_new_list,'utf-8')
                    assert sock1.send(data)
                    if pm == pmc:
                        l[4]=l[4]+1
                        timer()
                    
            print("do want send again?")
            x=int(input())
            if x==-1:
                print("out")
                break
            else:
                continue
        elif n==3:
                print("p1-->p3")
                sock1 = socket.socket()

                host1 = socket.gethostname()
                sock1.connect((host1, 1027))
                #print("vector clock before sending to p3",l)
                while(1):
                    data=input()
                    pmc=data[1:]
                    data=list(data)
                    data+='#'
                    if '-' not in data:
                        
                        l[0]=l[0]+1
                        data.append(l)
                    print(*data[0:len(data)-2])
                    my_new_list = [str(x) for x in data]
                    my_new_list=str(my_new_list)
                    if '-' in my_new_list :
                        #print("vector clock after sending to p3",l)
                        break
                    else:
                        
                        data=bytes(my_new_list,'utf-8')
                        assert sock1.send(data)
                        if pm == pmc:
                            l[4]=l[4]+1
                            timer()
                print("do want send again?")
                x=int(input())
                if x==-1:
                    print("out")
                    break
                else:
                    continue
        
def rec(p1):
    
##    node1 = socket.socket()
##
##    host1 = socket.gethostname()
##    node1.connect((host1, 1026))
##
##    node2 = socket.socket()
##
##    host2 = socket.gethostname()
##    node2.connect((host2, 1027))
##    
    print("Listening on node1")
    s = socket.socket()
    host = socket.gethostname()
    port = 1025
    s.bind((host,port))
    s.listen(5)
    while True:
        conn, addr = s.accept()     
        data = conn.recv(1024)
        data1=str(data,'utf-8')
        if data1=='^':
            print("one of the nodes failed")
        s1=""
        for i in range(len(data1)-1):
          if ord(data1[i])==39 or data1[i]=='[' or data1[i]==']' or data1[i]==',':
              pass
          else:
              s1+=data1[i]
        s1=s1.split()

        if len(s1)!=0:

            l1=list(map(str,s1))
            
            print(*s1[0:len(s1)-4])
            
            l1=l1[::-1]
            l1=l1[0:4]
            
            l1=l1[::-1]
            pr=l1[0]
            
            
            l1=l1[1:len(l1)]
            
            l1=list(map(int,l1))
             
            l[0]=l[0]+1
            
            if pr=='$':
                if l1[1]>l[1]:
                    l[1]=l1[1]
                if l1[2]>l[2]:
                    l[2]=l1[2]
                print ("All Data Received from p2")
            elif pr=='%':
                if l1[1]>l[1]:
                    l[1]=l1[1]
                print ("All Data Received from p3")
                if l1[2]>l[2]:
                    l[2]=l1[2]
            
            
            if 'y' and 'e' and 's' in s1:
                #f = open("TC.txt","a")
                f = pd.read_csv("TC.csv")
                #f.write("YES\n")
                l[3]=l[3]+1
            if l[3]==2:
                print(l[3])
                print(l[4])
##                f.write("committed tid:")
##                f.write(str(s1[0])+"\n")
##                f.close()
                df = pd.DataFrame({'tid': [str(s1[0])]})
                df.to_csv(index=False)
                print(df)
                
    ##      data='committed'
    ##      data=bytes(data,'utf-8')
    ##      assert node1.send(data)
    ##      assert node2.send(data)
                
            
            conn.close()
        
    

    
##    if count!=2:
##        raise Exception('abbort, could not recieve response message')
    

if __name__ =="__main__":
    vc=0

    t1 = threading.Thread(target=send, args=(p1,))
    t2 = threading.Thread(target=rec, args=(p1,))
    #t3 = threading.Thread(target=timer, args=())
    t2.start()
    #t3.start()

    
    
    print("send? press 1")
    n=int(input())
    if n==1:
        t1.start()
        t1.join()
    t2.join()

    print("Done!")


        
        
