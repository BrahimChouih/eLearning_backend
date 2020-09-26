from django.db import models
from accounts.models import Account

# Create your models here.


def uploadImage(instance, fileName):
    if type(instance) == type(Course):
        extesion = fileName.split('.')[1]
        return 'courses/%s.%s' % (instance.id, extesion)
    else:
        extesion = fileName.split('.')[1]
        return 'categories/%s.%s' % (instance.id, extesion)


def uploadThumbnail(instance, fileName):
    extesion = fileName.split('.')[1]
    return 'videos/thumbnail/%s.%s' % (instance.id, extesion)


def uploadVideo(instance, fileName):
    extesion = fileName.split('.')[1]
    return 'Videos/video/%s.%s' % (instance.id, extesion)


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=2000, null=True)
    owner = models.ForeignKey(
        to=Account, on_delete=models.CASCADE, related_name='Course_owner')
    create_at = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(upload_to=uploadImage)
    price = models.FloatField()
    rate = models.FloatField(default=0.0)
    numReviewers = models.IntegerField(default=0)
    category = models.ForeignKey(to='Category', on_delete=models.DO_NOTHING)
    students = models.ManyToManyField(
        to=Account, related_name='Course_students')

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to=uploadVideo, null=False)
    thumbnail = models.ImageField(upload_to=uploadThumbnail, null=True)
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE)
    lessonNum = models.IntegerField(default=1)

    def __str__(self):
        return self.title+' (' + self.course.title + ') '


class Reviewer(models.Model):
    comment = models.CharField(max_length=200, null=False)
    owner = models.ForeignKey(to=Account, on_delete=models.CASCADE)
    comment_on = models.ForeignKey(to=Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment


class Rater(models.Model):
    owner = models.ForeignKey(to=Account, on_delete=models.CASCADE)
    stars = models.FloatField(default=0.0)
    rate_on = models.ForeignKey(to=Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.owner.email + ' ( ' + self.rate_on.title + ' )'

    def save(self, *args, **kwargs):
        course = self.rate_on

        if course.numReviewers == 0:
            course.rate = self.stars
        else:
            if not(course.rate == 5 and self.stars == 5):
                course.rate = (self.stars + self.rate_on.rate)/2

        course.numReviewers += 1
        course.save()
        rater = Rater(
            owner=self.owner,
            stars=self.stars,
            rate_on=self.rate_on,
        )
        super().save(*args, **kwargs)


class Category(models.Model):
    category = models.CharField(max_length=30, null=False)
    image = models.ImageField(upload_to=uploadImage)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = 'Categories'
