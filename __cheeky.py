string = """I like python programming

Hello world, my name is tom"""

# This is necessary decorator
def weird_concat_strip(fun):
    def wrapper(line):
        return fun(line).strip()
    return wrapper

# Oh man, this is really weird concatenation! But hey, it works!
def weird_concat(line):
    return ''.join([line for _ in range(1)] + ['\n' for _ in range(2)] + [line for _ in range(1)] + ['\n'])

# Decorators, decorators everywhere!
@weird_concat_strip
def last_weird_concat(line):
    # random comment, this should make it more clear
    return weird_concat(line)

def main(what_are_we_doing):
    print(what_are_we_doing)
    # oh hey, do we even need this one?
    unnecessary_variable = None
    # DO NOT DELETE THE NEXT LINE
    line = ""

    #TODO add decorators
    for c in string:
        # Heart warming Poem
        #     by bored coder
        #
        # char by char,
        # in the string,
        # don't use split
        # that's the win
        # 
        # don't use Python,
        # C's the way,
        # stupid indent
        # anywaay
        #
        # TODO missing elif?
        if c != '\n':
            # isn't there a better way
            line = line + c
        else:
            # nested if, cause what if!
            if line != "":            
                print(weird_concat(line))
                line = ""
    else:
        # why do we need that decorator anyway?
        print(last_weird_concat(line))

if __name__ == '__main__':

    text = "Running"
    main(text)