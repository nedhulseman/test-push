from django.shortcuts import render



def index(requests):
    context_dict = {'text':'hello world', 'number':100}
    return render(requests, 'basic_app/index.html', context_dict)
def relative(requests):
    return render(requests, 'basic_app/rel_url_temp.html')
def other(requests):
    return render(requests, 'basic_app/other.html')
