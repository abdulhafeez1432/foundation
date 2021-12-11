from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db.models.fields import BooleanField, DateField, PositiveBigIntegerField, TextField
from django.db.models.fields.related import OneToOneField
from django.urls import reverse



class User(AbstractUser):
    is_subadmin = models.BooleanField('Sub Admin User', default=False)
    is_applicant = models.BooleanField('Applicant Users', default=False)

# Create your models here.
class PersonalDetails(models.Model):


    STATE = (
        ('1', 'ABIA'),
        ('2', 'ADAMAWA')
    )

    EDUCATION =(
        ('1', 'PRIMARY SCHOOL'), 
        ('2', 'SCHOOL LEAVING CERTICATE')
    )


    RELIGION =(
        ('1', 'ISLAM'), 
        ('2', 'CHRISTAINITY')
    )
   
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length = 250, null=True)
    dob = models.DateField("Date of Birth", null=True)
    place_of_birth = models.CharField(max_length = 150,null=True)
    state = models.CharField(max_length=1, choices=STATE, default='ABIA')
    education = models.CharField(max_length=1, choices=EDUCATION, default='SCHOOL LEAVING CERTICATE')
    religion = models.CharField(max_length=1, choices=RELIGION, default='ISLAM')
    attend = models.CharField('Which Masjeed or Church do You Attend', max_length=250, blank=True, null=True)
    phone_number = models.PositiveIntegerField()
    passport = models.ImageField("Passport Photography", upload_to='applicant', null=True)
    create_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)



    class Meta:
        verbose_name = "PersonalDetails"
        verbose_name_plural = "PersonalDetailss"

    def __str__(self):
        return f'Username: {self.user.username} - Fullname {self.user.get_full_name} '

    def get_absolute_url(self):
        return reverse("PersonalDetails_detail", kwargs={"pk": self.pk})


class FamilyDetails(models.Model):

    MARITAL = (
        ('1', 'Married'),
        ('2', 'Divorced'),
        ('3', 'Widowed')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    marital = models.CharField("What is Your Marital Status", max_length=1, choices=MARITAL)
    spouse = models.CharField("Spouse Name", max_length=50)
    spouse_employment = BooleanField("Does Your Spouse Employeed")
    employee_address = models.CharField("Spouse Employee Address", max_length=250)
    phone = PositiveBigIntegerField("Spouse PhoneNumber")
    job = models.CharField('Job Title', max_length=50)
    kids = PositiveBigIntegerField("No of Children")
    create_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)





    

    class Meta:
        verbose_name = "FamilyDetails"
        verbose_name_plural = "FamilyDetailss"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("FamilyDetails_detail", kwargs={"pk": self.pk})



class EmployentDetails(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.BooleanField("Are you Current Employed", default=False)
    company = models.CharField(max_length = 150)
    since = models.DateField("Since When")
    title = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    create_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


    class Meta:
        verbose_name = "EmployentDetails"
        verbose_name_plural = "EmployentDetailss"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("EmployentDetails_detail", kwargs={"pk": self.pk})

    

    
    
    
class SkilsDetails(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skill = models.BooleanField("Are you Skilled", default=False)
    skill_details = TextField("More Details About Your Skill")
    vocation = models.BooleanField("Do You Have any Vocational Traning", default=False)
    vocational_details = models.TextField("More Details About Your Vocation Course")
    vocation_info = models.TextField("More Info About Who train You and the Address")
    create_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "SkilsDetails"
        verbose_name_plural = "SkilsDetailss"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("SkilsDetails_detail", kwargs={"pk": self.pk})


    

class Assistance(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    assistance = models.BooleanField("Have You Recieved Assistance from us before", default=False)
    theAssistance = TextField("Kindly Give information About the Assistance")
    similar = models.BooleanField("Have You Recieved Similar Assistance from else where", default=False)
    theSimilar = TextField('Kindly Give details of the Assistance')
    since = models.DateField("Since When")
    title = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    create_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    

    class Meta:
        verbose_name = "Assistance"
        verbose_name_plural = "Assistances"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Assistance_detail", kwargs={"pk": self.pk})



class NeedDatails(models.Model):

    NEEDS = (
        ('1', 'SUBMITTED'),
        ('2', 'UNDER-PROCESS'),
        ('3', 'APPROVED'),
        ('4', 'COMPLETED')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    needs = TextField("Eplain The Extract Nature of Your Need")
    status = models.CharField(max_length = 1, choices=NEEDS, default='SUBMITTED')
    when_complete = DateField()
    value = TextField("What given to The Needy", blank=True)
    create_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    

    class Meta:
        verbose_name = "NeedDatails"
        verbose_name_plural = "NeedDatailss"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("NeedDatails_detail", kwargs={"pk": self.pk})



class RefereesDetails(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 150)
    phone = PositiveBigIntegerField()
    relationship = models.CharField(max_length=50)
    create_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
 
    class Meta:
        verbose_name = "RefereesDetails"
        verbose_name_plural = "RefereesDetailss"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("RefereesDetails_detail", kwargs={"pk": self.pk})
