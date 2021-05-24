from django.db import models

# Create your models here.
class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = " Show title should be at least 2 characters."
        if len(postData['network']) < 3:
            errors["network"] = " Show network should be at least 2 characters."
        if len(postData['desc']) < 10:
            errors["desc"] = "Show description should be at least 2 characters." 
        return errors    
        

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    desc = models.TextField(null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()