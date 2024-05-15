# Bad practice: Not using CBV for a form view
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            return HttpResponseRedirect('/orders/')
    else:
        form = OrderForm()
    return render(request, 'orders/create_order.html', {'form': form})