from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django import forms
from myapp.models import*



class SignUpForm(forms.Form):
    username = forms.CharField(max_length=128)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')


class LoginForm(forms.Form):
    username=forms.CharField(max_length=128)
    password=forms.CharField(widget=forms.PasswordInput)

class RegistrationForm(forms.ModelForm):
        model=User
        exclude={'last_login'}



class Login(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,template_name='redbus/login.html',context={'form':form,'invalid':False})

    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if(form.is_valid()):
            user=authenticate(request,username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if(user!=None):
                login(request,user)
                return redirect(reverse_lazy('myapp:searchbuses'))
            else:
                return render(request, template_name='redbus/login.html', context={'form': form,'invalid':True})

        return redirect('login')



class signup(View):
    def get(self,request,*args,**kwargs):
        form=SignUpForm()
        return render(request,template_name='redbus/register.html')

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)

        if form.is_valid():

            user = User.objects.create_user(**form.cleaned_data)
            user.save()
            login(request, user)
            return redirect(reverse_lazy('myapp:searchbuses'))
        else:
          form = SignUpForm()
          return render(request, 'redbus/register.html', {'form': form})


def Logout(request):
    logout(request)
    return redirect('myapp:login')

class ViewBookings(View):
    def get(self,request,*args,**kwargs):
        tickets=TicketInfo.objects.filter(user=request.user)
        print(tickets)
        return render(request,'redbus/veiwbookings.html',{'tickets':tickets})
    def post(self, request, *args, **kwargs):

        print(request.POST)


class ViewTicket(View):
    def get(self,request,*args,**kwargs):
        ticket = TicketInfo.objects.get(id=kwargs['ticketid'])
        bus=BusInfo.objects.get(id=ticket.bus.id)
        passengers = PassengerInfo.objects.filter(ticket=kwargs['ticketid'])
        seats = ','.join([passengers[i].seat_no for i in range(len(passengers))])
        return render(request, template_name='redbus/busticket.html', context={'seats': seats, 'ticket': ticket, 'bus': bus})

class SendMail(View):
    def get(self,request,*args,**kwargs):
        ticket = TicketInfo.objects.get(id=kwargs['ticketid'])
        bus = BusInfo.objects.get(id=ticket.bus.id)
        passengers = PassengerInfo.objects.filter(ticket=kwargs['ticketid'])
        seats = ','.join([passengers[i].seat_no for i in range(len(passengers))])
        html_message = render_to_string('redbus/maillticket.html',
                         context={'seats': seats, 'ticket': ticket, 'bus': bus})
        string = html_message
        send_mail(subject='Ticket Confirmation', message="", from_email='anjantatavarthi1997@gmail.com',
                  recipient_list=[request.user.email], html_message=string)

class CancelTicket(View):
    def get(self,request,*args,**kwargs):
        ticket = TicketInfo.objects.get(id=kwargs['ticketid']).delete()




