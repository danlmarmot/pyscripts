__author__ = 'danlmarmot'
"""
This Python script measures hash performance, and attempts to answer this question:
'Given a hash function and a block size for reading, which is the fastest hash function and block size?'

There's no warm up, there's no cache/memory/whatever filling, just a simple way to explore performance for
commonly used functions with the timeit library

"""

import timeit
import hashlib
import zlib
import inspect
import sys

# Constants
#*** block sizes for reading ***
# these are sensible defaults
MIN_BLOCK_SIZE = 10
MAX_BLOCK_SIZE = 24

# Number of times to run each combination of hash and block size
NUM_ITERATIONS = 10

# what file to use
TEST_FILE = "testfile.txt"


def main():
    get_timings()


def get_timings():
    func_list = [f for f, v in inspect.getmembers(sys.modules['__main__'], callable) if f.startswith('t_')]

    results = {}
    for f in func_list:
        for i in range(MIN_BLOCK_SIZE, MAX_BLOCK_SIZE):
            func = "%s(filename='%s',block_size=2**%s)" % (f, TEST_FILE, i)
            x = timeit.timeit(func, setup="from __main__ import " + f, number=NUM_ITERATIONS)
            print func + ": " + str(x)
            results[func] = x

    print "\nFastest results:"
    print min(results, key=results.get)


def t_md5sum(filename="testfile.txt", block_size=2 ** 16):
    md5 = hashlib.md5()
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(block_size), b''):
            md5.update(chunk)
    return md5.hexdigest()


def t_sha1sum(filename="testfile.txt", block_size=2 ** 16):
    sha1 = hashlib.sha1()
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(block_size), b''):
            sha1.update(chunk)
    return sha1.hexdigest()


def t_sha224sum(filename="testfile.txt", block_size=2 ** 16):
    sha = hashlib.sha224()
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(block_size), b''):
            sha.update(chunk)
    return sha.hexdigest()


def t_sha256sum(filename="testfile.txt", block_size=2 ** 16):
    sha = hashlib.sha256()
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(block_size), b''):
            sha.update(chunk)
    return sha.hexdigest()


def t_sha384sum(filename="testfile.txt", block_size=2 ** 16):
    sha = hashlib.sha384()
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(block_size), b''):
            sha.update(chunk)
    return sha.hexdigest()


def t_sha512sum(filename="testfile.txt", block_size=2 ** 16):
    sha = hashlib.sha512()
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(block_size), b''):
            sha.update(chunk)
    return sha.hexdigest()


def tno_crc32sum(filename="testfile.txt", block_size=2 ** 16):
    checksum = 0
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(block_size), b''):
            checksum = zlib.crc32(chunk, checksum)
            # Oxffffffff forces checksum to be in range 0 to 2**32-1
    return str(checksum & 0xffffffff)


if __name__ == '__main__':
    main()
