from django.db import models, connection

# Create your models here.

class Staff(models.Model):
    staffno = models.CharField(max_length=50,primary_key=True)

    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    sex = models.CharField(max_length=50)
    dob = models.DateField()
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    branchno = models.ForeignKey('Branch', models.DO_NOTHING, db_column='branchno')
    telephone = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    
    def hire_staff(self, staffno, fname, lname, position,sex, dob, salary, branchno, telephone, mobile, email):
        print(dob)
        with connection.cursor() as cursor:
            cursor.callproc('staff_hire_sp', [staffno, fname, lname, position, sex, dob, salary, branchno, telephone, mobile, email])
        
    
    def update_staff(self, staffno, salary, telephone, mobile, email):
        with connection.cursor() as cursor:
            cursor.callproc('update_staff_sp', [staffno, salary, telephone, mobile, email])     

    class Meta:
        db_table = 'DH_STAFF'


class Branch(models.Model):
    branchno = models.AutoField(primary_key=True)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    postcode = models.CharField(max_length=50)

    class Meta:
        db_table = 'DH_BRANCH'



class Client(models.Model):
    clientno = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    telno = models.CharField(max_length=20)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    preftype = models.CharField(max_length=50)
    maxrent = models.DecimalField(max_digits=8, decimal_places=2)

    def register_client(self, clientno, fname, lname, telno, street, city, email, preftype, maxrent):
        with connection.cursor() as cursor:
            cursor.callproc('register_client_sp', [clientno, fname, lname, telno, street, city, email, preftype, maxrent])

    class Meta:
        db_table = 'DH_CLIENT'

