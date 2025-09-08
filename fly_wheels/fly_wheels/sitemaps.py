from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from products.models import Product

class ProductSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Product.objects.all()

    def location(self, obj):
        
        return reverse("product_detail", kwargs={"slug": obj.slug})

    def lastmod(self, obj):
        return getattr(obj, "updated_at", None) or getattr(obj, "created", None)

class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        return Category.objects.all()

    def location(self, obj):
        return reverse("category_detail", kwargs={"slug": obj.slug})

class StaticSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return ["home", "shop", "contact"]

    def location(self, item):
        return reverse(item)
