from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from gallery.models import Notice, Owner,Ques
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,CreateView
from django.urls.base import reverse_lazy
from gallery.forms import MyForm
from rest_framework import viewsets, permissions
from gallery.serializers import NoticeSerializer, OwnerSerializer,\
    UserSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import permission_classes
from gallery.permissions import MyPers2

def about(request):
    return render(request, "about.html");
def contact(request):
    return render(request, "contact.html");
def DogBreedInfo(request):
    return render(request, "DogBreedInfo.html");  
def DogBreedInfo2(request):
    return render(request, "DogBreedInfo2.html");  
def DogBreedInfo3(request):
    return render(request, "DogBreedInfo3.html");  
    

@method_decorator(login_required, name='dispatch')
class NoticeList(ListView):
    model = Notice
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Notice.objects.all().order_by('-id')
        else:
            return Notice.objects.all().order_by('-id')
    paginate_by = 7

@method_decorator(login_required, name='dispatch')
class NoticeDetails(DetailView):
    model = Notice
    
@method_decorator(login_required, name='dispatch')
class OwnerUpdate(UpdateView):
    form_class=MyForm
    model = Owner
    success_url = reverse_lazy('notice_list')  
    
class QuesCreate(CreateView):
    success_url = reverse_lazy('notice_list')
    model = Ques
    fields = ['question']
    def form_valid(self, form):
        form.instance.notice = Notice.objects.filter(id=self.request.GET.get('nid'))[0] 
        form.instance.user = self.request.user
        return super(QuesCreate, self).form_valid(form)
       
    
    
# below code for API
class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all().order_by('-cr_date')
    serializer_class = NoticeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all().order_by('-uploaded_at')
    serializer_class = OwnerSerializer
    permission_classes = (MyPers2,)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

 