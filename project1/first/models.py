from django.db import models  
class Employee(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15) 
    manager=models.CharField(max_length=100) 
    
    
class Department(models.Model):  
    did = models.CharField(max_length=20)  
    dname = models.CharField(max_length=100) 
    manager = models.OneToOneField(Employee,on_delete=models.SET_NULL,null=True)
        
        
  
    
   
    
     


    
    