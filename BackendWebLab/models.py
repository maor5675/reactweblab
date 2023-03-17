from django.db import models

# Phonebrand table represents all the popular phone brands in israel and give us the option to illustrate the web with brand pics 

class Phonebrand(models.Model):
   brand = models.CharField(max_length=100, null=False)
   logo = models.ImageField(null=True, blank=True)
   
   def __str__(self):
      return self.brand

# Phonetype table represents all the popular phone types in israel connected to specific brand and give us the option to illustrate the web with gadget pics 

class Phonetype(models.Model):
   brand = models.ForeignKey(Phonebrand,on_delete=models.CASCADE)
   type = models.CharField(max_length=100, null=False)
   image =  models.ImageField(null=True, blank=True)

   def __str__(self):
      return self.brand.brand +","+  self.type

# represents the popular phone by phone type and brand make the serch more easy to execute 

class Phone(models.Model):
   type= models.ForeignKey(Phonetype,on_delete=models.CASCADE)
   device = models.CharField(max_length=100, null=False)

   def __str__(self):
      return self.device +","+  self.type.type

# here the web owner insert the popular Malfunction types he can ofer

class Malfunction_type(models.Model):
   Malfunction = models.CharField(max_length=100)

   def __str__(self):
      return self.Malfunction

class Price(models.Model):
   phone_device = models.ForeignKey(Phone,on_delete=models.CASCADE)
   Malfunction_type= models.ForeignKey(Malfunction_type,on_delete=models.CASCADE)
   price = models.PositiveIntegerField(null= True, blank = True)

   def __str__(self):
      return self.Malfunction_type.Malfunction +','+self.phone_device.device