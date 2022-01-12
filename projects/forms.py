from django.forms import ModelForm
from .models import Project


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
            "description",
            "demo_link",
            "source_link",
            'tags'
        ]
