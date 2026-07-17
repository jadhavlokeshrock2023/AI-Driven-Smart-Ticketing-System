from django.db import models



class KnowledgeArticle(models.Model):


    title = models.CharField(
        max_length=200
    )


    problem = models.TextField()


    solution = models.TextField()


    category = models.CharField(
        max_length=50,
        default="general"
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )



    def __str__(self):

        return self.title