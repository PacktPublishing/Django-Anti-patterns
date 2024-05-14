# apps/blog/models.py

class BlogPost(models.Model):

    title = models.CharField(max_length=100)

    content = models.TextField()

    author = models.ForeignKey("users.User", on_delete=models.CASCADE)

# apps/users/models.py

class User(models.Model):

    username = models.CharField(max_length=100)

    email = models.EmailField()

# apps/comments/models.py

class Comment(models.Model):

    post = models.ForeignKey("blog.BlogPost", on_delete=models.CASCADE)

    author = models.ForeignKey("users.User", on_delete=models.CASCADE)

    content = models.TextField()
