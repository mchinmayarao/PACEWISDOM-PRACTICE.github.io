# Django templates

### 1. Base Template (`base.html`)
This template includes the common structure and Bootstrap integration for all pages.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Learning Platform{% endblock %}</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <a class="navbar-brand" href="{% url 'index' %}">Learning Platform</a>
        <div class="collapse navbar-collapse">
            <ul class="navbar-nav ml-auto">
                {% if user.is_authenticated %}
                    <li class="nav-item"><a class="nav-link" href="{% url 'logout' %}">Logout</a></li>
                {% else %}
                    <li class="nav-item"><a class="nav-link" href="{% url 'login' %}">Login</a></li>
                    <li class="nav-item"><a class="nav-link" href="{% url 'signup' %}">Sign Up</a></li>
                {% endif %}
            </ul>
        </div>
    </nav>
    <div class="container mt-5">
        {% block content %}
        {% endblock %}
    </div>
</body>
</html>
```

### 2. Index Page (`index.html`)
This is the landing page of the site.

```html
{% extends 'base.html' %}

{% block title %}Home{% endblock %}

{% block content %}
    <h1>Welcome to the Learning Platform</h1>
    <p>Explore various courses and enhance your knowledge.</p>
    <a href="{% url 'courses' %}" class="btn btn-primary">Browse Courses</a>
{% endblock %}
```

### 3. Student Dashboard (`student_dashboard.html`)
This page shows the student's subscribed courses.

```html
{% extends 'base.html' %}

{% block title %}Student Dashboard{% endblock %}

{% block content %}
    <h2>Student Dashboard</h2>
    <h3 class="mt-4">Subscribed Courses</h3>
    <div class="list-group">
        {% for course in subscribed_courses %}
            <a href="{% url 'course_content' course.id %}" class="list-group-item list-group-item-action">{{ course.title }}</a>
        {% empty %}
            <p>No courses subscribed yet.</p>
        {% endfor %}
    </div>
{% endblock %}
```

### 4. Teacher Dashboard (`teacher_dashboard.html`)
This page includes course management options for teachers.

```html
{% extends 'base.html' %}

{% block title %}Teacher Dashboard{% endblock %}

{% block content %}
    <h2>Teacher Dashboard</h2>
    <a href="{% url 'create_course' %}" class="btn btn-primary mb-3">Create Course</a>
    <h3 class="mt-4">Your Courses</h3>
    <div class="list-group">
        {% for course in courses %}
            <a href="{% url 'edit_course' course.id %}" class="list-group-item list-group-item-action d-flex justify-content-between align-items-center">
                {{ course.title }}
                <span class="badge badge-primary badge-pill">Edit</span>
                <form action="{% url 'delete_course' course.id %}" method="post" style="display: inline;">
                    {% csrf_token %}
                    <button type="submit" class="btn btn-danger btn-sm">Delete</button>
                </form>
            </a>
        {% empty %}
            <p>No courses available.</p>
        {% endfor %}
    </div>
    <h3 class="mt-4">Students Who Purchased Your Courses</h3>
    <div class="list-group">
        {% for student in students %}
            <a href="#" class="list-group-item list-group-item-action">{{ student.name }} - {{ student.course_title }}</a>
        {% empty %}
            <p>No students have purchased your courses yet.</p>
        {% endfor %}
    </div>
{% endblock %}
```

### 5. Create Course (`create_course.html`)
This page allows teachers to create a new course.

```html
{% extends 'base.html' %}

{% block title %}Create Course{% endblock %}

{% block content %}
    <h2>Create Course</h2>
    <form method="post" action="{% url 'create_course' %}">
        {% csrf_token %}
        <div class="form-group">
            <label for="courseTitle">Course Title</label>
            <input type="text" class="form-control" id="courseTitle" name="title" placeholder="Enter course title" required>
        </div>
        <div class="form-group">
            <label for="courseDescription">Course Description</label>
            <textarea class="form-control" id="courseDescription" name="description" rows="3" placeholder="Enter course description" required></textarea>
        </div>
        <div class="form-group">
            <label for="coursePrice">Course Price</label>
            <input type="number" class="form-control" id="coursePrice" name="price" placeholder="Enter course price" required>
        </div>
        <button type="submit" class="btn btn-success">Create Course</button>
    </form>
{% endblock %}
```

### 6. Edit Course (`edit_course.html`)
This page allows teachers to edit existing courses.

```html
{% extends 'base.html' %}

{% block title %}Edit Course{% endblock %}

{% block content %}
    <h2>Edit Course</h2>
    <form method="post" action="{% url 'edit_course' course.id %}">
        {% csrf_token %}
        <div class="form-group">
            <label for="courseTitle">Course Title</label>
            <input type="text" class="form-control" id="courseTitle" name="title" value="{{ course.title }}" placeholder="Enter course title" required>
        </div>
        <div class="form-group">
            <label for="courseDescription">Course Description</label>
            <textarea class="form-control" id="courseDescription" name="description" rows="3" placeholder="Enter course description" required>{{ course.description }}</textarea>
        </div>
        <div class="form-group">
            <label for="coursePrice">Course Price</label>
            <input type="number" class="form-control" id="coursePrice" name="price" value="{{ course.price }}" placeholder="Enter course price" required>
        </div>
        <h3 class="mt-4">Course Content</h3>
        <div class="form-group">
            <label for="courseContent">Content</label>
            <textarea class="form-control" id="courseContent" name="content" rows="3" placeholder="Enter course content" required>{{ course.content }}</textarea>
        </div>
        <button type="submit" class="btn btn-success">Save Course</button>
        <form method="post" action="{% url 'delete_course' course.id %}" style="display: inline;">
            {% csrf_token %}
            <button type="submit" class="btn btn-danger">Delete Course</button>
        </form>
    </form>
{% endblock %}
```

### 7. Payment Page (`payment.html`)
This page includes the PayPal payment integration.

```html
{% extends 'base.html' %}

{% block title %}Payment{% endblock %}

{% block content %}
    <h2>PayPal Payment</h2>
    <form action="https://www.paypal.com/cgi-bin/webscr" method="post">
        <!-- Identify your business so that you can collect the payments. -->
        <input type="hidden" name="business" value="seller@example.com">
        <!-- Specify a Buy Now button. -->
        <input type="hidden" name="cmd" value="_xclick">
        <!-- Specify details about the item that buyers will purchase. -->
        <input type="hidden" name="item_name" value="{{ course.title }}">
        <input type="hidden" name="amount" value="{{ course.price }}">
        <input type="hidden" name="currency_code" value="USD">
        <!-- Display the payment button. -->
        <input type="image" name="submit" border="0"
        src="https://www.paypalobjects.com/en_US/i/btn/btn_buynow_LG.gif"
        alt="Buy Now">
        <img alt="" border="0" width="1" height="1"
        src="https://www.paypalobjects.com/en_US/i/scr/pixel.gif" >
    </form>
{% endblock %}
```



### 8. Login Page (`login.html`)

```html
{% extends 'base.html' %}

{% block title %}Login{% endblock %}

{% block content %}
    <h2>Login</h2>
    <form method="post" action="{% url 'login' %}">
        {% csrf_token %}
        <div class="form-group">
            <label for="username">Username</label>
            <input type="text" class="form-control" id="username" name="username" placeholder="Enter username" required>
        </div>
        <div class="form-group">
            <label for="password">Password</label>
            <input type="password" class="form-control" id="password" name="password" placeholder="Enter password" required>
        </div>
        <button type="submit" class="btn btn-primary">Login</button>
        <p class="mt-3">Don't have an account? <a href="{% url 'signup' %}">Sign up</a></p>
    </form>
{% endblock %}
```

### 9. Signup Page (`signup.html`)

```html
{% extends 'base.html' %}

{% block title %}Sign Up{% endblock %}

{% block content %}
    <h2>Sign Up</h2>
    <form method="post" action="{% url 'signup' %}">
        {% csrf_token %}
        <div class="form-group">
            <label for="username">Username</label>
            <input type="text" class="form-control" id="username" name="username" placeholder="Enter username" required>
        </div>
        <div class="form-group">
            <label for="email">Email</label>
            <input type="email" class="form-control" id="email" name="email" placeholder="Enter email" required>
        </div>
        <div class="form-group">
            <label for="password">Password</label>
            <input type="password" class="form-control" id="password" name="password" placeholder="Enter password" required>
        </div>
        <div class="form-group">
            <label for="confirm_password">Confirm Password</label>
            <input type="password" class="form-control" id="confirm_password" name="confirm_password" placeholder="Confirm password" required>
        </div>
        <button type="submit" class="btn btn-primary">Sign Up</button>
        <p class="mt-3">Already have an account? <a href="{% url 'login' %}">Login</a></p>
    </form>
{% endblock %}
```

# class based view

To convert your API views into Django class-based views (CBVs) that use Django templates, you’ll need to switch from using `generics` to more specific class-based views that render HTML templates. Here’s how you can adapt your existing views for templates:

### 1. Course List and Create View

#### `views.py`

```python
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Course
from .forms import CourseForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class CourseListView(ListView):
    model = Course
    template_name = 'courses/course_list.html'
    context_object_name = 'courses'

class CourseCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'courses/course_form.html'
    success_url = reverse_lazy('course_list')

    def form_valid(self, form):
        form.instance.teacher = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_teacher  # Adjust this based on your actual logic
```

### 2. Course Detail, Update, and Delete View

#### `views.py`

```python
from django.views.generic import DetailView, UpdateView, DeleteView
from .models import Course
from .forms import CourseForm

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'
    context_object_name = 'course'

class CourseUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'courses/course_form.html'
    success_url = reverse_lazy('course_list')

    def test_func(self):
        course = self.get_object()
        return self.request.user == course.teacher  # Adjust this based on your actual logic

class CourseDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Course
    template_name = 'courses/course_confirm_delete.html'
    success_url = reverse_lazy('course_list')

    def test_func(self):
        course = self.get_object()
        return self.request.user == course.teacher  # Adjust this based on your actual logic
```

### 3. Content List and Create View

#### `views.py`

```python
from django.views.generic import ListView, CreateView
from .models import Content, Course
from .forms import ContentForm

class ContentListView(ListView):
    model = Content
    template_name = 'contents/content_list.html'
    context_object_name = 'contents'

    def get_queryset(self):
        course_name = self.kwargs['name']
        course = Course.objects.get(name=course_name)
        return Content.objects.filter(course=course)

class ContentCreateView(LoginRequiredMixin, CreateView):
    model = Content
    form_class = ContentForm
    template_name = 'contents/content_form.html'
    success_url = reverse_lazy('content_list')

    def form_valid(self, form):
        course_name = self.kwargs['name']
        course = Course.objects.get(name=course_name)
        form.instance.course = course
        return super().form_valid(form)
```

### 4. Content Detail, Update, and Delete View

#### `views.py`

```python
from django.views.generic import DetailView, UpdateView, DeleteView
from .models import Content
from .forms import ContentForm

class ContentDetailView(DetailView):
    model = Content
    template_name = 'contents/content_detail.html'
    context_object_name = 'content'

class ContentUpdateView(LoginRequiredMixin, UpdateView):
    model = Content
    form_class = ContentForm
    template_name = 'contents/content_form.html'
    success_url = reverse_lazy('content_list')

class ContentDeleteView(LoginRequiredMixin, DeleteView):
    model = Content
    template_name = 'contents/content_confirm_delete.html'
    success_url = reverse_lazy('content_list')
```

### 5. Subscribers List View

#### `views.py`

```python
from django.views.generic import ListView
from .models import Enrollment, Course
from django.contrib.auth.mixins import LoginRequiredMixin

class SubscribersListView(LoginRequiredMixin, ListView):
    template_name = 'subscribers/subscriber_list.html'
    context_object_name = 'subscribers'

    def get_queryset(self):
        course_name = self.kwargs['name']
        course = Course.objects.get(name=course_name)
        enrollment = Enrollment.objects.filter(course=course)
        return [{"name": user.student.name, "email": user.student.email} for user in enrollment]
```

### 6. Forms

You'll also need forms for creating and updating `Course` and `Content`. Here's an example using Django forms:

#### `forms.py`

```python
from django import forms
from .models import Course, Content

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'price']  # Adjust fields as necessary

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['title', 'body']  # Adjust fields as necessary
```

### 7. Templates

Here are example templates for each view:

#### `courses/course_list.html`

```html
{% extends 'base.html' %}

{% block title %}Course List{% endblock %}

{% block content %}
    <h2>Courses</h2>
    <a href="{% url 'course_create' %}" class="btn btn-primary">Create New Course</a>
    <ul class="list-group mt-3">
        {% for course in courses %}
            <li class="list-group-item">
                <a href="{% url 'course_detail' course.id %}">{{ course.title }}</a>
            </li>
        {% endfor %}
    </ul>
{% endblock %}
```

#### `courses/course_form.html`

```html
{% extends 'base.html' %}

{% block title %}Course Form{% endblock %}

{% block content %}
    <h2>Create/Edit Course</h2>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit" class="btn btn-primary">Save</button>
    </form>
{% endblock %}
```

#### `courses/course_detail.html`

```html
{% extends 'base.html' %}

{% block title %}Course Detail{% endblock %}

{% block content %}
    <h2>{{ course.title }}</h2>
    <p>{{ course.description }}</p>
    <p>Price: {{ course.price }}</p>
    <a href="{% url 'course_update' course.id %}" class="btn btn-primary">Edit Course</a>
    <a href="{% url 'course_delete' course.id %}" class="btn btn-danger">Delete Course</a>
{% endblock %}
```

#### `contents/content_list.html`

```html
{% extends 'base.html' %}

{% block title %}Content List{% endblock %}

{% block content %}
    <h2>Content for {{ course.name }}</h2>
    <a href="{% url 'content_create' course.name %}" class="btn btn-primary">Add New Content</a>
    <ul class="list-group mt-3">
        {% for content in contents %}
            <li class="list-group-item">
                <a href="{% url 'content_detail' content.id %}">{{ content.title }}</a>
            </li>
        {% endfor %}
    </ul>
{% endblock %}
```

#### `contents/content_form.html`

```html
{% extends 'base.html' %}

{% block title %}Content Form{% endblock %}

{% block content %}
    <h2>Create/Edit Content</h2>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit" class="btn btn-primary">Save</button>
    </form>
{% endblock %}
```

#### `contents/content_detail.html`

```html
{% extends 'base.html' %}

{% block title %}Content Detail{% endblock %}

{% block content %}
    <h2>{{ content.title }}</h2>
    <p>{{ content.body }}</p>
    <a href="{% url 'content_update' content.id %}" class="btn btn-primary">Edit Content</a>
    <a href="{% url 'content_delete' content.id %}" class="btn btn-danger">Delete Content</a>
{% endblock %}
```

#### `subscribers/subscriber_list.html`

```html
{% extends 'base.html' %}

{% block title %}Subscribers{% endblock %}

{% block content %}
    <h2>Subscribers for {{ course.name }}</h2>
    <ul class="list-group mt-3">
        {% for subscriber in subscribers %}
            <li class="list-group-item">
                {{ subscriber.name }} ({{ subscriber.email }})
            </li>
        {% endfor %}
    </ul>
{% endblock %}
```

These templates and views provide a complete setup for managing courses and content, including listing, creating, editing, and deleting, as well as managing subscribers. Adjust paths, field names, and logic as needed based on your specific project requirements.

# Payments
To ensure that a user is enrolled in a course after a successful payment, you need to follow these steps:

1. **Update the `capture_order` view to handle enrollment**: After a successful payment, enroll the user in the course. 

2. **Update the PayPal payment flow**: Ensure the transaction ID is captured and associated with the enrollment.

3. **Modify the `create_order` view to include dynamic course pricing**: Currently, the price is hard-coded; it should be dynamic based on the course.

Here's how you can adjust your code to accomplish these tasks:

### 1. Update `capture_order` View

Modify the `capture_order` view to enroll the user in the course. You'll need to extract user information and the course they paid for from the request.

```python
from django.contrib.auth import get_user_model

User = get_user_model()

@csrf_exempt
def capture_order(request, order_id):
    try:
        # Capture the order
        access_token = generate_access_token()
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}",
        }
        
        response = requests.post(f"{PAYPAL_API_BASE}/v2/checkout/orders/{order_id}/capture", headers=headers)
        result = handle_response(response)

        # Check if the payment was successful
        if result["httpStatusCode"] == 200:
            # Get transaction ID and course information
            transaction = result["jsonResponse"].get("purchase_units", [{}])[0].get("payments", {}).get("captures", [{}])[0]
            transaction_id = transaction.get("id")

            # Get user and course details from the request
            user = request.user
            course_id = json.loads(request.body).get("course_id")  # You need to send course_id in the request body

            # Enroll the user in the course
            course = Course.objects.get(pk=course_id)
            enrollment, created = Enrollment.objects.get_or_create(
                student=user,
                course=course,
                defaults={'transaction_id': transaction_id}
            )

            if created:
                return JsonResponse({"message": "Payment successful and user enrolled!"}, status=200)
            else:
                return JsonResponse({"message": "User already enrolled."}, status=200)
        else:
            return JsonResponse({"error": "Failed to capture order."}, status=result["httpStatusCode"])
    
    except Exception as e:
        print(f"Failed to capture order: {str(e)}")
        return JsonResponse({"error": "Failed to capture order."}, status=500)
```

### 2. Modify `create_order` View

Make sure the order's price matches the course's price. Update the payload to use dynamic values from the `Course` model.

```python
@csrf_exempt
def create_order(request):
    try:
        # Get the cart data from the request
        data = json.loads(request.body)
        course_id = data.get("course_id")
        course = Course.objects.get(pk=course_id)

        access_token = generate_access_token()
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}",
        }
        
        payload = {
            "intent": "CAPTURE",
            "purchase_units": [
                {
                    "amount": {
                        "currency_code": "USD",
                        "value": str(course.price),
                    },
                },
            ],
        }
        
        response = requests.post(f"{PAYPAL_API_BASE}/v2/checkout/orders", headers=headers, json=payload)
        result = handle_response(response)
        
        return JsonResponse(result["jsonResponse"], status=result["httpStatusCode"])
    
    except Exception as e:
        print(f"Failed to create order: {str(e)}")
        return JsonResponse({"error": "Failed to create order."}, status=500)
```

### 3. Update the Checkout Template

Ensure the checkout template sends the `course_id` with the order creation request.

```html
<script>
    window.paypal
        .Buttons({
            style: {
                shape: "rect",
                layout: "vertical",
                color: "gold",
                label: "paypal",
            },
            async createOrder() {
                try {
                    const response = await fetch("/api/orders", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify({
                            course_id: "{{ course.course_id }}",  // Include course_id
                        }),
                    });

                    const orderData = await response.json();
                    if (orderData.id) {
                        return orderData.id;
                    }
                    throw new Error(JSON.stringify(orderData));
                } catch (error) {
                    console.error(error);
                }
            },
            async onApprove(data, actions) {
                try {
                    const response = await fetch(`/api/orders/${data.orderID}/capture`, {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                        },
                    });

                    const orderData = await response.json();
                    if (!orderData.purchase_units) {
                        throw new Error(JSON.stringify(orderData));
                    }
                    const transaction =
                        orderData?.purchase_units?.[0]?.payments?.captures?.[0];
                    resultMessage(
                        `Transaction ${transaction.status}: ${transaction.id}<br>
                        <br>See console for all available details`
                    );
                    console.log("Capture result", orderData, JSON.stringify(orderData, null, 2));
                } catch (error) {
                    console.error(error);
                    resultMessage(`Sorry, your transaction could not be processed...<br><br>${error}`);
                }
            },
        })
        .render("#paypal-button-container");
</script>
```

This setup will enroll the user in the course upon a successful payment and handle different parts of the payment flow properly.