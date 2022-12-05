from django.shortcuts import render

from books.models import Book


def books_view(request):
    '''общий каталог'''
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {'books': books}
    return render(request, template, context)


def books_view_per_date(request, filter_date):
    '''фильтр по дате публикации'''
    template = 'books/books_list_filter_per_date.html'
    books = Book.objects.filter(pub_date=filter_date)

    # список всех дат публикаций:
    ALL_PUB_DATES = []
    all_books = Book.objects.all()
    for i in all_books:
        if str(i.pub_date) not in ALL_PUB_DATES:
            ALL_PUB_DATES.append(str(i.pub_date))

    ALL_PUB_DATES = sorted(ALL_PUB_DATES)
    book_index = ALL_PUB_DATES.index(filter_date)
    max_index = len(ALL_PUB_DATES) - 1
    preview_pub_day = ALL_PUB_DATES[book_index - 1]

    # задаем индекс next_page или False:
    if book_index < max_index:
        next_pub_day = ALL_PUB_DATES[book_index + 1]
    else:
        next_pub_day = False

    context = {'books': books,
               'filter_date': filter_date,
               'ALL': ALL_PUB_DATES,
               'book_index': book_index,
               'preview_pub_day': preview_pub_day,
               'next_pub_day': next_pub_day,
               'max_index': max_index
               }
    return render(request, template, context)
