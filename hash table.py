MAX_LOAD = 0.75


class HashTable:
    def __init__(self):
        self.cap = 8
        self.size = 0
        self.table = [[] for _ in range(self.cap)]

    def h(self, key):
        res = 0
        for c in key:
            res = (res * 31 + ord(c)) % self.cap
        return res

    def resize(self):
        old = self.table
        self.cap *= 2
        self.table = [[] for _ in range(self.cap)]
        for bucket in old:
            for k, v in bucket:
                self.table[self.h(k)].append([k, v])

    def put(self, key, value):
        bucket = self.table[self.h(key)]
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return
        bucket.append([key, value])
        self.size += 1
        if self.size > self.cap * MAX_LOAD:
            self.resize()

    def get(self, key):
        for k, v in self.table[self.h(key)]:
            if k == key:
                return v
        return None

    def delete(self, key):
        bucket = self.table[self.h(key)]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                v = bucket[i][1]
                bucket.pop(i)
                self.size -= 1
                return v
        return None


q = int(input())
t = HashTable()
out = []
for _ in range(q):
    cmd = input().split()
    if cmd[0] == 'put':
        t.put(cmd[1], int(cmd[2]))
    elif cmd[0] == 'get':
        v = t.get(cmd[1])
        out.append('Error' if v is None else str(v))
    elif cmd[0] == 'del':
        v = t.delete(cmd[1])
        out.append('Error' if v is None else str(v))
    else:
        out.append(str(t.size))
print('\n'.join(out))
