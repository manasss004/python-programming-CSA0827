def generateParenthesis(n):
    def backtrack(result, current, open_count, close_count):
        if len(current) == 2 * n:
            result.append("".join(current))
            return
        
        if open_count < n:
            current.append("(")
            backtrack(result, current, open_count + 1, close_count)
            current.pop()
        
        if close_count < open_count:
            current.append(")")
            backtrack(result, current, open_count, close_count + 1)
            current.pop()
    
    result = []
    backtrack(result, [], 0, 0)
    return result

n = 3
combinations = generateParenthesis(n)
print(combinations)
