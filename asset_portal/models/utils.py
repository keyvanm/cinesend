import os
import uuid


from django.utils.deconstruct import deconstructible

@deconstructible
class UniqueFilename(object):
    def __init__(self, path):
        self.path = path

    def __call__(self, instance, filename):
        f, ext = os.path.splitext(filename)
        # set filename as random string
        filename = '{}.{}'.format(uuid.uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(self.path, filename)

logos_unique_filename = UniqueFilename("logos")
posters_unique_filename = UniqueFilename("posters")
