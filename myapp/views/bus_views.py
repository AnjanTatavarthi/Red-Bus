
from django.template.loader import render_to_string
from django.views.generic import ListView
from django import forms
from django.shortcuts import render, redirect
from django.views import View
from myapp.views import reverse_lazy
from myapp.models import *
from django.core.mail import send_mail


class BusDetailsForm(forms.Form):
    source=forms.CharField(max_length=128)
    destination=forms.CharField(max_length=128)
    date=forms.DateField()
    
class SearchBuses(View):
    def get(self, request, *args, **kwargs):
        form = BusDetailsForm()
        return render(request, template_name='redbus/searchbuses.html', context={'form': form,'invalid':False})
    def post(self,request,*args,**kwargs):
        form=BusDetailsForm(request.POST)
        print(form)
        if(form.is_valid()):
                form.cleaned_data['date']=str(form.cleaned_data['date'])
                request.session['web_input'] =form.cleaned_data
                print(form.cleaned_data)
                return redirect(reverse_lazy('myapp:display'))
        else:
            return render(request, template_name='redbus/searchbuses.html', context={'form': form, 'invalid':True})


class DisplayForm(ListView):
    model=BusInfo
    context_object_name = 'buses'
    template_name = 'redbus/buslist.html'
    data=[]

    def get(self, request, *args, **kwargs):
        self.data = request.session['web_input']
        return super(DisplayForm, self).get(request, *args, **kwargs)

    def get_queryset(self):
        res=BusInfo.objects.filter(source=self.data['source'],destination=self.data['destination'],date_of_journey=self.data['date'])
        print(res)
        return BusInfo.objects.filter(source=self.data['source'],destination=self.data['destination'],date_of_journey=self.data['date'])




class DisplayBuses(View):
    data=[]
    def get(self, request, *args, **kwargs):
        self.data = request.session['web_input']
        res = BusInfo.objects.filter(source=self.data['source'], destination=self.data['destination'],date_of_journey=self.data['date'])
        print(len(res))
        if(len(res)>0):
            return render(request,template_name='redbus/buslist.html',context={'buses':res})
        else:
            return render(request,template_name='redbus/unavailable.html')





class BusSeats(View):

    def get(self,request,*args,**kwargs):
        passengers=PassengerInfo.objects.filter(ticket__bus_id=kwargs['id']).values('seat_no')
        return render(request, template_name='redbus/seats.html', context={'reserved_seats': passengers})

    def post(self,request,*args,**kwargs):
        data=request.POST
        data=dict(data)
        del data['csrfmiddlewaretoken']
        seats=list(data.keys())
        s = dict()
        i = 1
        for seat in seats:
            s[i] = seat
            i+=1
        request.session['seats']=s
        return redirect('myapp:seats',id=kwargs['id'])

class TicketDetails(View):
    def get(self,request,*args,**kwargs):
        seats=request.session['seats']
        return render(request, template_name='redbus\passengerInfo.html',context = {'seats':seats})

    def post(self,request,*args,**kwargs):
        data=request.POST
        data=dict(data)
        del data['csrfmiddlewaretoken']
        bus=BusInfo.objects.get(id=kwargs['id'])

        ticket=TicketInfo.objects.create(status="booked",phone_no=data['phoneno'][0],no_of_tickets=len(data)-1,total_amount=(len(data)-1) *bus.fare,bus_id=kwargs['id'],user=request.user)
        cur_seats=bus.available_seats-len(data)-1
        print("-----------------------------------------")
        print(bus.available_seats)
        print("the number of ticket",ticket.no_of_tickets)
        print("the no of ticketes",len(data)-1)
        print(cur_seats)
        BusInfo.objects.filter(id=kwargs['id']).update(available_seats=cur_seats)
        k=1
        for i in data.values():
            if(len(i)==4):
                passenger=PassengerInfo.objects.create(name=i[0],age=i[1],gender=i[2],seat_no=i[3],ticket=ticket)
                k+=1

        passengers=PassengerInfo.objects.filter(ticket=ticket)
        seats=','.join([passengers[i].seat_no for i in range(len(passengers))])
        html_message = render_to_string('redbus/maillticket.html', context={'seats': seats, 'ticket': ticket, 'bus': bus})
        string = html_message
        send_mail(subject='Ticket Confirmation', message="", from_email='anjantatavarthi1997@gmail.com',
        recipient_list=[request.user.email], html_message=string)
        return render(request, template_name='redbus/busticket.html', context={'seats':seats, 'ticket':ticket, 'bus':bus})


