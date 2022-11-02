from django.shortcuts import render, redirect
from .forms import CommentForm
from .models import Comment

# Create your views here.
productID = None


def comments_view(request):
    comment_form = CommentForm(request.POST or None)
    print('this is comment')
    if comment_form.is_valid():
        print(request)
        full_name = comment_form.cleaned_data['full_name']
        email = comment_form.cleaned_data['email']
        description = comment_form.cleaned_data['description']
        Comment.objects.create(full_name=full_name, email=email, description=description)
        print(request.POST)
        print(request)
        return redirect(f'/products/product/{productID}/t')

    context = {
        'comment_form': comment_form,
    }
    return render(request, template_name='comment_product_component.html', context=context)
