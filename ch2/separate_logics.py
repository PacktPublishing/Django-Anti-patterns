def separated_view(request): 
    # Fetch data from request 
    data = request.POST.get('data') 

    # Process data (business logic) 
    result = process_data(data) 

    # Return data for rendering 
    return result 

def process_data(data): 
    # Business logic processing 
    return data 