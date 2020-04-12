import gzip


class GZip(object):
    def __init__(self, filepath):
        self.filepath = filepath

    def extract(self, dest_filepath, block_size=65536):
        with gzip.open(self.filepath, 'rb') as s_file, \
                open(dest_filepath, 'wb') as d_file:
            while True:
                block = s_file.read(block_size)
                if not block:
                    break
                else:
                    d_file.write(block)
            d_file.write(block)
