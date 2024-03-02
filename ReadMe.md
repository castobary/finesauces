# FineSources Project

+ First ecommence project

## Models

“Let’s go over our models and their attributes:


**name**
 - this attribute will be responsible for preserving titles of categories and products that we create. This field is set to be a `CharField` , since we want it to store text value, which then translates into a VARCHAR  value in our database. The maximum character count is set to 100.

**slug**
 - This is a field intended to be used in URLs. A slug is a short label that contains only letters, numbers, underscores, or hyphens. We will use the slug field to build beautiful, SEO-friendly URLS for our e-commerce listings. Both, name and slug fields, are set to be unique, meaning Django will prevent multiple categories having the same name and slug fields.

**category**
 - This field defines a **many-to-one** relationship, meaning that each product belongs to a specific category, and the category can contain any number of products. To keep track of the relationship between `Category` and `Product` models, Django will actually create extra column in the Product table to store the `Category` id, under which a specific product belongs. This extra category id column makes it easy to, for example, retrieve all of the products for “a specific Category. As for related_name parameter, Django has a built-in syntax we can use, known as FOO_set, where FOO is a lowercased source model name. So, for our Category model, we can use category_set syntax to access all related Product instances. related_name parameter is entirely optional, but I prefer adding it to models, which then allows us to set the name of this reverse relationship explicitly.

**image**
 
 - The image file. By default, images will be uploaded to the products
 folder.

description
 - Field for storing product description. We are using TextField
 here instead of CharField, since we do not want to limit the description's length.

shu
 - Scoville Heat Units (SHU) - since we will be selling hot sauces, we need a field to indicate, how hot the sauce is.

price
 - this field uses Python’s decimal.Decimal type to store a fixed precision decimal number. The maximum number of digits (including the decimal places) is “set using the max_digits attribute and decimal places with decimal_places attribute. We use DecimalField
 instead of FloatField to avoid rounding issues.

available
 - A Boolean value to indicate whether the product is available or not. If no value (True/False)
 is specified, a database record is created with the default value specified (True).”

## `Meta` class
 
 + model metadata is “anything that’s not a field”. Note that adding Meta
 class to our models is optional.”

## `Pillow` Library

+ Used to deal with images


# admin site customizations

<code>
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display =('name', 'category', 'slug', 'price', 'available')
    list_filter = ('category', 'available')
    list_editable = ('price', 'available')
    prepopulated_fields = {'slug': ('name',)}
</code>


We added a couple of new attributes here. list_filter  will enable us to filter products by their category and availability. When we create some products, you will notice a sidebar in the Products section very similar to the one in Users. We will use the list_editable attribute to set the fields that can be edited from the administration site's display page. This will allow us to edit “multiple rows at once. Any field in list_editable must also be present in the  list_display attribute since only the displayed fields can be edited.
While we are in the admin site, let’s add one more category to the portfolio (I will go with Extreme. Notice how the slug field is being filled in automatically).


## Django Template Language (DTL)


“Django also comes with its own template system called Django template language (DTL), which enables us to customize, how the template is presented. It comes with four constructs:


+ `{{variables}}` - allow us to render a value from the context
 . They are surrounded by `{{ and }}`


+ `tags` - provide arbitrary logic in the rendering process. They most often serve as a control structure in shape of “if”
 statement or a “for” loop. Tags are surrounded by {%
 and %}


+ `filters` - transform the values of variables and tag arguments. They are surrounded by `{{ and }}` and come after variable we want to transform, separated by | (e.g. `{{ review.created|date}}`). They can also take arguments: `{{ review.created|date:"Y-m-d"}}`

+ `comments` - look like this: {# this won't be rendered #}. A `{% comment %}` tag provides multi-line comments and has to be concluded by `{% endcomment %}`





