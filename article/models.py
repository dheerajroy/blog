from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy
from django.contrib.auth.models import User
from django.utils.text import slugify

class Article(models.Model):
    def validate_cover_extension(value):
        if not (value.name.rsplit('.')[1] in ['png', 'jpg', 'jpeg']):
            raise ValidationError(gettext_lazy(f'Only .png, .jpg, .jpeg files are allowed. {value.name} is not a valid file.'), params={'value': value})

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='covers', validators=[validate_cover_extension])
    title = models.CharField(max_length=150)
    content = models.TextField(max_length=6000)
    slug = models.SlugField(unique=True, blank=True, null=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(args, kwargs)

    def __str__(self):
        return f'{self.posted_at} | {self.author} | {self.title}'
