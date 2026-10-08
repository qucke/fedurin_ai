import re
with open("a.txt") as f:
  pat = re.compile(r'^[\w]+(ть)(с[яь])?\s[\w]+о$|^[\w]+о\s[\w]+(ть)(с[яь])?$')
  for s in f:
    ss = re.search(pat, s.strip())
    if ss is not None:
      print(ss.group())
