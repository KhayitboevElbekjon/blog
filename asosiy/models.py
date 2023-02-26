from django.db import models
class Maqola(models.Model):
    sarlavha=models.CharField(max_length=50)
    sana=models.DateField()
    matn=models.TextField()
    rasm=models.FileField()
    def __str__(self):
        return f"{self.sarlavha}"

class Intervyu(models.Model):
    sarlavha=models.CharField(max_length=50)
    sana=models.DateField()
    video_url=models.TextField()
    def __str__(self):
        return f"{self.sarlavha}"

