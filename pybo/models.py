from django.db import models

class QRcode(models.Model):
    qrname = models.CharField(max_length=6, blank=True)
    code = models.ImageField(upload_to='qr', blank=True, null=True)
    class Meta:
        verbose_name_plural = "QR CODES"

    def __str__(self):
            return 'QR= %s' % (self.qrname)

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()