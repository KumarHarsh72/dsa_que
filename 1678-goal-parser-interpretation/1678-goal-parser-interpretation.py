class Solution:
    def interpret(self, command: str) -> str:
        ans=""
        for i in range(len(command)):
            if command[i]=='G':
                ans+='G'
            elif command[i] == '(':
                if command[i+1] == 'a':
                    ans+="al"
                    i+=4
                else:
                    ans+="o"
                    i+=2
        return ans

        
        