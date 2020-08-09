from django.shortcuts import render
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io
# Create your views here.
def accept(request):
    if request.method=="POST":
        name=request.POST.get("name","")
        email=request.POST.get("email","")
        phone=request.POST.get("phone","")
        summary=request.POST.get("summary","")
        degree=request.POST.get("degree","")
        school=request.POST.get("school","")
        university=request.POST.get("university","")
        previous_work=request.POST.get("previous_work","")
        skills=request.POST.get("skills","")
        skills2=request.POST.get("skills2","")
        skills3=request.POST.get("skills3","")
        oskills=request.POST.get("oskills","")
        achievements=request.POST.get("achievements","")
        certify=request.POST.get("certify","")
        linkedin=request.POST.get("linkedin","")
        sgrade=request.POST.get("sgrade","")
        ugrade=request.POST.get("ugrade","")
        hobbies=request.POST.get("hobbies","")
        languages=request.POST.get("languages","")
        about=request.POST.get("about","")
        projects=request.POST.get("projects","")
        branch=request.POST.get("branch","")

        profile=Profile(name=name,email=email,phone=phone,summary=summary,degree=degree,
        school=school,university=university,previous_work=previous_work,skills=skills,
        skills2=skills2,skills3=skills3,oskills=oskills,achievements=achievements,
        certify=certify,linkedin=linkedin,sgrade=sgrade,ugrade=ugrade,
        hobbies=hobbies,languages=languages,about=about,projects=projects,branch=branch)

        profile.save()
    return render(request,'pdf/accept.html')


def resume(request,id):
    user_profile=Profile.objects.get(pk=id)
    template= loader.get_template('pdf/resume.html')
    html=template.render({'user_profile':user_profile})
    options={
        'page-size':'Letter',
        'encoding':'UTF-8',
    }
    path_wkhtmltopdf = r'D:\wkhtmltox-0.12.6-1.mxe-cross-win64\wkhtmltox\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pdf = pdfkit.from_string(html,False,options,configuration=config)
    response=HttpResponse(pdf,content_type='application/pdf')
    response['content-Disposition']='attachment'
    filename='resume.pdf'
    return response

def list(request):
    profiles=Profile.objects.all()
    return render(request,'pdf/list.html',{'profiles':profiles})

