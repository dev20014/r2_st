from django.db import models
from blog_person.r2_storage import PrivateMediaStorage
import uuid
import os
import logging

def path_and_rename(prefix, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex, ext)
    return os.path.join(prefix, filename)


def get_path_for_my_model_file(instance, filename):
    path = path_and_rename('mymodelfiles/', filename)
    print(path)
    logging.info("path")
    logging.info(path)
    return path 

class Document(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.FileField()


class PrivateDocument(models.Model):
    # uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.FileField(upload_to=get_path_for_my_model_file, storage=PrivateMediaStorage())
    # user = models.ForeignKey(User, related_name='documents')