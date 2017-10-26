import hashlib as hf


class Block:

    def __init__(self, index, ph, dt):
        self.index = index
        self.phash = ph
        self.data = dt
        self.nonce = 0
        self.hashit()
        self.mine()

    def __repr__(self):
        return (str(self.index) + ', ' + self.phash + ', ' + self.data[:25] + ', ' + self.chash)

    def __str__(self):
        return (str(self.index) + ', ' + self.phash + ', ' + self.data[:25] + ', ' + self.chash)

    def hashit(self):
        self.chash = hf.sha256((str(self.index) + self.phash + self.data + str(self.nonce)).encode('utf-8')).hexdigest()

    def isMined(self):
        if self.chash[:4] == '0000':
            return True
        else:
            return False

    def mine(self):
        if not self.isMined():
            while not self.isMined():
                self.nonce += 1
                self.hashit()


class BlockChain:

    def __init__(self):
        self.chain = []
        self.gbl = Block(0, '000079d75cb2b33d2469c9a8aa1e0630d482f836a164fc55aff18ef7fa56ab44', 'gensis block')
        self.chain.append(self.gbl)

    def addBlock(self, inp):
        dt = inp
        blk = Block(len(self.chain), self.chain[len(self.chain)-1].chash, dt)
        self.chain.append(blk)

    def updateData(self, id, inp):
        self.chain[id].data = inp
        self.chain[id].hashit()
        self.chain[id].mine()

    def isChainBroken(self):
        fl = False
        for i in range(1, len(self.chain)):
            if self.chain[i].phash != self.chain[i-1].chash:
                print('chain is broken')
                fl = True
                break
        if not fl:
            print('Chain is not broken')

    def repairChain(self):
        for i in range(1, len(self.chain)):
            if self.chain[i].phash != self.chain[i-1].chash:
                self.chain[i].phash = self.chain[i-1].chash
                self.chain[i].mine()

    def __repr__(self):
        out = ''
        for blk in self.chain:
            out += "< " + str(blk) + " >\n"
        return out
