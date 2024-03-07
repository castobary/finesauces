from django.contrib import admin
from .models import Category, Product, Review


# Register your models here.
#admin.site.register(Category)

# customized style

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}  # have slug field filled from name



class OrderReviewInline(admin.TabularInline):
    model = Review
    extra = 0


#admin.site.register(Product)
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display =('name', 'category', 'slug', 'price', 'available')
    list_filter = ('category', 'available')
    list_editable = ('price', 'available')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [OrderReviewInline]




