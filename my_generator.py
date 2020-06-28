import hashlib

def my_generator(file):
    with open (file, 'r') as source_file:
        lines = source_file.readlines()
        start = 0
        end = len(lines)
        while start < end:
            data = hashlib.md5(lines[start].encode()).hexdigest()
            yield data
            start += 1

for i in my_generator('test.txt'):
    print(i)



