# Example of inefficient database queries in a loop


def list_blog_posts(user):

    posts = []

    for post in BlogPost.objects.all():

        if post.author == user:

            posts.append(post)

    return posts
