import socket
import sys
import threading
from blkchain import blockchain
import json


thechain = blockchain.BlockChain()
theq = []
port = 5200
host = 'localhost'
cl = {('localhost', '5000')}

sep1 = ''
sep2 = ''
sep3 = ''

def addFile(commit, name, size, code, previous_file):
    global theq
    data = str(commit)+sep1+name+sep1+str(size)+sep1+code+sep1+str(previous_file)
    theq.append(data)

def bdata_to_file(i, data):
    class file:
        def __init__(self, key, commit, name, size, code, previous_file):
            self.key = int(key)
            self.commit = int(commit)
            self.name = name
            self.size = int(size)
            self.code = code
            self.previous_file = int(previous_file)

        def __repr__(self):
            return str(self.key)+sep1+str(self.commit)+sep1+self.name+sep1+str(self.size)+sep1+self.code+sep1+str(self.previous_file)

    return file(i ,data[0], data[1], data[2], data[3], data[4])

def getfiles(key=None, commits=None, reverse=False):
    rqd = []
    global thechain

    if key is not None:
        return [bdata_to_file(key, thechain.chain[key].data.split(sep1))]

    for i in range(2, len(thechain.chain)):
        dt = thechain.chain[i].data.split(sep1)

        if commits is not None:
            if int(dt[0]) in commits:
                rqd.append(bdata_to_file(i, dt))
                continue

    rqd.sort(key=lambda f: f.key, reverse=reverse)
    return rqd


class tr(threading.Thread):

    def __init__(self, port, host, data):
        super(tr, self).__init__()
        self.port = port
        self.host = host
        self.data = data
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def run(self):
        global port
        msg = self.data
        at = msg + sep2 + str(port)
        self.s.sendto(at.encode('utf-8'), (self.host, self.port))


class td(threading.Thread):

    def __init__(self):
        super(td, self).__init__()
        global port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.bind(("", port))
        print("blkchain - waiting on port:", port)

    def run(self):
        global thechain
        while True:
            data, addr = self.s.recvfrom(40960)
            # print(data, addr)
            inf = data.decode('utf-8')
            dt, rport = inf.split(sep2)
            if dt[:4] == '0110':
                wst, rpt, adrs = dt.split(sep3)
                nc = (adrs, int(rpt))
                if not cl.__contains__(nc):
                    cl.add(nc)
            elif dt[:4] == '0101':
                wst, rpt, rhst = dt.split(sep3)
                nc = (rhst, int(rpt))
                if not cl.__contains__(nc):
                    cl.add(nc)
            elif dt[:4] == '0011':
                wst, newchain = dt.split(sep3)
                dechain = json.loads(newchain)
                for a in dechain:
                    thechain.addBlock(dechain[a])
                # print(thechain)
            elif dt[:4] == '1001':
                nc = (addr[0], rport)
                if not cl.__contains__(nc):
                    for ss in cl:
                        th = tr(int(ss[1]), ss[0], '0110' + sep3 + str(rport) + sep3 + nc[0])
                        th.start()
                    cl.add(nc)
            elif dt[:4] == '0000':
                wst, rpt = dt.split(sep3)
                thechain.addBlock(rpt)
            # print(cl)
            # print(thechain)


class dtr(threading.Thread):
    
    def __init__(self):
        super(dtr, self).__init__()

    def run(self):
        data = "first pinggg"
        global port
        global thechain
        for nc in cl:
            host = nc[0]
            pt = int(nc[1])
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            msg = data
            at = '1001' + sep3 + msg + sep2 + str(port)
            s.sendto(at.encode('utf-8'), (host, pt))
        while True:
            global theq
            while len(theq) > 0:
                data = theq.pop()
                thechain.addBlock(data)
                for nc in cl:
                    host = nc[0]
                    pt = int(nc[1])
                    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    msg = data
                    at = '0000' + sep3 + msg + sep2 + str(port)
                    s.sendto(at.encode('utf-8'), (host, pt))


def startClient():
    t1 = td()
    t2 = dtr()
    t1.start()
    t2.start()