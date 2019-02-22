

def checksum(M):
    L = 0
    C = [0]*(16)
    N = sizeInBytesOf(M)#len(M.encode('utf-8'))
    for i in range(int(N/16)):
        for j in range(16):
            c=M[16i+j]
            C[j]=C[j]^S[c^L]
            L=C[j]
    return C

def _hash(M):
    N = sizeInBytesOf(M)
    X = [0]*(48)
    for i in range(int(N/16)):
        for j in range(16):
            X[j+16]=M[16*i*j]
            X[j+32]=M[j+16]^X[j]
        t=0
        for j in range(18):
            for k in range(48):
                t=X[k]^S[t]
                X[k]=t
            t=(t+j)%256
def main():
    S = input() # plaintext
    M = add_padding(plaintext)
    C = checksum(M)
    M = M+C
    Encrypted = _hash(M)
    print(Encypted)
