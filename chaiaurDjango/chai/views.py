from django.shortcuts import render
from .models import ChaiVarity
from django.shortcuts import get_object_or_404
from .forms import ChaiVarityForm
from .models import ChaiVarity, Store

# Create your views here.
def all_chai(request):
   print("=="*100)
   if request.method == "GET":
       chais = ChaiVarity.objects.all()
       print(chais[0].__dict__)
       return render(request, 'chai/all_chai.html', {"chais": chais})


def chai_detail(request,chai_id):
   chai = get_object_or_404(ChaiVarity, pk=chai_id)
   return render(request, "chai/chai_detail.html", {"chai":chai})





def chai_store_view(request):
   stores = None
   if request.method == 'POST':
       form = ChaiVarityForm(request.POST)
       if form.is_valid():
           chai_variety = form.cleaned_data['chai_varity']
           stores = Store.objects.filter(chai_varieties=chai_variety)
   else:
       form = ChaiVarityForm()
   return render(request, 'chai/chai_stores.html',
                 {'stores': stores, 'form': form})


