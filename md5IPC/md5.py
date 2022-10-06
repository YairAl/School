import hashlib
import multiprocessing
import threading


class MD5:

    def __init__(self, start, end):
        processors = multiprocessing.cpu_count()
        for processor in processors:
            thread = threading.Thread(target=self.decrypt, args=(start, end))
            thread.start()

    def decrypt(self, start, end):
        start = start.zfill(10)
        while start != end:
            result = hashlib.md5(start)

        # printing the equivalent byte value.
        print("The byte equivalent of hash is : ", end="")
        print(result.digest())
