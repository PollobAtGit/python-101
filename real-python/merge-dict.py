v = { 'a': 10 }
vv = { 'b': 100 }

def q(**kwargs):
  print(type(kwargs))
  for x, y in kwargs.items():
    print(x, y)

q(**v)
q(**v)

# merged dictionary
q(**{**v, **vv})
q(**dict(v, **vv))
