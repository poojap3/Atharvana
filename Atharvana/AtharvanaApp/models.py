
#AtharvanaApp
#pass= 12345


from django.db import models

class TaskValue(models.Model):
    mm=models.CharField(max_length=50, null=True, blank=True)
    s1=models.CharField(max_length=50, null=True, blank=True)
    s2=models.CharField(max_length=50, null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True,verbose_name="created",blank=True,null=True)
