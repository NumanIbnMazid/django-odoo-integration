from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
from utils.odoo_api import OdooAPI
from utils.forms import BookForm
from django.shortcuts import render, redirect
# import erppeek

api = OdooAPI(
    url=settings.ODOO_URL,
    db=settings.ODOO_DB,
    username=settings.ODOO_USER,
    password=settings.ODOO_PASSWORD
)


class HomeView(TemplateView):
    template_name = 'pages/home.html'

    def get(self, request, *args, **kwargs):
        odoo_data = api.search_read('ir.module.module', [
            ['state', '=', 'installed']], ['name'])
        odoo_book_data = api.search_read(
            'library.book', [], ['name', 'short_name'])
        context = {
            'odoo_data': odoo_data,
            'odoo_book_data': odoo_book_data,
        }
        return render(request, "pages/home.html", context=context)


def add_book(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        api.create('library.book', {
                   'name': form.cleaned_data['name'], 'short_name': form.cleaned_data['short_name']})
        return redirect('/')
    context = {'form': form}
    return render(request, 'pages/add-book.html', context)
