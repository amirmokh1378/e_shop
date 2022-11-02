import pprint

from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.http import Http404

from eshop_orders.forms import UserNewOrderForm
from .models import Product
from eshop_product_categories.models import ProductCategory
import eshop_Comments
from eshop_tags.models import Tag


# Create your views here.

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def products_page(request):
    object_list = Product.objects.get_queryset()
    context = {
        'object_list': object_list
    }
    return render(request, 'product/product_list.html', context=context)


class ProductListView(ListView):
    template_name = 'product/product_list.html'
    paginate_by = 4

    # model = Product

    def get_queryset(self):
        return Product.objects.filter_by_active()


class SearchListView(ListView):
    template_name = 'product/product_list.html'
    paginate_by = 7

    # model = Product

    def get_queryset(self):
        qu = self.request
        print(qu.path)
        return Product.objects.filter_by_title_or_description(qu.GET['l'])


def detail_view_product_page(request, productId, *args, **kwargs):
    productQu = Product.objects.filter(pk=productId)
    eshop_Comments.views.productID = productId
    if productQu.count() == 1 and productQu.first().active:
        # order part
        orderForm = UserNewOrderForm(request.POST or None, initial={'product_id': productId})
        # end of order part
        galleryQu = Product.objects.filter_by_gallery(productId)
        galleryQuList = list(chunks(galleryQu, 3))
        suggestionProducts = Product.objects.filter(categories__product=productQu[0]).distinct()
        suggestionProductsList = list(chunks(suggestionProducts, 3))
        context = {
            'object': productQu[0],
            'galleryQuList': galleryQuList,
            'suggestionProductsList': suggestionProductsList,
            'orderForm': orderForm
        }
    else:
        raise Http404('مجود نیست')
    return render(request, 'product/product_detail.html', context=context)


class ProductCategoryListView(ListView):
    template_name = 'product/product_list.html'
    paginate_by = 4

    # model = Product

    def get_queryset(self):
        try:
            # self.kwargs
            # self.args
            # self.request
            categoryName = self.kwargs['categoryName']
            return Product.objects.filter_by_category(categoryName)
        except EOFError as e:
            raise Http404(f'the specified is not found')


def render_partial_category(request):
    queryset = ProductCategory.objects.all()
    context = {
        'qu': queryset
    }
    return render(request, 'product/partial_product_category_component.html', context=context)

# def filter(request, *args, **kwargs):
#     pq = Product.objects.filter(tag=2)
#     pq = Product.objects.filter(tag__title='p')
#     pq = Product.objects.filter(tag__title__icontains='p')
#     tq = Tag.objects.filter(products=1)
#     tq = Tag.objects.filter(products__image=1)
#     tq = Tag.objects.filter(products__title__icontains='Blender')
#     lookup = Q(tag=1) | Q(active=True) & Q(tag__title='p') | Q(tag__title__icontains='p')
#     print(lookup)
#     pq = Product.objects.get_queryset().filter(lookup).distinct()
#     lookup = Q(products=1) | Q(active=True) & Q(products__title='p') | Q(products__title__icontains='p')
#     print(lookup)
#     tq = Tag.objects.get_queryset().filter(lookup).distinct()
#
#     print('pq: ', pq)
#     print('tq: ', tq)
#     context = {
#     }
#
#     return render(request, 'product/product_detail.html', context=context)
