# https://practice.geeksforgeeks.org/problems/get-minimum-element-from-stack/1
# https://www.geeksforgeeks.org/design-a-stack-that-supports-getmin-in-o1-time-and-o1-extra-space/
# this can be easily solved using an extra arr whose ith position stores min element upto that ith element but space cost will be O(N)
# another way to calculte min every time we pop and update min every time when the pushed element is smaller then the current element but that would cost O(N) for pop()

# another way to store two values at a single index .
# since val can range from 1 to 100 hence can store 2 value at a single position of array
# mod is largest val +1
# val//mod gives min upto that element 
# val%mod gives the element itself.


class stack:
    def __init__(self):
        self.s=[]
        #self.minEle=None
        self.mod=101
        
    def push(self,x):
        #CODE HERE
        if not self.s or  x<self.s[-1]//self.mod:
            minEle=x
            x+=minEle*self.mod
            self.s.append(x)
        else:
            minEle=self.s[-1]//self.mod
            x+=minEle*self.mod
            self.s.append(x)
            
    def pop(self):
        #CODE HERE
        if self.s:
            return self.s.pop()%self.mod
        return -1
        
    def getMin(self):
        #CODE HERE
        if self.s:
            return self.s[-1]//self.mod
        return -1

# the whole idea is to store curr min and update min when acutal min is poped 
# other way is store 2*curr_min-prev_min at the postion where curr min is found,
# this formula actually keeps track of whether or not top elelemt is actual element or it is manupulated
# every time we get a request to push x
# we check that if its less then the curr_min 
# then we update curr min and store 2*curr_min-prev element lets (say this as val)
# val is always less then curr_min since prev was greater then curr_min
# hence whenever we encounter a value poped is less then the curr_min
# we know that its not the actual element but manuiplated value of curr_min
# in other words we need to pop curr_min and update curr_min 
# curr_min=2*curr_min-poped_element
# where poped element is nothing but 2*curr_min-prev_min
# hence we retrive min val after poping curr_min

class stack:
    def __init__(self):
        self.s=[]
        self.minEle=None

    def push(self,x):
        #CODE HERE
        if self.s and self.minEle>x:
        # what we are trying here is to store some that can be retrive 
            self.s.append(2*x-self.minEle)
            self.minEle=x
        else:
            self.s.append(x)
            if len(self.s)==1:
                self.minEle=x
            

    def pop(self):
        #CODE HERE
        if self.s: 
            val=self.s.pop()
            if val<self.minEle:
                val,self.minEle=self.minEle,2*self.minEle-val
                
            return val
        else:
            return -1
        

    def getMin(self):
        #CODE HERE
        if self.s:
            return self.minEle
        return -1

