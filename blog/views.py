from django.shortcuts import render, get_object_or_404, redirect
from .models import News, Products, Gallery, Contact, Sotuv, Comment
from .forms import ContactForm, SotuvForm, CommentForm
from django.views.generic import UpdateView, CreateView, DeleteView, ListView
from django.urls import reverse_lazy
# Create your views here.
def index(request):
    news = News.objects.all()
    products = Products.objects.all()
    context = {
        'news': news,
        'products': products
    }
    return render(request, 'index.html', context=context)
class ProductsUpdateView(UpdateView):
    model = Products
    fields = ('name', 'cost', 'dis_cost', 'img')
    template_name = 'products_edit.html'
class ProductsDeleteView(DeleteView):
    model = Products
    template_name = 'products_delete.html'
    success_url = reverse_lazy('index')
class ProductCreateView(CreateView):
    model = Products
    template_name = 'products_create.html'
    fields = ('name', 'img', 'cost', 'dis_cost', 'slug')
def ashyolar(request):
    products = Products.objects.all()
    context = {
        'products': products
    }
    return render(request, 'Ashyolar.html', context=context)
def about(request):
    return render(request, 'Biz haqimizda.html', context={})
def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('afterContact')
    return render(request, "Bog'lanish.html", context={})
def detail(request, products):
    product = get_object_or_404(Products, slug=products)
    comments = product.comments.filter(active=True)
    comment_count = comments.count()
    new_comment = None
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.products = product
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()
    context = {
        'product': product,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'comment_count': comment_count
    }
    return render(request, "detel.html", context=context)
def gallery(request):
    foto = Gallery.objects.all()
    context = {
        'foto': foto
    }
    return render(request, "Fo'to'Galareya.html", context=context)
def savat(request):
    proSotuv = Sotuv.objects.all()
    products = Products.objects.all()
    context = {
        'proSotuv': proSotuv,
        'products': products,
    }
    return render(request, "Savat.html", context=context)
def afterContact(request):
    return render(request, 'afterContactForm.html', context={})
def sotuv(request):
    sotuvform = SotuvForm(request.POST or None)
    if request.method == 'POST' and sotuvform.is_valid():
        sotuvform.save()
        return redirect('savat')
    context = {
        'sotuvform': sotuvform
    }
    return render(request, 'Form.html', context=context)

class SearchResults(ListView):
    model = Products
    template_name = 'search_result.html'
    context_object_name = 'barcha_mahsulotlar'
    def get_queryset(self):
        query = self.request.GET.get('q')
        return Products.objects.filter(
            name__icontains=query
        )

