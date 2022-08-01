import django
from django.db import models


class Title(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Sector(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Work_experience(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Citezenship(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Expert(models.Model):
    PPD_CHOICES = (
        ('Short term', 'short_term'),
        ('Long term', 'long_term'),
    )
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=20, unique=True)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    work_experience = models.ForeignKey(Work_experience, on_delete=models.CASCADE)
    spoken_languages = models.ForeignKey(Language, on_delete=models.CASCADE)
    citizenship = models.ForeignKey(Citezenship, on_delete=models.CASCADE)
    prefer_project_duration = models.CharField(max_length=10, choices=PPD_CHOICES)
    cv_file = models.FileField(upload_to='media/cv_files/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        try:
            return self.first_name + ' ' + self.last_name
        except:
            return 'No name'

    class Meta:
        verbose_name = 'Expert'
        verbose_name_plural = 'Experts'
