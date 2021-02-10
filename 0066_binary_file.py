with open('./data/binary', mode='bw') as bin_file:
    for i in range(17):
        bin_file.write(bytes([i]))

with open('./data/binary', mode='br') as bin_file:
    for b in bin_file:
        print(b)

a = 65534 # FF FE
b = 65535 # FF FF
c = 65536 # 00 01 00 00
d = 2998302 # 00 2D C0 1E

with open('./data/binary2', mode='bw') as bin_file:
    bin_file.write(a.to_bytes(2, 'big'))
    bin_file.write(b.to_bytes(2, 'big'))
    bin_file.write(c.to_bytes(4, 'big'))
    bin_file.write(d.to_bytes(4, 'big'))
    bin_file.write(d.to_bytes(4, 'little')) # big endian or little endian

with open('./data/binary2', mode='br') as bin_file:
    e = int.from_bytes(bin_file.read(2), 'big')
    print(e)
    f = int.from_bytes(bin_file.read(2), 'big')
    print(f)
    g = int.from_bytes(bin_file.read(4), 'big')
    print(g)
    h = int.from_bytes(bin_file.read(4), 'big')
    print(h)
    i = int.from_bytes(bin_file.read(4), 'big')
    print(i)


