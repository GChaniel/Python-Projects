from django.db import models

# Each instance represents one university campus stored in the database.
class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=80)
    # Stores a short state code, with room for up to two characters.
    state = models.CharField(max_length=2)
    campus_id = models.IntegerField()

    # Provides database queries such as UniversityCampus.objects.all().
    objects = models.Manager()

    class Meta:
        # Sets the plural label displayed in the Django admin.
        verbose_name_plural = 'University Campus'


    def __str__(self):
        # Identifies the campus by its name and state in admin lists.
        return f"{self.campus_name}: {self.state}"
