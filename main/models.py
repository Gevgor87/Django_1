from django.db import models

# Create your models here.

class Base(models.Model):
    title = models.CharField("title", max_length=200)
    logo_img = models.ImageField("Logo", upload_to="images")

    def __str__(self) -> str:
        return self.title


class Category(models.Model):
    title = models.CharField("title", max_length=100)

    def __str__(self) -> str:
        return self.title
    
class Button_1(models.Model):
    text1 = models.CharField("text1", max_length=200)
    text2 = models.CharField("text2", max_length=200)
    text3 = models.CharField("text3", max_length=200)
    p1 = models.CharField("p1", max_length=100)
    p2 = models.CharField("p2", max_length=100)
    p3 = models.CharField("p3", max_length=100)
    p4 = models.CharField("p4", max_length=100)
    p5 = models.CharField("p5", max_length=100)
    button = models.CharField("button", max_length=50)
    img = models.ImageField("image", upload_to="images")

    def __str__(self) -> str:
        return self.text1

class Button_2(models.Model):
    text1 = models.CharField("text1", max_length=200)
    text2 = models.CharField("text2", max_length=200)
    p1 = models.CharField("p1", max_length=200)
    p2 = models.CharField("p2", max_length=200)
    p3 = models.CharField("p3", max_length=200)
    p4 = models.CharField("p4", max_length=200)
    p5 = models.CharField("p5", max_length=200)
    p6 = models.CharField("p6", max_length=200)
    img = models.ImageField("image", upload_to="images")

    def __str__(self) -> str:
        return self.text1

class Button_3(models.Model):
    text1 = models.CharField("text1", max_length=200)
    icon = models.ImageField("icon", upload_to="images")
    image_sm = models.ImageField("Image sm", upload_to="images")
    image_big = models.ImageField("Image big", upload_to="images")


    def __str__(self) -> str:
        return self.text1
    
class Button_4(models.Model):
    title = models.CharField("title", max_length=50)
    text1 = models.TextField("text 1")
    text2 = models.TextField("text 2")
    address1 = models.CharField("Address 1", max_length=100)
    address2 = models.CharField("Address 2", max_length=100)
    button = models.CharField("button", max_length=20)

    def __str__(self) -> str:
        return self.title

class Footer(models.Model):
    text1 = models.CharField("text", max_length=60)
    text2 = models.CharField("text", max_length=60)
    link = models.URLField('url')
    link_name = models.CharField("link name", max_length=100)

class Contack(models.Model):
    name = models.CharField("Name", max_length=50)
    email = models.EmailField("Email")
    message = models.TextField("Message")

    def __str__(self) -> str:
        return self.name