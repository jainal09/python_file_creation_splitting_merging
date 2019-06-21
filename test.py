import shutil
import uuid
import os
from generate_image import FakeFilesFactory
"""psuedo Code for joining blocks in one file"""

GENERATED_FILES = []
chunkedFiles = []
BIN_CHUNK_SIZE = 4000
MERGE_FILE_PATH = "mergedfile/"
GENERATED_FILES_DIR = "Inputfile/generatedimages"

def iterator_function():
    for items in os.listdir(GENERATED_FILES_DIR):
        GENERATED_FILES.append(items)
def split_file():
    for file in GENERATED_FILES:


        with open('Inputfile/generatedimages/' + file, 'rb') as bigfile:
            bigfile.seek(0)
            while True:
                binChunk = bigfile.read(BIN_CHUNK_SIZE)

                if not binChunk: break;

                small_filename = 'splittedfiles/data/{}'.format(str(uuid.uuid4()))
                smallfile = open(small_filename, "wb")
                smallfile.write(binChunk)

                chunkedFiles.append(small_filename)

                if smallfile:
                    smallfile.close()
        print(file + "done")


def join_file():
    for files in GENERATED_FILES:
        with open(MERGE_FILE_PATH + files, 'wb+') as fdst:
            fdst.seek(0)
            source_path = 'splittedfiles/data/'
            for chunkedFilePath in chunkedFiles:
                print("Filename source: ", source_path, " File: ", chunkedFilePath)
                with open(chunkedFilePath, 'rb') as fsrc:
                    shutil.copyfileobj(fsrc, fdst, 640)
    print("File Joining Done")

if __name__ == "__main__":
    generate = FakeFilesFactory()
    iterator_function()
    split_file()
    join_file()

