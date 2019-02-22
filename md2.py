import fileinput

# Adds the padding so its size is a multiple of 16 bytes
# Recieves a string S
# Returns a message M in bytes
def add_padding(S):
    M = S.encode('utf-8') #convert to byte format, still is a string
    M = bytes(M) #actually convert to byte
    size = len(M) #meassure size of bytes
    missing_bytes = (16 - size % 16)%16 + 1 #calculates the length needed for the padding
    for i in range(1, missing_bytes):
        M += bytes([i])
    return M

# initializesa var size the num_bytes given with the value provided
# recieves two ints, num_bytes and value
def initialize(num_bytes, value):
    A = bytes()
    for i in range(num_bytes):
        A+= bytes([value])
    return A

# Generates the checksum
# Recieves a message M in bytes and a message S as a string
def checksum(S,M):
    L = 0
    C = initialize(16, 0)
    N = len(M)
    for i in range(int(N/16)):
        for j in range(16):
             c=M[16*i+j]
             #c=bytes([M[16*i+j]])
             #print(int(c)^int(L))
             C[j]=int(C[j])^int(S[c^L])
             L=C[j]
    return C

# Generates the hash
# Recieves the message with the checksum MC
def _hash(M):
    N = len(M)
    X = initialize(48, 0)
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
    return X

def main():
    file_input = fileinput.input()
    S = file_input[0].replace("\n", "").replace('"', "")
    M = add_padding(S)
    print(M)
    # L = 0
    # print(C)
    C = checksum(S,M)
    MC = M+C
    #hash = _hash(MC)
    print(hash)
if __name__ == "__main__":
    main()
