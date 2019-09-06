from __future__ import unicode_literals
from storages.backends.s3boto import S3BotoStorage


class MediaS3BotoStorage(S3BotoStorage):
    """
    Storage for uploaded media files.
    """

    def __init__(self, *args, **kwargs):
        kwargs['location'] = 'media'
        super(MediaS3BotoStorage, self).__init__(*args, **kwargs)