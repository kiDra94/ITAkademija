from django.shortcuts import render
from django.http import HttpResponse #sluzi da povratnu vrijednost index funkcije pretvori u Http kod!
from django.http import HttpResponseRedirect
from .forms import BookForm
from django.urls import reverse

books = [{'title':'The Picture of Dorian Gray','year':'1890'},
        {'title':'Pride and Prejudice','year':'1813'},
        {'title':'The Adventures of Tom Sawyer ', 'year':'1875'},
        {'title':'The Raw Youth', 'year':'1875'},
        {'title':'Twelve Years a Slave ', 'year':'1853'},
        {'title':'Hamlet', 'year':'1603'}]


'''def index(requst):
    return render(requst, 'index.html', {'books' : books}) # render generise odgovor sablona i vraca klijentu
    # za parametre uzima requst(klijentski zahtjev koji vraca serveru), index.html je sablonski fajl,
    #  rijecnik ce fujncija iskoristiti da popuni polja u html fajlu'''
#def inndex prosiren
def index(requst, book_name = None):
    if not book_name:
        return render(requst, 'index.html', {'books' : books})
    temp_res = []
    if book_name:
        for x in books:
            if str(book_name).lower() == x['title'].lower():
                temp_res.append(x['year'])

        if temp_res:
            return HttpResponse("<h1>Book {} was published in {} year</h1>".format(book_name, temp_res[0]))
        else:
            return HttpResponse("<h1>No book found</h1>")
        
def main_page(requst):
    return HttpResponse("<h1>Welcome to our library.</h1>")

def int_test(request, int_key):
    temp_res = []
    for x in books:
        if str(int_key) == x['year']:
            temp_res.append(x['title'])
    if temp_res:
        return HttpResponse("<h1>Book published in requested year is {} </h1>".format(temp_res[0]))
    else:
        return HttpResponse("<h1>No book found for selceted year</h1>")

def redirect_test(request):
    return HttpResponse("<h1>Adding successful</h1>")

def get_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            books.append({'title' : form.cleaned_data['book_title'], 'year' : form.cleaned_data['book_year']})
            return HttpResponseRedirect(reverse('redirect'))
    else:
        form = BookForm()
        return render(request, 'form.html', {'form' : form})