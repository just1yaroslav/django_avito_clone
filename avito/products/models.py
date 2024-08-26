from django.db import models
from users.models import UserCustomModel


class ProductModel(models.Model):
    class ProductCategory(models.TextChoices):
        CAR = "Car"
        COMPUTER = "Computer"
        LAPTOP = "Laptop"
        PHONE = "Phone"
        HOUSE = "House"
        OTHER = "Other"

    class ProductStatus(models.TextChoices):
        PUBLISHED = "PB", "Published"
        DRAFT = "DR", "Draft"

    status = models.CharField(
        max_length=10,
        choices=ProductStatus.choices,
        default=ProductStatus.DRAFT,
        verbose_name='Status'
    )
    category = models.CharField(
        max_length=10,
        choices=ProductCategory.choices,
        default=ProductCategory.OTHER,
        verbose_name='Category'
    )
    author = models.ForeignKey(
        UserCustomModel,
        on_delete=models.CASCADE,
        verbose_name='Author'
    )
    title = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        default='title product',
        verbose_name='Title'
    )
    slug = models.SlugField(
        max_length=100,
        blank=False,
        null=False,
        verbose_name='Slug'
    )
    low_description = models.TextField(
        blank=True,
        null=True,
        default='product description',
        verbose_name='Description (low)'
    )
    full_description = models.TextField(
        blank=True,
        null=True,
        default='product full description',
        verbose_name='Description (full)'
    )
    product_image_cover = models.ImageField(
        upload_to='products/%Y/%m/%d/',
        blank=True,
        null=True,
        verbose_name='Image product cover'
    )
    product_images = models.ImageField(
        upload_to='products/%Y/%m/%d/',
        blank=True,
        null=True,
        verbose_name='Images product'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name='Price'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    def __str__(self):
        return f'id: {self.id} info: {self.category} {self.status} author: {self.author} | product: {self.title} {self.price}руб'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-price']
        