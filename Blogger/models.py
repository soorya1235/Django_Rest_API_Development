from django.db import models

class Post(models.Model):
    post_id = models.IntegerField(default=1,unique=True)
    post_name = models.CharField(max_length=100)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    Topic = models.CharField(max_length=100)
    description = models.TextField()
    rank = models.FloatField()

    def uploadPhoto(self,filename):
        path = "Blogger/photos/{}".format(filename)
        return path

    post_image = models.ImageField(upload_to=uploadPhoto,null=True,blank=True)
    # Create your models here.
    def uploadFile(self,filename):
       path = "Blogger/file/{}".format(filename)
       return path

    post_files = models.ImageField(upload_to=uploadFile,null=True,blank=True)

    def __str__(self):
        return f"Post Name => {self.post_name} and Post ID => {self.post_id}"