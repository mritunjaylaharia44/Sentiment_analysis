from django.shortcuts import render

from sentiment_model import sentiment_analysis


# Create your views here.
def home(request):

    # logic
    if request.method == 'POST':
        text = request.POST.get('comment')
        res, conf = sentiment_analysis.sentiment(text)
        conf = conf*100
        context = {
            'text': text,
            'class': res,
            'confidence': conf,
        }
        return render(request, 'analysis/home.html', context)

    context = {}
    return render(request, 'analysis/home.html', context)
