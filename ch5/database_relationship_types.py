from django.db import models

# One-to-One Relationship
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()

# One-to-Many Relationship
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

# Many-to-Many Relationship
class Group(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User)
