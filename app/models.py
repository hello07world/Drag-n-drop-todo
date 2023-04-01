from django.db import models
# import jsonfield 
# Create your models here.




class Todo(models.Model):
    class TodoChoice(models.TextChoices):
        
        DONE = "done", "done"
        DOING = "doing", "doing"
        PENDING = "pending", "pending"
        TRASH = "trash", "trash"
        
        
    todo=models.CharField(max_length=100 , null=True , blank=True)
    status = models.CharField(max_length=25 ,choices=TodoChoice.choices, default=TodoChoice.PENDING)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.todo

