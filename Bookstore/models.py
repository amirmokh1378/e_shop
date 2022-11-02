# from django.db import models
# from django.db.models.deletion import CASCADE

# Create your models here.


# class Category(models.Model):
#     cat_romance = "Romance"
#     cat_fantacy = "Fantacy"
#     cat_thriller = "Thriller"
#     cat_horror = "Horror"
#     cat_crime = "Crime"
#     cat_true_story = "True Story"
#     category = models.CharField(
#         max_length=100,
#         choices=(
#             (cat_crime, cat_crime),
#             (cat_fantacy, cat_fantacy),
#             (cat_horror, cat_horror),
#             (cat_romance, cat_romance),
#             (cat_thriller, cat_thriller),
#             (cat_true_story, cat_true_story)
#         )
#     )
#
#     def __str__(self):
#         return self.category
#
#
# class Publisher(models.Model):
#     publisher_name = models.CharField(max_length=100)
#     publish_date = models.DateField
#
#     def __str__(self):
#         return self.publisher_name
#
#
# class Author(models.Model):
#     gender_male = "Male"
#     gender_female = "Female"
#     gender_other = "Other"
#     name = models.CharField(max_length=100)
#     gender = models.CharField(max_length=100,
#                               choices=(
#                                   (gender_female, gender_female),
#                                   (gender_male, gender_male),
#                                   (gender_other, gender_other)
#                               )
#                               )
#     country = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.name
#
#
# class Details(models.Model):
#     book_name = models.CharField(max_length=100)
#     category = models.ForeignKey(Category, on_delete=CASCADE)
#     pages = models.IntegerField(default=1)
#     publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
#     Author = models.ForeignKey(Author, on_delete=CASCADE)
#
#     def __str__(self):
#         return self.book_name
