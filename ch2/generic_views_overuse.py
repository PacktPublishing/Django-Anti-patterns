from django.views.generic import ListView 

class MyListView(ListView): 
    model = MyModel 
    template_name = 'my_template.html' 
    context_object_name = 'objects' 