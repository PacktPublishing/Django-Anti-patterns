# models.py in a single Django app

class BlogPost(models.Model):

    title = models.CharField(max_length=100)

    content = models.TextField()

    author = models.ForeignKey("User", on_delete=models.CASCADE)

    # ... other blog-related fields

class User(models.Model):

    username = models.CharField(max_length=100)

    email = models.EmailField()

    # ... other user-related fields

class Comment(models.Model):

    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    content = models.TextField()

    # ... other comment-related fields
