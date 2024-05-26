def solve(a, b, c, d, e, f):
  for x in range(-999, 1000):
    for y in range(-999, 1000):
      if a * x + b * y == c and d * x + e * y == f:
        return x, y

if __name__ == '__main__':

    a, b, c, d, e, f = map(int, input().split())

    x, y = solve(a,b,c,d,e,f)

    print("{} {}".format(x, y))

