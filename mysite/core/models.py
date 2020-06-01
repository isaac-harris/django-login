from django.db import models
import datetime
import os

# Customer Model
class Customers(models.Model):
    customerName = models.CharField(max_length = 64)
    customerDOB = models.DateField(max_length=8)
    customerPhone = models.CharField(max_length = 64)
    customerEmail = models.CharField(max_length = 64)
    customerAddress = models.CharField(max_length = 64)

    
    def __str__(self):
        #makes it expandible 
        lastId = len(Customers.objects.all())
        toReturn = ""
        
        #start the text with a header and <ul>
        if int(self.id) == 1:
            toReturn += "<h1>Customer Database</h1><ul><li>" + self.customerName + ", " + str(self.customerDOB) + ", " + self.customerPhone + ", " + self.customerEmail + ", " + self.customerAddress + "</li>"
        
        #end the text with </ul>
        elif int(self.id) == lastId:
            toReturn += "<li>" + self.customerName + ", " + str(self.customerDOB) + ", " + self.customerPhone + ", " + self.customerEmail + ", " + self.customerAddress + "</li></ul>"
        
        #as with the past 2 conditions, also add the element to the bulletpoint list
        else:
            toReturn += "<li>" + self.customerName + ", " + str(self.customerDOB) + ", " + self.customerPhone + ", " + self.customerEmail + ", " + self.customerAddress + "</li>"
        
        return (toReturn)