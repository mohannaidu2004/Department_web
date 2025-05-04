from django.db import models
from django.core.validators import FileExtensionValidator
from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # ... other fields

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='news/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Staff(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    qualification = models.TextField()
    profile_picture = models.ImageField(upload_to='staff/')
    email = models.EmailField(blank=True, null=True)
    join_date = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

class Timetable(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(
        upload_to='timetables/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])]
    )
    upload_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class GalleryImage(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/')
    upload_date = models.DateTimeField(auto_now_add=True)
    event_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    submission_date = models.DateTimeField(auto_now_add=True)
    is_responded = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.subject}"

class EmailSubscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email

class EmailConfig(models.Model):
    email_host = models.CharField(max_length=100)
    email_port = models.PositiveIntegerField()
    email_username = models.CharField(max_length=100)
    email_password = models.CharField(max_length=100)
    email_use_tls = models.BooleanField(default=True)
    email_use_ssl = models.BooleanField(default=False)
    default_from_email = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        # Ensure only one instance exists
        self.__class__.objects.exclude(id=self.id).delete()
        super().save(*args, **kwargs)

    def __str__(self):
        return "Email Configuration"