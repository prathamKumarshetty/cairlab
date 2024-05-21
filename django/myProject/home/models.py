from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()

    def __str__(self):
        return self.name


class Faculty(models.Model):
    Faculty_id = models.IntegerField(primary_key=True)
    Faculty_name = models.CharField(max_length=100, default="")
    Faculty_domain = models.CharField(max_length=100, default="")
    Faculty_image = models.ImageField(upload_to="faculty/images", default="")
    Faculty_description = models.TextField(default="")
    Faculty_pass = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.Faculty_name


class Student(models.Model):
    Student_id = models.AutoField(primary_key=True)  # Automatically generates unique IDs
    Student_name = models.CharField(max_length=100, default="")
    Student_roll_no = models.CharField(max_length=20, default="")
    Student_image = models.ImageField(upload_to="students/images", default="")
    Student_phone_no = models.CharField(max_length=15, default="")
    Rid = models.BooleanField(default=False)  # True or False field

    def __str__(self):
        return self.Student_name


class Publications(models.Model):
    PUBLICATION_QUARTILE_CHOICES = [
        ('Q1', 'Q1'),
        ('Q2', 'Q2'),
        ('Q3', 'Q3'),
        ('Q4', 'Q4'),
    ]
    
    PUBLICATION_SCOPUS_CHOICES = [
        (True, 'Yes'),
        (False, 'No'),
    ]

    Publication_id = models.AutoField(primary_key=True)
    Faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    Publication_name = models.CharField(max_length=255, default="")
    Publication_scopus = models.BooleanField(choices=PUBLICATION_SCOPUS_CHOICES, default=False)
    Publication_quartile = models.CharField(max_length=2, choices=PUBLICATION_QUARTILE_CHOICES, default='Q1')
    Publication_pdf = models.FileField(upload_to="publications/pdfs", default="")

    def __str__(self):
        return f"{self.Publication_name} by {self.Faculty_id.Faculty_name}"


class RU(models.Model):
    RU_id = models.AutoField(primary_key=True)
    Student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    Faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    RU_domain = models.CharField(max_length=255, default="")
    RU_pdf = models.FileField(upload_to="ru/pdfs", default="")

    def __str__(self):
        return f"RU {self.RU_id} - {self.RU_domain} (Student: {self.Student_id.Student_name})"
