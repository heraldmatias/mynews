from django import forms

class ResumenForm(forms.Form):
    url = forms.URLField(required = True, widget = forms.TextInput(attrs={'style':'width:100%;'}))
    resumen = forms.CharField(required = False, widget = forms.Textarea(attrs={'style':'width:100%;'}))

    def __init__(self, *args, **kwargs):
        super(ResumenForm, self).__init__(*args,**kwargs)
        
    def summary(self):
        cleaned_data = self.cleaned_data
        from engine.summarize import summarize_page
        self.data['resumen'] = u'%s' % summarize_page(cleaned_data['url']).__str__()

