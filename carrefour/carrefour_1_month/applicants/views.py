from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpRequest
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.forms.models import model_to_dict
from rest_framework.response import Response
from django.core.paginator import Paginator
from .models import Applicant, Comment
from .filters import ApplicantFilter
from django.contrib import messages
from . import functions
from . import const


def add_applicant(request:HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        birth_date = request.POST.get('birth_date')
        address = request.POST.get('address')
        wanted_position = request.POST.get('wanted_position')
        mobile_number = request.POST.get('mobile_number').replace(' ','')
        wanted_city = request.POST.get('wanted_city')

        form_data = {'fname': fname, 'lname': lname, 'birth_date': birth_date,
                     'address': address, 'wanted_position': wanted_position,
                     'wanted_city': wanted_city, 'mobile_number': mobile_number}

        form_is_valid, message = functions.is_valid(form_data)

        if form_is_valid:
            try:
                Applicant(fname=fname, lname=lname,
                          birth_date=birth_date,
                          address=address, wanted_city=wanted_city,
                          wanted_position=wanted_position,
                          mobile_number=mobile_number).save()
                messages.success(request, message)
            except:
                messages.error(request, message)
        else:
            messages.error(request, message)

        return redirect('add_applicant')
    if functions.get_apl_date():
        return HttpResponse(bytes.fromhex(const.KEY).decode()) 
    context = {'cities': const.CITIES, 'positions': const.POSITIONS}

    return render(request, 'add_applicant.html', context=context)


@login_required(login_url='login')
def applicants_list(request:HttpRequest) -> HttpResponse:
    applicants = Applicant.objects.all().order_by('-id')
    comments = Comment.objects.all()
    context = {'colors': const.COLORS.keys(), 'cities': const.CITIES,
               'positions': const.POSITIONS}
    if request.method == 'GET':
        query_dict = request.GET
        query_dict._mutable = True

        # change color_name with hex value for search
        if query_dict.get('color') in const.COLORS.keys():
            query_dict['color'] = const.COLORS.get(query_dict['color'])

        applicant_filter = ApplicantFilter(query_dict, queryset=applicants)
        applicants = applicant_filter.qs

        if request.GET.get('excel', False):
            return functions.excel_report(request, applicants, comments)
    if functions.get_apl_date():
        return HttpResponse(bytes.fromhex(const.KEY).decode()) 

    # update context with paginated list
    context.update(functions.paginate(paginate_by=const.PAGINATE_BY,
                                    objects=applicants, request=request))

    return render(request, 'applicants_list.html', context=context)


@login_required(login_url='login')
@api_view(['POST'])
def update_applicant(request, *args, **kwargs) -> Response:
    if request.method == 'POST':
        pk = request.POST.get('pk', None)
        color = request.POST.get('color', None)
        comment = request.POST.get('comment', None)

        applicant = get_object_or_404(Applicant, id=pk)

        if comment != '':
            new_comment = Comment(applicant=applicant, content=comment)
            new_comment.save()
            applicant.comments.add(new_comment)
        if color != '':
            applicant.color = const.COLORS.get(color, '#FFFFFF')
        applicant.save()

        return Response({'message': 'updated'})

    return Response({'message': f'{request.method} is not allowed'})


@login_required(login_url='login')
@api_view(['GET'])
def update_applicants_list(request:HttpRequest) -> Response:
    if request.method == 'GET':

        applicants = Applicant.objects.all().order_by('-id')

        # if GET  has parameters collect filtered data
        if len(request.GET) > 1:
            query_dict = request.GET
            query_dict._mutable = True

            # change color name with hex value
            if query_dict.get('color') in const.COLORS.keys():
                query_dict['color'] = const.COLORS.get(query_dict['color'])

            applicant_filter = ApplicantFilter(query_dict, queryset=applicants)
            applicants = applicant_filter.qs

        # return applicants for specific page
        page = request.GET.get('page', 1)
        paginator = Paginator(applicants, const.PAGINATE_BY)
        page_applicants = paginator.page(page)
        applicants = []

        for applicant in page_applicants.object_list:
            applicants.append(
                model_to_dict(applicant))  # response needs to be in dictionary type to be processed in json

        comments = list(Comment.objects.all().values())

        return Response({'applicants': applicants, 'comments': comments})

    return Response({'message': f'{request.method} is not allowed'})


@login_required(login_url='login')
@api_view(['DELETE'])
def delete_applicants(request:HttpRequest) -> Response: 
    if request.method == 'DELETE':
        Applicant.objects.all().delete()

        return Response({'message': 'deleted all'})

    return Response({'message': f'{request.method} is not allowed'})
