from django.shortcuts import render
from app.forms import ContactForm
# Create your views here.
def index(request):
    contact_form=ContactForm()
    return render(request, 'index.html',{'form':contact_form})

def fd(request):
    if request.method=='POST':
        fn=request.POST['first_name']
        ln=request.POST['last_name']
        em=request.POST['email']
        ms=request.POST['content']
    return render(request, 'form_data.html',{'title':'Data Page','fn':fn,'ln':ln,'em':em,'ms':ms})