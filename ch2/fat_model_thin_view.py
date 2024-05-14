class FatModel(models.Model): 
    # Fields and simple methods here 
    pass 

def thin_view(request): 
    # Move complex logic outside of model 
    result = complex_operation() 
    return HttpResponse(result) 

def complex_operation(): 
    # Complex business logic outside model 
    pass 