from django.db import models

class About(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    intro = models.TextField()

    def __str__(self):
        return self.fname

class Experience(models.Model):
    profile = models.CharField(max_length=50)
    organisation = models.CharField(max_length=50)
    summary = models.TextField()
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50)

    def __str__(self):
        return self.profile

class Education(models.Model):
    institute = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    specialization = models.CharField(default = '', max_length=50)
    score = models.CharField(max_length=50)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50)

    def __str__(self):
        return self.institute

class Tool(models.Model):
    name = models.CharField(max_length=50)
    f_link = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=20)
    detail = models.CharField(max_length=70)

    def __str__(self):
        return self.name

class Interest(models.Model):
    int = models.TextField()

    def __str__(self):
        return self.int

class Award(models.Model):
    description = models.TextField(default='some award')

    def __str__(self):
        return self.description
