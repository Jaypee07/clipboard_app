from django.db import models

class Snippet(models.Model):
    # The actual text you copied (TextField handles long strings)
    content = models.TextField()
    
    # Automatically stamps the exact time it was saved
    created_at = models.DateTimeField(auto_now_add=True)
    
    # The toggle to prevent auto-deletion
    keep_permanently = models.BooleanField(default=False)

    # This just makes it readable in the admin dashboard later
    def __str__(self):
        return self.content[:50]