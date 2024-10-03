from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100)  # Corrected field name
    sub_category = models.CharField(max_length=100)  # Corrected field name
    title = models.CharField(max_length=100)
    content = models.TextField()  
    author = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/')
    slug = models.CharField(max_length=150)
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return f"{self.category} {self.sub_category} - {self.title} by {self.author}"

class BlogComment(models.Model):
    sno=models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    timestamp=models.DateTimeField(default=now)
    
    def __str__(self):
        return f"{self.comment[0:50]+'...'} {self.post} by {self.user}"
