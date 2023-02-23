from django import forms

class Login(forms.Form):
    username = forms.CharField(max_length=32)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput)

class Register(forms.Form):
    username = forms.CharField(max_length=32)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput)
    name = forms.CharField(max_length=128)
    choice = forms.ChoiceField(choices=(("1", "Соискатель"), ("2", "Работадатель"),))

class EditWorker(forms.Form):
    name = forms.CharField(max_length=128)
    description = forms.TextInput()
    contacts = forms.CharField(max_length=256)

class EditEmployer(forms.Form):
    aname = forms.CharField(max_length=128)
    mount_of_employees = forms.IntegerField()
    address = forms.CharField(max_length=128)
    contacts = forms.CharField(max_length=256)
    description = forms.TextInput()

class WorkerExperience(forms.Form):
    employer_name = forms.CharField(max_length=128)
    start_date = forms.DateField()
    end_date = forms.DateField()
    description = forms.TextInput()

class CreateVacancy(forms.Form):
    name = forms.CharField(max_length=128)
    description = forms.TextInput()
    salary = forms.IntegerField()
    image = forms.ImageField()


