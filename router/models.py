from django.db import models

class RouterDetails(models.Model):  
    sapid = models.CharField(max_length=18,blank=False,null=False)  
    loopback = models.CharField(max_length=15,blank=False,null=False)  
    hostname = models.CharField(max_length=15,blank=False,null=False)
    mac_address = models.CharField(max_length=17,blank=False,null=False)
    status = models.BooleanField(default=True,blank=False,null=False)  
    class Meta:  
        db_table = "router_details"
        unique_together = ['loopback','hostname'] 
