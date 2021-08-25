

import test_modules

def test_0():
    print "path:", test_modules.__path__
    print "name:", test_modules.__name__

if __name__ == '__main__':
    test_0()