from django.db import models

class EmailPreference(models.Model):
    """
EmailPreference is a Django model that stores a user's email address and their selected recipe preferences.

Attributes:
    user_email (models.EmailField): A unique field for storing the user's email address.
    recipe_preferences (models.TextField): A field for storing the user's selected cuisines as a comma-separated list.

Methods:
    __str__(): Returns the user's email address as the string representation of the model.
"""

    user_email = models.EmailField(unique=True)
    recipe_preferences = models.TextField(help_text="Comma-separated list of selected cuisines")

    def __str__(self):
        return self.user_email