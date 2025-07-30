class sol():
    def pri(self,name , n):
        if(n == 0):
            return
    
        print(name)
        self.pri(name,n-1)


s = sol()
s.pri("sam",5)