import threading
import socket
import time
l=[0,0,0]
p1=0
p2=0
p3=0
pc=[0,0]
def send(p1):
    while(1):
        print("press 1 to reply to the TC")
        n=int(input())
        if n==1:
            print("node3-->TC")
            sock1 = socket.socket()

            host1 = socket.gethostname()
            sock1.connect((host1, 1025))
            
            if pc[0]==1:
                
                data="NO%"
                data=list(data)
                data.append(l)
                my_new_list = [str(x) for x in data]
                my_new_list=str(my_new_list)
                data1=bytes(my_new_list,'utf-8')
                assert sock1.send(data1)
                
            while(1):
                data=input()
                data=list(data)
                    
                data+='$'
                data+='%'
                if '-' not in data:
                    
                    l[2]=l[2]+1
                    data.append(l)
                print(*data[0:len(data)-2])
                my_new_list = [str(x) for x in data]
                my_new_list=str(my_new_list)
                
                if '-' in my_new_list :
                    break
                else:
                    
                    data=bytes(my_new_list,'utf-8')
                    assert sock1.send(data)
            print("do want send again?")
            x=int(input())
            if x==-1:
                print("out")
                break
            else:
                continue
def rec(p1):
    print("Listening on node3")
    s = socket.socket()
    host = socket.gethostname()
    port = 1027
    s.bind((host,port))
    s.listen(5)
    
    while True:
        conn, addr = s.accept()     
        data = conn.recv(1024)
        data1=str(data,'utf-8')
        s1=""
        for i in range(len(data1)-1):
          if ord(data1[i])==39 or data1[i]=='[' or data1[i]==']' or data1[i]==',':
              pass
          else:
              s1+=data1[i]
        s1=s1.split()
        l1=list(map(str,s1))
        print(*s1[0:len(s1)-4])
        pmc=s1[1:len(s1)-4]
        l1=list(map(str,s1))
        l1=l1[::-1]
        l1=l1[0:4]
        l1=l1[::-1]
        pr=l1[0]

        l1=l1[1:]
        l1=list(map(int,l1))

        l[2]=l[2]+1
        if pr=='#':
            if l1[0]>l[0]:
                l[0]=l1[0]
            print ("Received")
        elif pr=='$':
            if l1[1]>l[1]:
                l[1]=l1[1]
            print ("All Data Received from p2")
        if 'p'and'r'and'e'and'p'and'a'and'r'and'e' in pmc:
            f = open("node3.txt","a")
            f.write(s1[0])
            f.write("\n")
            f.close()
            pc[0]=pc[0]+1
        conn.close()
    
def timer():

    time.sleep(30)
    
    ss = socket.socket()
    host = socket.gethostname()
    ss.connect((host,1025))
    if pc[0]==0:
        pc[1]=1
        print("Did not receive prep message")
    elif pc[0]==3:
        data='^'
        data=bytes(data,'utf-8')
        assert ss.send(data)
        raise ValueError('bad thing happened.')
        

if __name__ =="__main__":
    vc=0
    t1 = threading.Thread(target=send, args=(p1,))
    t2 = threading.Thread(target=rec, args=(p1,))
    t3 = threading.Thread(target=timer, args=())
    t3.start()

    t2.start()
    
    print("send? press 1")
    n=int(input())
    if n==1:
        t1.start()
        t1.join()
    t2.join()
    t1.stop()
    t2.stop()


        
        
