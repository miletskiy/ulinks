
from django import forms
from django.core.urlresolvers import reverse

from links.models import Resource

from crispy_forms.helper import FormHelper 
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions


class ResourceAddForm(forms.models.ModelForm):
    """docstring for ResourceForm"""

    class Meta:
        model = Resource
        fields = ('title', 'link', 'description', )
    
    def __init__(self, *args, **kwargs):
        super(ResourceAddForm, self).__init__(*args, **kwargs)
        # super(ResourceAddForm, self).__init__(*args, **kwargs)(self):
        
        self.helper = FormHelper(self)

        self.helper.form_action = reverse('new_link')

        self.helper.form_method = 'POST'
        self.helper.form_class = 'col-sm-10 form-horizontal'

        # field properties
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-8'

        # buttons
        self.helper.layout.fields.append(FormActions(
            Submit('add_button', 'Add', css_class="btn btn-success"),
            Submit('cancel_button', 'Cancel', css_class="btn btn-link"),
        ))

