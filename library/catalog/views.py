from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.    
    num_authors = Author.objects.count()
    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    paginate_by = 10
    context_object_name = 'book_list'   # your own name for the list as a template variable
    template_name = 'book_list.html'  # Specify your own template name/location

    def get_queryset(self):
        return Book.objects.all()[:5]

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        return context

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book_detail.html'
    
class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 20
    context_object_name = 'author_list'   # your own name for the list as a template variable
    template_name = 'author_list.html'  # Specify your own template name/location

    def get_queryset(self):
        return Author.objects.all()[:20]

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(AuthorListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        return context

class AuthorDetailView(generic.DetailView):
    model = Author
    paginate_by = 10
    context_object_name = 'author_detail'   # your own name for the list as a template variable
    template_name = 'author_detail.html'  # Specify your own template name/location
