from django.views.generic import ListView

from .models import Product, Category


class IndexView(ListView):
    model = Product
    template_name = "index.html"
    context_object_name = "products"
    queryset = Product.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
