# Bad practice: Function-based views with complex logic
def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    if request.user.is_authenticated and request.user.is_staff:
        # Do something for staff users
        pass
    else:
        # Do something for regular users
        pass

    # Render template
    return render(request, 'product_detail.html', {'product': product})

# Good practice: Using CBVs to separate concerns
from django.views.generic import DetailView

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated and self.request.user.is_staff:
            # Add additional context for staff users
            pass
        else:
            # Add additional context for regular users
            pass

        return context
