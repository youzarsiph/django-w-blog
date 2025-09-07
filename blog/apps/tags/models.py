"""Data Models for blog.apps.tags"""

from django.db import models
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase


# Create your models here.
class Tag(TaggedItemBase):
    """Through model for defining m2m rel between Articles and Tags"""

    content_object = ParentalKey(
        "blog_articles.BlogArticle",
        related_name="tagged_items",
        on_delete=models.CASCADE,
    )
