from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

class RequestForm(forms.Form):

    def __init__(seld, *args, **kwargs):
        super(ExampleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
            HTML(
            'Request',
            ),
            ButtonHolder(
                Submit('submit', 'Submit')
            )
        )
