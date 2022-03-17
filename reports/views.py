from multiprocessing import context
from django.shortcuts import render,get_object_or_404,redirect
from .forms import *
from areas.models import *
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import *
from .models import *

# Create your views here.

#!ReportView
@login_required
def reportView(request,production_line):
    rform = ReportForm(request.POST or None,production_line=production_line)
    print('Production Line',production_line)
    print('################################')
    
    pform = ProblemReportedForm(request.POST or None)#request.POST or None sonra yazarsan yeniden bunu amma helelik diger form ustunde isleyirik ona gore silindi mecbur cunki djangoda 1 view icerisinde 1 dene form isleye biler amma yollari var coxlu form isletmeyinde
    reports = Report.objects.filter(production_line__name=production_line)#yeni hemin mal haqqinda gelen reportlari getir mene
    
    #?Problem Write
    if 'submitbtn1' in request.POST:
        print('PROBLEM')
            #pform
        if pform.is_valid():#pform = ProblemReport model
            r_id = request.POST.get('report_id')
            print(r_id)
            print('POST request working pform')
            report = Report.objects.get(id=r_id)
            obj = pform.save(commit=False)
            obj.user = request.user
            obj.report = report
            obj.save()  
            return redirect(request.META.get('HTTP_REFERER'))
            
            #requestden sonra formlarin sifirlamalisanki diger formu isledende yeni submit filan olanda diger formdaki qalan input yerleir ile toqqusmasin
            #reset form after request
            # rform = ReportForm()
            # pform = ProblemReportedForm()
    
    #?Report Write
    elif 'submitbtn2' in request.POST:
        print('REPORT')
        #rform
        if rform.is_valid():
            line = get_object_or_404(ProductionLine,name=production_line)
            obj = rform.save(commit=False)
            obj.user = request.user
            obj.production_line = line
            obj.save()#sonda save yaz yoxsa database oturmaz islenen kod datasi
            return redirect(request.META.get('HTTP_REFERER'))
            
            #reset form after request
            # rform = ReportForm()
            # pform = ProblemReportedForm()
            
    context = {
        'rform':rform,
        'pform':pform,
        'reports':reports
    }
    return render(request,'reports/report.html',context)

#!DeleteView for ReportDelete
def deleteView(request,*args,**kwargs):
    r_id = kwargs.get('pk')
    obj = Report.objects.get(id=r_id)
    obj.delete()
    return redirect(request.META.get('HTTP_REFERER'))

#!UpdateView for ReportUpdate
class ReportUpdatView(UpdateView):
    model = Report
    form_class = ReportForm
    context_object_name = 'updateReport'
    template_name = 'reports/update.html'
    
    def get_success_url(self):
        return self.request.path

#!HomeView Giris eden userin ProductionLine gosterir ancag ve axtaris etmek olur
class HomeView(FormView):
    template_name = 'reports/home.html'
    form_class = ReportSelectLineForm
    
    def get_form_kwargs(self):
        kwargs = super(HomeView,self).get_form_kwargs()
        kwargs['logged_user'] = self.request.user
        return kwargs
    
    def post(self,*args,**kwargs):
        prod_line = self.request.POST.get('prod_line')
        return redirect('pform:reportView',production_line=prod_line)

#!SelectView
class SelectView(FormView):
    template_name = 'reports/select.html'
    form_class = ReportResultForm
    success_url = reverse_lazy('pform:mainReportSummary')#yeni session olan seyfeye don oz session deyerinle birlikde
    
    def form_valid(self,form):
        self.request.session['day'] = self.request.POST.get('day',None)
        self.request.session['production_line'] = self.request.POST.get('production_line',None)
        print('My session date', self.request.session['day'])
        return super(SelectView,self).form_valid(form)

#!main_report_summary
@login_required
def main_report_summary(request):
    try:
        #session data
        day = request.session.get('day',None)
        production_line_id = request.session.get('production_line',None)#return id
        
        #database filtering session data
        execution_qs = Report.objects.filter_by_day_prodid(day,production_line_id).aggregate_execution()['execute__sum']
        planned_qs = Report.objects.filter_by_day_prodid(day,production_line_id).aggregate_plan()['plan__sum']
        
        print(execution_qs)
        print(planned_qs)
        
        #report_qs_day = Report.objects.filter_by_day_prodid(day)
        #execution_agg = Report.objects.aggregate_execution().get('execute__sum')
        # print('Execution Agg',execution_agg)
        
        # print('Day',report_qs_day)
        
        # print('Manager yeni oz sorgumuzun deyeri', report_qs_day)
        
    except:
        pass
    
    context = {
        'day':day,
        'report_qs_day_prod_id':execution_qs,
        'planned_qs':planned_qs
    }
    
    return render(request,'reports/summary.html',context)