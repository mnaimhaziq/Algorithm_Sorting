class trie:
     
    def __init__(self):
        self.root = {"*": "*"}
 
    def insert(self, word):
        cur = self.root
        for char in word:
            if char not in cur:
                cur[char] = {}
            cur = cur[char]
        cur["*"] = "*"
 
    def search(self, word):
        cur = self.root
        for char in word:
            if char not in cur:
                return False
            cur = cur[char]
       
        if "*" in cur:
            return True
        else:
            return False
 
 
if __name__ == "__main__":
    tr = trie()
 
    tr.insert("algoisfunalgoisgreat")
    print(tr.search("algo"))
    print(tr.search("fun"))
 
 
