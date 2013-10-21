from storages.backends.s3boto import S3BotoStorage

StaticS3Storage = lambda: S3BotoStorage(location='static')
MediaS3Storage  = lambda: S3BotoStorage(location='media')