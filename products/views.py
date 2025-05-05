from django.views import generic

from .forms import CommentForm
from .models import Product

class ProductListView(generic.ListView):  # class base view: CBV
    queryset = Product.objects.filter(active=True)
    # model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context