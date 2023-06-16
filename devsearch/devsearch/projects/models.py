from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    feature_image = models.ImageField(blank=True, null=True, upload_to='projects/%Y/%m/%d', default='default.jpg')
    demo_link = models.CharField(max_length=200, blank=True, null=True)
    source_link = models.CharField(max_length=200, blank=True, null=True)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0)
    vote_ratio = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
