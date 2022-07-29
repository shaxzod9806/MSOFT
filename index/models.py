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
        ('short_term', 'short_term'),
        ('long_term', 'long_term'),
    )

    title = models.ForeignKey(Title, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE, null=True, blank=True)
    work_experience = models.ForeignKey(Work_experience, on_delete=models.CASCADE)
    spoken_languages = models.ForeignKey(Language, on_delete=models.CASCADE, null=True, blank=True)
    citizenship = models.ForeignKey(Citezenship, on_delete=models.CASCADE, null=True, blank=True)
    prefer_project_duration = models.CharField(max_length=10, choices=PPD_CHOICES, default='short_term', null=True,
                                               blank=True)
    cv_file = models.FileField(upload_to='media/cv_files/', null=True, blank=True)
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

        # ordering = ['-created_at']  # -created_at means descending order
        # ordering = ['-created_at']  # -created_at means descending order
