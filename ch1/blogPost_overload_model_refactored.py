class BlogPost(models.Model):

    title = models.CharField(max_length=200)

    content = models.TextField()

    published_date = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)


# Use signals to handle side effects

from django.db.models.signals import post_save

from django.dispatch import receiver


@receiver(post_save, sender=BlogPost)
def handle_post_save(sender, instance, created, **kwargs):

    if created:

        update_tags(instance)

        send_notifications(instance)


def update_tags(post):

    # Logic to update tags

    pass


def send_notifications(post):

    # Logic to send notifications

    pass
