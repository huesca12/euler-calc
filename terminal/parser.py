
def isNumber(x):
    try:
        return str(float(x)) == str(x) or str(int(x)) == str(x)
    except:
        return False

def getMaxDelimiters(x):
    delims = 0
    maxDelims = 0
    maxLoc = -1
    lastMaxLoc = -1
    for i,j in zip(x, range(len(x))):
        if i == '(':
            delims += 1
        
        if i == ')':
            if delims == maxDelims:
                lastMaxLoc = j

            delims -= 1
        
        if delims > maxDelims:
            maxDelims = delims
            maxLoc = j
    
    if lastMaxLoc == -1:
        lastMaxLoc = maxLoc
    return maxDelims, maxLoc, lastMaxLoc

x = [float.__add__, float.__truediv__, float.__pow__, float.__mul__]

def format(string):
    abses = 0
    for i in range(len(string)):
        if string[i] == '|' and abses == 0:
            abses += 1
            string = string[:i] + "abs(" + string[i+1:]
            i += 1
        elif string[i] == '|' and abses == 1:
            abses -= 1
            print(i)
            string = string[:i] + ")" + string[i+1:]
    return string

def getNumbersOnBothSides(x, loc):
    afterNum = beforeNum = 0
    
    j = loc + 1
    while isNumber(x[loc + 1:j]):
        j += 1
    afterNum = float(x[loc + 1:j])
    
    k = loc - 1
    while isNumber(x[k: loc - 1]):
        k -= 1
    beforeNum = float(x[k:loc - 1])
    
    return beforeNum, afterNum

def parse(string):
    if len(string) == 0:
        return []
    funcs = []
    maxDLs, begin, end = getMaxDelimiters(string)
    for i in range(begin, end):
        if string[i] == '^':
            num1, num2 = getNumbersOnBothSides(string, i)
            if num1 is not None and num2 is not None:
                funcs.append((num1, float.__pow__, num2))
            if num1 is None and num2 is not None:
                funcs.append((float.__pow__, num2))

            #funcs.append((float.__pow__, num1, num2))
            #j = i + 1
            #while isNumber(string[i+1:j]):
            #    j += 1
            #if not isNumber(string[i - 1]):
            #    funcs.append((float.__pow__, float(string[i+1:j])))
            #else:
            #    k = i - 1
            #    while isNumber(string[k: i-1]):
            #        k -= 1
            #    funcs.append((float.__pow__, float(string[k:i-1]), float(string[i+1:j])))
    funcs.append(parse(string[:begin] + string[end:]))
    return funcs



if __name__ == "__main__":
    while True:
        i = input("Enter a function \n")
        print(format(i))