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
        Account, on_delete=models.CASCADE, related_name='Course_owner')
    create_at = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(upload_to=uploadImage)
    price = models.FloatField()
    rate = models.FloatField(default=0.0)
    numReviewers = models.IntegerField(default=0)
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING)
    students = models.ManyToManyField(
        Account, related_name='Course_students', blank=True)

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
    rate = models.ForeignKey('Rater', on_delete=models.PROTECT, null=True)

    def save(self, *args, **kwargs):
        try:
            self.rate = Rater.objects.get(owner=self.owner)
        except:
            print('ther is not rate from you no this course')

        super().save(*args, **kwargs)

    def __str__(self):
        return self.owner.email + ' ( ' + self.comment_on.title + ' )'


class Rater(models.Model):
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)
    stars = models.FloatField(default=0.0)
    rate_on = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.owner.email + ' ( ' + self.rate_on.title + ' )'

    def save(self, *args, **kwargs):
        course = self.rate_on
        course.numReviewers += 1
        raters = Rater.objects.filter(rate_on=course).values()
        sumStars = 0
        for stars in raters:
            sumStars += stars['stars']
        sumStars += self.stars
        course.rate = sumStars / course.numReviewers
        course.save()

        super().save(*args, **kwargs)


class Category(models.Model):
    category = models.CharField(max_length=30, null=False)
    image = models.ImageField(upload_to=uploadImage)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = 'Categories'
