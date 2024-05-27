import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())

    records = {}

    for _ in range(n):
        name, action = sys.stdin.readline().strip().split()
        if action == "enter":
            records[name] = True
        else:
            records.pop(name, None)

    for name in sorted(records.keys(), reverse=True):
        print(name)
