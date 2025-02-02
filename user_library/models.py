from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from user.models import User 
from movie.models import Movie
from serie.models import Serie

# Create your models here.
class WatchedMovie(models.Model):

    class Rating(models.IntegerChoices):
        ONE = 1, '1 - Terrible'
        TWO = 2, '2 - Very Bad'
        THREE = 3, '3 - Bad'
        FOUR = 4, '4 - Poor'
        FIVE = 5, '5 - Average'
        SIX = 6, '6 - Fair'
        SEVEN = 7, '7 - Good'
        EIGHT = 8, '8 - Very Good'
        NINE = 9, '9 - Excellent'
        TEN = 10, '10 - Masterpiece'

    class RewatchChoice(models.TextChoices):
        NEVER = "never", "Never again."
        NO = "no", "Once was enough."
        MAYBE = "maybe", "Maybe in some years."
        WORTH = "worth", "It's Worth a rewatch."
        TOP = "totally", "Must rewatch it!"

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='watched_movies')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=Rating.choices, blank=True, null=True)
    rewatch = models.CharField(choices=RewatchChoice.choices, blank=True, null=True)
    watched_at = models.DateTimeField(auto_now_add=True) # track when added to watched list.
    personal_note = models.TextField(max_length=2000, blank=True, null=True)

    class Meta:
        db_table = 'watched_movies'
        verbose_name = 'watched_movie'
        verbose_name_plural = 'watched_movies'

    def __str__(self):
        return f"{self.user.username} watched {self.movie.title}"
    


class WatchList(models.Model):

    class Status(models.TextChoices):
        PLANNED = 'plan', 'Plan to Watch'
        WATCHING = 'watching', 'Currently Watching'
        FINISHED = 'finished', 'Finished Watching'
        DROPPED = 'dropped', 'Dropped'


    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='watch_list')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
    personal_note = models.TextField(max_length=500, blank=True, null=True)
    status = models.CharField(choices=Status.choices, blank=True, null=True)


    class Meta:
        db_table = 'watch_list'
        verbose_name = 'Watch_List'
        verbose_name_plural = 'Watch_Lists'
        unique_together = ('user', 'movie')

    def __str__(self):
        return f"{self.user.username} added {self.movie.title} to watchlist"
    

class Like(models.Model):

    MOVIE = 'movie'
    SERIE = 'serie'

    CONTENT_TYPE_CHOICES = [
        (MOVIE, 'Movie'),
        (SERIE, 'Serie'),
    ]

    user = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE, related_name='liked')
    content_type = models.CharField(max_length=25, choices=CONTENT_TYPE_CHOICES)
    object_id = models.PositiveIntegerField()

    # Time stamp
    liked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "user_Like"
        unique_together = ('user', 'content_type', 'object_id')
        ordering = ['-liked_at']

    def __str__(self):
        return f"{self.user.username} liked {self.content_type} {self.object_id}"

