from math import ceil, floor

def boxed_msg(msg):
    lines = msg.split('\n')
    max_length = max([len(line) for line in lines])
    horizontal = '+' + '-' * (max_length + 2) + '+\n'
    res = horizontal
    for l in lines:
        res += format_line(l, max_length)
    res += horizontal
    return res.strip()
    
def format_line(line, max_length):
    half_dif = (max_length - len(line)) / 2 # in Python 3.x float division
    return '| ' + ' ' * ceil(half_dif) + line + ' ' * floor(half_dif) + ' |\n'

print(boxed_msg('first_line\nsecond_line\nthe_ultimate_longest_line'))
# +---------------------------+
# |         first_line        |
# |        second_line        |
# | the_ultimate_longest_line |
# +---------------------------+