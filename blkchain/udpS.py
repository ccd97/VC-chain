import socket
import sys
import threading
from blkchain import blockchain
import json

thechain = blockchain.BlockChain()
theq = []
port = 5000
host = 'localhost'
cl = set()

sep1 = ''
sep2 = ''
sep3 = ''


class tr(threading.Thread):
	
	def __init__(self,port,host,data):
		super(tr,self).__init__()
		self.port = port
		self.host = host
		self.data = data
		self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	def run(self):
		global port
		msg = self.data
		at = msg + sep2 + str(port) 
		self.s.sendto(at.encode('utf-8'),(self.host,self.port))


class td(threading.Thread):
	
	def __init__(self):
		super(td,self).__init__()
		global port
		self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.s.bind(("", port))
		print("blkchain - waiting on port:", port)
		
	def run(self):
		global thechain
		thechain.addBlock('server block')
		while True:
			data, addr = self.s.recvfrom(40960)
			inf = data.decode('utf-8')
			dt,rport = inf.split(sep2)
			if dt[:4] == '0110':
				wst,rpt,adrs = dt.split(sep3)
				nc = (adrs,int(rpt))
				if cl.__contains__(nc) == False:
					cl.add(nc)
			elif dt[:4] == '1001':
				nc = (addr[0],rport)
				if cl.__contains__(nc) == False:
					for ss in cl:
						th = tr(int(ss[1]),ss[0],'0110' + sep3 + str(rport) + sep3 + nc[0])
						th.start()
						th.join()
					for ss in cl:
						th = tr(int(nc[1]),nc[0],'0101' + sep3 + str(ss[1]) + sep3 +ss[0])
						th.start()
						th.join()
					dechain = {}
					for i in range(1,len(thechain.chain)):
						dechain[i] = thechain.chain[i].data
					dej = json.dumps(dechain)
					sdt = '0011' + sep3 + dej
					tt = tr(int(nc[1]),nc[0],sdt)
					tt.start()
					tt.join()
					cl.add(nc)
			elif dt[:4] == '0000':
				wst,rpt = dt.split(sep3)
				thechain.addBlock(rpt)
			print('[' + str(thechain.chain[-1]) + ']')


def start():
	t1 = td()
	t1.start()
	t1.join()
