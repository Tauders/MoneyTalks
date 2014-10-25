from registration.backends.simple.views import RegistrationView
from moneytalks.forms import MyRegistrationForm


class MyRegistration(RegistrationView):
    form_class = MyRegistrationForm