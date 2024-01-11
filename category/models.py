from django.db import models
from autoslug import AutoSlugField
import uuid
import os
import random
from django.template.defaultfilters import slugify
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.template.defaultfilters import slugify

# Create your models here.
class Category(models.Model):
    id    = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name            =   models.CharField(max_length=255,db_index=True)
    image          =   models.ImageField(upload_to='category-image', null=True, blank=True,)
    slug             =   AutoSlugField(populate_from='name',max_length=255,unique=True,null=True)
    description      =   models.TextField(blank=True,null=True)
    parent_id        =   models.ForeignKey('self', on_delete=models.SET_NULL, null=True,blank=True, related_name='category_parent')
    is_active        =   models.BooleanField(default=True)   
    created_date     =   models.DateTimeField(auto_now_add=True)
    modified_date    =   models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})


