def mixed_view(request): 
    # Fetch data from request 
    data = request.POST.get('data') 

    # Process data (business logic) 
    result = process_data(data) 

    # Render HTML response 
    return HttpResponse('<h1>{}</h1>'.format(result)) 