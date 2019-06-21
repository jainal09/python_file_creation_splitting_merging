from multiprocessing.dummy import Pool as ThreadPool
from PIL import Image
from uuid import uuid4
from traceback import print_exc
import numpy


MAX_IMAGE_GEN_THREAD_POOL_SIZE = 4

class FakeImageBuilder():
    def createimage(self, pool_size = None, imagesCount=1, height=1280, width=1024):
        try:
            self._generatedImageNames = []
            pool_size = pool_size - 1
            def generateImage():
                if pool_size == 0:
                    print()
                    return True
                else:
                    thisImageName =  "Inputfile/generatedimages/"+ str(uuid4()) + ".jpeg"

                    imarray = numpy.random.rand(height, width, 3) * 255
                    im = Image.fromarray(imarray.astype('uint8')).convert('L')
                    results = im.save(thisImageName)

                    self._generatedImageNames.append(thisImageName)

            x = self.pool.apply_async(generateImage)
            x.get()


        except Exception as e:
            print_exc()

    def buildFakeImages(self, imagesCount=8, height=1024, width=1280):
        pool_size = int(imagesCount % MAX_IMAGE_GEN_THREAD_POOL_SIZE)
        self.pool = ThreadPool(pool_size or 1)

        while imagesCount != 0:
            self.createimage(pool_size, height, width)
            imagesCount = imagesCount - 1
        self.pool.close()
        self.pool.join()

    def getGeneratedImageNames(self):
        return self._generatedImageNames

class FakeFilesFactory():
    def __init__(self):
        self.imageBuilder = FakeImageBuilder()
        self.imageBuilder.buildFakeImages()

    def getRandomFile(self):
        pass

    # Purpose: Generates random files
    # (image)
    # Parameters:
    #         imagesCount: Number of images
    #         to generate
    def getRandomFiles(self, imagesCount):
        return self.imageBuilder.buildFakeImages()

