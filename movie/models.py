from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.template import defaultfilters


class Movie(models.Model):
    CATEGORY_CHOICES = (
        ('comedy', 'Comedy'),
        ('horror', 'Horror'),
        ('thriller', 'Thriller'),
        ('romantic', 'Romantic'),
        ('sfx', 'Science Fiction')
    )

    class Meta:
        verbose_name = 'movie'
        verbose_name_plural = 'movies'
        ordering = ['stars']

    title = models.CharField(
        max_length=100,
        verbose_name='title',
    )

    director = models.CharField(
        max_length=100,
        verbose_name='director',
    )

    writer = models.CharField(
        max_length=100,
        verbose_name='writer',
    )

    stars = models.PositiveSmallIntegerField(
        verbose_name='stars',
    )

    summary = models.TextField(
        verbose_name='summary',
    )

    year = models.CharField(
        max_length=4,
        default=timezone.now().year,
        verbose_name='year',
    )

    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES,
        verbose_name='category',
    )

    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name='created At',
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='updated At',
    )

    deleted = models.BooleanField(
        default=False,
        verbose_name='deleted',
    )

    deleted_at = models.DateTimeField(
        null=True,
        verbose_name='deleted At',
    )

    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='registered_by',
        verbose_name='registered by',
    )

    slug = models.SlugField(
        unique=True,
    )

    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.title)
        super().save(*args, **kwargs)

    def soft_delete(self):
        self.deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return "{}/{}".format(self.title, self.year)
