
def solve(n):
  s = str(n)
  sign = 1
  start = 0
  if n < 0:
    sign = -1
    start = 1
  for i in range(start, len(s)):
    print(i)
    print(f"{sign*int(s[i])} <= {sign*5}")
    if sign*int(s[i]) <= sign*5:
      return int(s[:i] + "5" + s[i:])
  return int(s + '5')

print(solve(-64256))
