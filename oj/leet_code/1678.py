class Solution(object):
    def interpretWithReplace(self, command):
        if command:
            return command.replace("()", "o").replace("(al)", "al")

    def interpret(self, command):
        if command:
            ans = []
            i = 0
            while i < len(command):
                
                if command[i] == "G":
                    ans.append("G")
                    i = i + 1
                elif command[i : i + 2] == "()":
                    ans.append("o")
                    i = i + 2
                elif command[i : i + 4] == "(al)":
                    ans.append("al")
                    i = i + 4

            return "".join(ans)

s = Solution()

assert s.interpret("G()(al)") == "Goal"
assert s.interpret("G()()()()(al)") == "Gooooal"
assert s.interpret("(al)G(al)()()G") == "alGalooG"

assert s.interpretWithReplace("G()(al)") == "Goal"
assert s.interpretWithReplace("G()()()()(al)") == "Gooooal"
assert s.interpretWithReplace("(al)G(al)()()G") == "alGalooG"

