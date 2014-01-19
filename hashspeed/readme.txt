Here are a couple of simple examples of using the timeit function to test algorithmic efficiency.

The script compares the speed of Python's checksumming for a large file with a few hash functions:
    - md5
    - various SHA*
    - CRC

These hash functions are tested across a range of block sizes, from 10 to 24.

You'll need to supply a file named testfile.txt.   This should be of a reasonable size, say 1 to 4 MB.