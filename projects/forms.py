from django.forms import ModelForm, widgets
from .models import Project
from django import forms


class ProjectForm(ModelForm):
    class Meta:
        # at a minimum a modelform needs two fields
        model = Project  # the model that we're gonna create form from
        # fields = '__all__'  # it's gonna look at all the attributes of the
        # Project class(table), but leave id alone because that's not an
        # editable field, created won't be there because that's automatically
        # generated
        fields = [
            "title",
            "featured_image",
            "description",
            "demo_link",
            "source_link",
            "tags",
        ]
        # it's from django.forms and makes our tags selection more user-friendly
        widgets = {
            "tags": forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        # self.fields["title"].widget.attrs.update({
        #     "class": "input",
        #     "placeholder": "Add Title"})

        # # we went into this field right here (title), we used the init
        # # method above and we're just going to overwrite it, we then select
        # # that and go into the widgets attributes and we want to update
        # # a specific attribute. We told it to update the class and go
        # # ahead and make that input field or add this class to it

        # self.fields["description"].widget.attrs.update({
        #     "class": "input",
        #     "placeholder": "Add Description"})

        for name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'input',
                'placeholder': 'Add ' + f'{name}'.capitalize()
            })
