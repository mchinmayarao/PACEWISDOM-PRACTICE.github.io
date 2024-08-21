from django.core.mail import send_mail
from DailyRecipe import settings
from .recipe_generator import get_recipe
from .models import EmailPreference

def send_emails():

    """
Sends daily recipe emails to users based on their selected cuisine preferences.

The function retrieves all email preferences from the database, generates a recipe for a randomly selected cuisine, and sends an email to each user.

Args:
    None

Returns:
    None

Process:
    1. Retrieves all email preferences from the `EmailPreference` model.
    2. Splits and cleans the stored cuisine preferences for each user.
    3. Calls `get_recipe()` to generate a recipe for a randomly selected cuisine.
    4. Constructs and sends an email containing the selected cuisine and recipe to each user.

Raises:
    Any exceptions related to email sending will be raised by the `send_mail` function.
"""


    email_preferences = EmailPreference.objects.all()

    for email_preference in email_preferences:
        email = email_preference.user_email
        cuisines = email_preference.recipe_preferences.split(',')  # Split preferences into a list
        cuisines = [cuisine.strip() for cuisine in cuisines if cuisine.strip()]  # Clean up the list

        if not cuisines:
            continue

        recipe, selected_cuisine = get_recipe(cuisines)
        
        message = f"""
        Hi there,

        Here is your daily recipe update!

        Cuisine: {selected_cuisine}
        Recipe: {recipe}
        
        
        
        Enjoy your cooking!

        Best regards,
        Your Recipe Team
        """
    
    # Send the email
    send_mail(
        'Your Daily Recipe Update',
        message,
        settings.DEFAULT_FROM_EMAIL,
        [email],
        fail_silently=False,
    )
