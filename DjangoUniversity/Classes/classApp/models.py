from django.db import models

# Each instance represents one university class stored in the database.
class UniversityClasses(models.Model):
    title = models.CharField(max_length=80)
    courseNumber = models.IntegerField()
    instructor = models.CharField(max_length=80)
    duration = models.FloatField()

    # Provides database queries such as UniversityClasses.objects.all().
    objects = models.Manager()

    class Meta:
        # Sets the plural label displayed in the Django admin.
        verbose_name_plural = 'Universities Classes'


    def __str__(self):
        # Identifies the class by its title and instructor in admin lists.
        return f"{self.title}: {self.instructor}"
