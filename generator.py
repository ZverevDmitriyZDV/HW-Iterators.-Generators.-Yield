import hashlib


def hash_line(file_name):
    with open(file_name, 'r', encoding="utf-8") as f:
        for line in f.readlines():
            yield line, hashlib.md5(line.encode('utf-8')).hexdigest()


test = 'test_input.txt'
for data in hash_line(test):
    print(*data)
