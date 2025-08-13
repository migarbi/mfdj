from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=50)
    image = models.ImageField(upload_to='media/')
    place = models.IntegerField()

    def __str__(self):
        return f"{self.title}, {self.description}"

    class Meta:
        pass


class Photo(models.Model):
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name='photos')
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.TextField(max_length=50)
    image = models.ImageField(upload_to='photos/')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}, {self.category.title}"


class ExtraPhoto(models.Model):
    category = models.ForeignKey(Photo,
                                 on_delete=models.CASCADE,
                                 related_name='extra_photos')
    image = models.ImageField(upload_to='photos/')
    def __str__(self):
        return f"Доп фото {self.photo.title}"

class User(models.Model):
    pass