import threading
import paramiko
import time
import concurrent.futures

#========================1st section implements threading using threading module=================

#list of threads
threads = []
suts = ['10.116.59.178','10.116.59.179','10.116.86.149','10.116.59.133']
#suts = ['10.116.59.178']
res = {}

print("start time is {}".format(time.asctime(time.localtime(time.time()))))
def connectLinux(host):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=host,username='root',password='welcome')
    stdin,stdout,stderr=ssh_client.exec_command('ls')

    for file in stdout:
        if host in res:
            res[host].append(file)
        else:
            res[host] = []
            res[host].append(file)


'''
for sut in suts:
    t = threading.Thread(target=connectLinux,args=(sut,))
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

#print(res)
print("End time is {}".format(time.asctime(time.localtime(time.time()))))
'''
#========================1st section implements threading using threading module=================
#this module is wrapper over Threading module

lst = [5,4,3,2,1]


def testfunc(i):
    print(f'sleeping for {i} sec')
    time.sleep(i)
    print(f'done sleeping for {i} sec')
    return i

with concurrent.futures.ThreadPoolExecutor() as executor:
    '''
    # f1 = executor.submit(testfunc(),1)  this is one way to create a thread and call a function

    #to call it with an in loop , result will be list of all returned value of testfunc method
    results = [executor.submit(testfunc,sec) for sec in lst]

    #this will print results when all threads completes execution
    for f in concurrent.futures.as_completed(results):
        print(f.result())
    '''

    # we can write above code using map  , it will create thread for all elements in lst and execute testfunc menthod
    results = executor.map(testfunc,lst)

    for result in results:
        print(result)


#print(res)

print("End time is {}".format(time.asctime(time.localtime(time.time()))))