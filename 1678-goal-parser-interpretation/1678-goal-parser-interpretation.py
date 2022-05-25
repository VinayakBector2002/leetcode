class Solution:
    def interpret(self, command: str) -> str:
        # one line solution 
        return command.replace("()","o").replace("(al)","al")
        
        
        
        
        '''
        string_length = len(command)
        string_output = ""
        for i in range(string_length):
            if (command[i] == "("):
                if (command[i+1] == ")"):
                    string_output = string_output + "o"
                else:
                    continue
            else :
                if (command[i] != ")"):
                    string_output = string_output + command[i]
                else:
                    continue
        return string_output
        '''