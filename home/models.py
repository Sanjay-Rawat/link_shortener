from django.db import models
class ContactModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    contactNumber = models.IntegerField(null=True) 
    comment = models.TextField(max_length=1000)
    attachment_url = models.TextField(max_length=1000,null=True)
    class Meta:
        db_table = 'Contacts'


class UrlModel(models.Model):
    _id = models.CharField(max_length=50) 
    o_url = models.CharField(max_length=500) #original url
    created_at = models.DateTimeField()
    expire_at = models.DateTimeField(null=True)
    created_by = models.CharField(null=True,max_length=50)

    class Meta:
        db_table = 'Urls'