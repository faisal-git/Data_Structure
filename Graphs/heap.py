# heapdict ,heap,priority queue,


import heapdict 
  
h = heapdict.heapdict() 
  
# Adding pairs into heapdict 
h['g']= 2
h['e']= 1
h['k']= 3
h['s']= 4
print(len(h))
print('list of key:value pairs in h:\n',  
      list(h.items())) 
print('pair with lowest priority:\n', 
      h.peekitem()) 
print('list of keys in h:\n', 
      list(h.keys())) 
print('list of values in h:\n', 
      list(h.values())) 
print('remove pair with lowest priority:\n', 
      h.popitem()) 
print('get value for key 5 in h:\n', 
      h.get(5, 'Not found')) 
  
# clear heapdict h 
h.clear() 
print(list(h.items())) 