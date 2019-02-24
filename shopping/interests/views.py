from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import reverse

from django.contrib import messages

from interests.models import Customer
from interests.models import Category

from interests.forms import InterestsForm

from django.views.generic.list import ListView


def home_page(request):
    default_customer, _ = Customer.objects.get_or_create(name="John", surname="Doe")
    default_customer.interests.clear()
    form = InterestsForm()
    if request.method == 'POST':
        form = InterestsForm(request.POST)
        if form.is_valid():
            for key, value in form.cleaned_data.items():
                for interest in value:
                    filtered_interest, _ = Category.objects.get_or_create(name=interest)
                    default_customer.interests.add(filtered_interest)
            default_customer.save()
            return redirect('/user/'+str(default_customer.id)+'/interests/')
        else:
            messages.error(request, "An error has occured. Check all the fields.")
            return redirect('/')
    context = {'form': form}
    return render(request, 'home.html', context)

def user_interests_list(request, id_user):
    customer = Customer.objects.get(id=id_user)
    user_interests = Category.objects.filter(customer__id=id_user)
    context = {'user_interests': user_interests, 'customer': customer}
    return render(request, 'user_interests_list.html', context)

class InterestListView(ListView):
    model = Category
    template_name = 'user_interests_list_cbv.html'
    context_object_name = 'user_interests'

    # Need to override in order to pass parameters (gotten from urls)
    def get_queryset(self):
        queryset = super(InterestListView, self).get_queryset()
        return queryset.filter(customer__id=self.kwargs['id_user'])
