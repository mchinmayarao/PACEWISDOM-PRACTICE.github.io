from django.shortcuts import render
from .forms import EmailPreferenceForm
from .models import EmailPreference

def home(request):
    """
Handles the display and processing of the email subscription form on the homepage.

If the request method is POST, the function processes the submitted form data to either create or update the user's email preferences in the database. If the form submission is successful, it renders the homepage with a success message. For GET requests, it simply renders the homepage with an empty form.

Args:
    request (HttpRequest): The HTTP request object containing metadata about the request.

Returns:
    HttpResponse: The rendered homepage with the form and optional success message.

Process:
    1. If the request method is POST:
        a. Validates the submitted form data.
        b. Updates or creates the `EmailPreference` entry with the provided email and cuisine preferences.
        c. Renders the homepage with a success message and a new empty form.
    2. If the request method is GET:
        a. Renders the homepage with an empty form.
"""

    if request.method == 'POST':
        form = EmailPreferenceForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            cuisines = form.cleaned_data['cuisines']

            EmailPreference.objects.update_or_create(
                user_email=email,
                defaults={
                    'recipe_preferences': cuisines,
                }
            )

            form = EmailPreferenceForm()
            return render(request, 'home.html', {'form': form, 'subscription_success': True})
    else:
        form = EmailPreferenceForm()
    
    return render(request, 'home.html', {'form': form})


