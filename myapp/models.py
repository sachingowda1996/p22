from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=30,unique=True,blank=False)

    def __str__(self):
        return self.topic_name
    

class Webpage(models.Model):
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,unique=True,blank=False)
    url=models.URLField(max_length=100,unique=True,blank=False)

    def __str__(self):
        return self.name


class AccessDetails(models.Model):
    Webpage=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    datetime=models.DateTimeField(auto_now_add=True)        

    def __str__(self):
        return str(self.datetime)