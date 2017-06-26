class vector(object):

    # constructor
    def __init__(self, xComponent=0, yCompoment=0):
        self.x = xComponent
        self.y = yComponent

    def add(self, vector):
        self.x += vector.x
        self.y += vector.y
