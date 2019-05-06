from django.shortcuts import render
from django.views.generic.base import View

from .models import Content

# Create your views here.


class ContentView(View):

    def get(self, request):
        all_content = Content.objects.all()
        return render(request, 'shows/index.html', {'all_content': all_content})

    def post(self, request):
        content_area = request.POST.get('contentArea')
        if content_area is not '' and len(content_area) < 200:
            content = Content()
            content.content_text = content_area
            content.save()

        all_content = Content.objects.all()
        return render(request, 'shows/index.html', {'all_content': all_content})
