from pygments.lexers import guess_lexer_for_filename
from pygments.formatters import TerminalTrueColorFormatter
from pygments import highlight
import pygments
import sys

def process(_file, code):
    try:
        lexer = guess_lexer_for_filename(_file, code)
    except pygments.util.ClassNotFound:
        return code
    return highlight(code, lexer, TerminalTrueColorFormatter())

if __name__ == '__main__':

    for line in sys.stdin:
        # sys.stderr.write("DEBUG: got line: " + line)
        # sys.stdout.write(line)
        path, *code = line.split(':')
        if path.startswith('Binary file'):
            print(line, end='')
        else:
            _file = path.split('/')[-1]
            print(path + ":" + process(_file, ':'.join(code).strip()), end='')
