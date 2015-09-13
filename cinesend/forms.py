from django import forms


class MySignupForm(forms.Form):
    first_name = forms.CharField(max_length=40, required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=40, required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    # address = AddressField(widget=forms.TextInput(attrs={'placeholder': 'Invite Code'}))
    invite_code = forms.CharField(max_length=40, required=True,
                                  widget=forms.TextInput(attrs={'placeholder': 'Invite/coupon Code'}))

    def clean(self):
        super(MySignupForm, self).clean()
        if self.cleaned_data.get("invite_code") != "HOTDOCS15":
            raise forms.ValidationError("You must have a valid invite code to sign up for CineSend Beta")
        return self.cleaned_data

    def signup(self, request, user):
        form = MySignupForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
