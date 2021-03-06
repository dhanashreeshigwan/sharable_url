import json
from django.views import View
from django.shortcuts import render
from django.core.signing import Signer
from django.http import HttpResponse

from .apps.snippet.forms import SnippetForm
from shreableUrl.apps.snippet.models import Snippet
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core import signing


class SnippetView(View):
    """
      Create Snippet
    """
    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, *args, **kwargs):
        return super(SnippetView,self).dispatch(*args, **kwargs)

    def get(self,request):
        form=SnippetForm()
        return render(request, 'snippet.html', {'form': form, 'msg': '', 'snippet_id': 0})

    def post(self,request):
        sid=0
        msg = ''
        form=SnippetForm(request.POST)
        if form.is_valid():
            # signer = Signer(form.cleaned_data['key'])
            data = signing.dumps({"key": form.cleaned_data['data']})
            s=Snippet.objects.create(data=data,\
                                     key=form.cleaned_data['key'])
            sid = s.id
            url = request.get_host()+"/snippet/"+str(sid)
            update_snippet = Snippet.objects.filter(id=sid).update(url=url)
            msg = 'Snippet Successfully created'
        else:
            msg = "Snippet with this key already exist"
        return render(request, 'snippet.html',\
               {'form': form,'msg':msg,\
                'snippet_id':sid,'server':request.get_host()})

class KeyLogin(View):
    """
      Receive key as input
    """
    def get(self,request,**kwargs):
        key=None
        if request.GET.get("key_id"):
            key = request.GET.get("key_id")

        if key:
            return HttpResponse(json.dumps({'key':key}))
        return render(request, 'validate_key.html', {'id':kwargs['snippet_id']})

class SnippetDetailView(View):
    """
      Display Snippet Details
    """
    def post(self,request):
        s = Snippet.objects.get(id=request.POST['snippet_id'])
        if request.POST['key'] == s.key:
            # signer = Signer(s.key)
            val = signing.loads(s.data)
            return render(request,'snippet_detail.html',{'data': val.get('key'),\
                                                         'flag': True})
        else:
            return render(request, 'snippet_detail.html', {'flag': False })

