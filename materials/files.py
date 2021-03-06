# w   writes into the file, and removing existing content
# w+  writes into the file, reads the file, and removing existing content. If file does not exist, it creates a new one
# r   reads the file
# r+  writes into the file, reads the file, without removing existing content
# a   writes into the file, without removing existing content
# a+  writes into the file, reads the file, without removing existing content. If file does not exist, it creates a new one

# Try copying this into a folder with a file called "data.txt" and see what happens
# modify data.txt a bit

with open('data.txt', 'r') as Filea:
    Q = Filea.read(12)
    Filea.seek(0)
    P = Filea.read()
    print(Q)
    print(P)


A = 'A'
B = '2'
C = 'C3'

with open('data.txt', 'w') as filea:
    filea.write(f'{A}{B}{C}')

D = 'D++'

with open('data.txt', 'a') as filea:
    filea.write(f'\n{D}')