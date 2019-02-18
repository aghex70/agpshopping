from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import reverse

from django.contrib import messages

from interests.models import Customer
from interests.models import Category

from interests.forms import InterestsForm
# from concrete_base_model.models import

# Create your views here.
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
            return redirect('/user/'+str(default_customer.id)+'/interests')
        else:
            messages.error(request, "An error has occured. Check all the fields.")
            return redirect('/')
    context = {'form': form}
    return render(request, 'home.html', context)

def list_user_interests(request, id_user):
    return render(request, 'home.html')
