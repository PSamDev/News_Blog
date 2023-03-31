from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to="images/", height_field=None, width_field=None, max_length=None)
    
    
    class Meta:
        verbose_name = "Category"        
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.title
    
class News(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    thumbnail = models.ImageField(upload_to="images/", height_field=None, width_field=None, max_length=None)
    content = models.TextField()
    post_time = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "News"        
        verbose_name_plural = "News"
    
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    comment = models.TextField()
    comment_time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = "Comment"        
        verbose_name_plural = "Comments"
    
    
    def __str__(self):
        return self.comment
    
class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    number = models.CharField(max_length=20)
    message = models.TextField()
    
    class Meta:
        verbose_name = "Message"        
        verbose_name_plural = "Messages"
        
    def __str__(self):
        return self.name