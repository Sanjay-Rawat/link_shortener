from django.db import models
class ContactModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    contactNumber = models.IntegerField(null=True)
    comment = models.TextField(max_length=1000)
  
    class Meta:
        db_table = 'Contacts'