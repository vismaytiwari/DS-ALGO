class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        hashmap = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        dic = {}
        for i,v in enumerate(hashmap):
            dic[chr(i+97)] =  v
        data = set()
        for word in words:
            ans=''
            for w in word:
                ans+=dic[w]
            data.add(ans)
        return len(data)