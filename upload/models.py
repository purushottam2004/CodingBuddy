from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class test(models.Model):
    question_name = models.CharField(max_length=50)
    question_zip = models.FileField(upload_to='files/', blank=True)
    for_student = models.ForeignKey(student, on_delete=models.CASCADE)
    issolved = models.BooleanField(default=False)
    def __str__(self):
        return self.question_name

class ans(models.Model):
    answer_name = models.CharField(max_length=50)
    answer_zip = models.FileField(upload_to='files/', blank=True)
    for_question = models.ForeignKey(test, on_delete=models.CASCADE)
    for_student = models.ForeignKey(student, on_delete=models.CASCADE)
    def __str__(self):
        return self.answer_name
