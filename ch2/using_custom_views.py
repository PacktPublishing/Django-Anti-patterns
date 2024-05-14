from django.views.generic import TemplateView 

class MyCustomView(TemplateView): 

    template_name = 'my_template.html' 

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        context['objects'] = MyModel.objects.all() 
        return context 