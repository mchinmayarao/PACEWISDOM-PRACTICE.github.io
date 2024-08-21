from django import forms

class EmailPreferenceForm(forms.Form):
    """
EmailPreferenceForm is a form that allows users to register their email addresses and select their preferred cuisines from a list of Indian cuisines.

Attributes:
    email (forms.EmailField): A required field for the user's email address.
    cuisines (forms.MultipleChoiceField): A required field that allows users to select multiple cuisines from a list, using checkboxes.

Methods:
    clean_cuisines(): Processes and returns the selected cuisines as a comma-separated string.

    """
    
    email = forms.EmailField(label='Email address', required=True)
    cuisines = forms.MultipleChoiceField(
        choices=[
            ('punjabi', 'Punjabi Cuisine (North India)'),
            ('gujarati', 'Gujarati Cuisine (West India)'),
            ('rajasthani', 'Rajasthani Cuisine (West India)'),
            ('bengali', 'Bengali Cuisine (East India)'),
            ('maharashtrian', 'Maharashtrian Cuisine (West India)'),
            ('kashmiri', 'Kashmiri Cuisine (North India)'),
            ('goan', 'Goan Cuisine (West India)'),
            ('south_indian', 'South Indian Cuisine'),
            ('kerala', 'Kerala Cuisine (South India)'),
            ('tamil', 'Tamil Cuisine (South India)'),
            ('andhra', 'Andhra Cuisine (South India)'),
            ('karnataka', 'Karnataka Cuisine (South India)'),
            ('bihari', 'Bihari Cuisine (East India)'),
            ('odia', 'Odia Cuisine (East India)'),
            ('assamese', 'Assamese Cuisine (Northeast India)'),
            ('manipuri', 'Manipuri Cuisine (Northeast India)'),
            ('nagaland', 'Nagaland Cuisine (Northeast India)'),
            ('mughlai', 'Mughlai Cuisine (North India, influenced by Persian cuisine)'),
            ('parsi', 'Parsi Cuisine (Western India, influenced by Persian cuisine)'),
            ('awadhi', 'Awadhi Cuisine (North India)')
        ],
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    def clean_cuisines(self):
        data = (',').join(self.cleaned_data["cuisines"])
        print(data)
        return data