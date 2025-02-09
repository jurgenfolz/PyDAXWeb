# homepage/views.py
from django.shortcuts import render
from django.http import HttpResponse
from .forms import DAXForm
from PyDAX import DAXExpression
from .models import DAXExpressionModel

def home_view(request):
    result_clean = None
    result_comments = None

    if request.method == 'POST':
        form = DAXForm(request.POST)
        if form.is_valid():
            user_dax = form.cleaned_data['dax_expression']

            # 1) Save the original expression in the database
            record = DAXExpressionModel.objects.create(expression_text=user_dax)

            # 2) Process it with PyDAX
            expression = DAXExpression(user_dax)

            # 3) Determine which button was clicked
            if 'extract_comments' in request.POST:
                # Suppose PyDAX can return comments as a string
                result_comments = expression.comments  

            elif 'remove_comments' in request.POST:
                result_clean = expression.dax_expression_no_comments
    else:
        form = DAXForm()

    context = {
        'form': form,
        'result_clean': result_clean,
        'result_comments': result_comments
    }
    return render(request, 'home.html', context)
