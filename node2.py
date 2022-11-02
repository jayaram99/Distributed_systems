import threading
import socket
import time

l=[0,0,0]
p1=0
pc = [0,0]
def send(p1):
    while(1):
        
        print(" press 1 to reply to the TC")
        n=int(input())
        
        if n==1:
            print("node1-->TC")
            if pc[1]==1:
                data="1NO"
                data=bytes(data,'utf-8')
                assert sock1.send(data)
                print("p2-->p1")
            sock1 = socket.socket()

            host1 = socket.gethostname()
            sock1.connect((host1, 1025))
            #print("vector clock before sending to p1",l)
            while(1):
                data=input()
                data=list(data)
                x=data[0]
##                if 'y' and 'e' and 's' in data[1:] :
##                    f = open("node2.txt","a")
##                    f.write(x)
##                    f.close()
                data+='$'
                if '-' not in data:
                    
                    l[1]=l[1]+1
                    data.append(l)
                print(*data[0:len(data)-2])
                my_new_list = [str(x) for x in data]
                my_new_list=str(my_new_list)

                if '-' in my_new_list :
                    #print("vector clock after sending to p1",l)
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
    print("Listening on node2")
    s = socket.socket()
    host = socket.gethostname()
    port = 1026
    s.bind((host,port))
    s.listen(5)
    
    while True:
        #time.sleep(10)
        #print("gud morning")
        conn, addr = s.accept()     # accept the connection
        data = conn.recv(1024)
        data1=str(data,'utf-8')
        #print("vector clock before receiving",l)
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
         
        l[1]=l[1]+1
        if pr=='#':
            if l1[0]>l[0]:
                l[0]=l1[0]
            print ("All Data Received from p1")
        elif pr=='%':
            if l1[2]>l[2]:
                l[2]=l1[2]
            print ("All Data Received from p3")
        #print("vector clock after receiving",l)
        x=s1[0]
        if 'p'and'r'and'e'and'p'and'a'and'r'and'e' in pmc:
            f = open("node2.txt","a")
            f.write(s1[0])
            f.write("\n")
            f.close()
            pc[0]=pc[0]+1
        conn.close()
        
def timer():

    time.sleep(120)
    
    ss = socket.socket()
    host = socket.gethostname()
    ss.connect((host,1025))
    if pc[0]==0:
        pc[1]=1
        data='^'
        data=bytes(data,'utf-8')
        assert ss.send(data)
        raise ValueError('did not receive prepare message bad thing happened.')
    
if __name__ =="__main__":
    vc=0
 
    t1 = threading.Thread(target=send, args=(p1,))
    t2 = threading.Thread(target=rec, args=(p1,))
    t2.start()
    
    print("send? press 1")
    n=int(input())
    if n==1:
        t1.start()
        t1.join()
    t2.join()

    print("Done!")


        
        
