from django.db import models

# Create your models here.

class DAXExpressionModel(models.Model):
    expression_text = models.TextField()  # store the original DAX expression
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # When we print the object, show an excerpt of the expression or a generic ID
        return f"DAXExpressionModel(id={self.id}, created_at={self.created_at})"
