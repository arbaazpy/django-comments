from django.db import models


class User(models.Model):
    """
    A person who uses the website
    """

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Thread(models.Model):
    """
    A comment thread
    """

    title = models.CharField(max_length=255)
    creator = models.ForeignKey(
        User,
        related_name='threads',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    A comment by a user on a thread
    """

    text = models.CharField(max_length=255)
    user = models.ForeignKey(
        User,
        related_name="comments",
        on_delete=models.CASCADE
    )
    thread = models.ForeignKey(
        Thread,
        related_name="comments",
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return f"{self.user.name} - {self.thread.title}"


class Club(models.Model):
    """
    A group of users
    """

    text = models.CharField(max_length=255)
    user = models.ManyToManyField(User, related_name="clubs")

    def __str__(self):
        return self.text
