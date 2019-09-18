from django.shortcuts import render
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.db.models import Min
# new line added
from .models import top_house_details,contract_details,agent_details,defualt_detials,index_house_details,index_defoult_change,why_we_choose_details,ledership_details,blog_post_create,about_page_defaut
from .choice import select_city,offer_type
# Create your views here.
from django.http import HttpResponse
def index(request):
    details_house = top_house_details.objects.all()
    get_index_house_details = index_house_details.objects.all()
    get_index_house_details.aggregate(Min('rent_price'))
    # get_index_house_details = index_house_details.objects.filter(price_range(min_price,max_price))
    # get_index_house_details = index_house_details.objects.filter(max('rent_price'))
    get_index_defoult_change = index_defoult_change.objects.all()
    get_why_we_choose_details = why_we_choose_details.objects.all()
    get_agent_details = agent_details.objects.all()
    paginator = Paginator(get_index_house_details,6)
    page = request.GET.get('page')
    paged_all_house = paginator.get_page(page)
    get_default_details = defualt_detials.objects.all()

    context = {
        'details_house': details_house,
        'get_index_house_details':paged_all_house,
        'get_index_defoult_change':get_index_defoult_change,
        'get_why_we_choose_details':get_why_we_choose_details,
        'get_agent_details' : get_agent_details,
        'select_city' : select_city,
        'offer_type' : offer_type,
        'get_default_details' : get_default_details


    }

    return render(request,'pages/index.html',context)


def buy(request):
    get_index_house_details = index_house_details.objects.all()
    get_why_we_choose_details = why_we_choose_details.objects.all()
    get_index_defoult_change = index_defoult_change.objects.all()
    get_default_details = defualt_detials.objects.all()

    paginator = Paginator(get_index_house_details,3)
    page = request.GET.get('page')
    paged_all_house = paginator.get_page(page)
         
    context = {
        'get_index_house_details': paged_all_house,
        'get_why_we_choose_details':get_why_we_choose_details,
        'get_index_defoult_change':get_index_defoult_change,
        'get_default_details' : get_default_details





    }

    return render(request,'pages/buy.html',context)


def rent(request):
    get_why_we_choose_details = why_we_choose_details.objects.all()
    get_index_house_details = index_house_details.objects.all()
    get_index_defoult_change = index_defoult_change.objects.all()
    get_default_details = defualt_detials.objects.all()

    paginator = Paginator(get_index_house_details,3)
    page = request.GET.get('page')
    paged_all_house = paginator.get_page(page)
  
    context = {
        'get_why_we_choose_details':get_why_we_choose_details,
        'get_index_house_details':paged_all_house,
        'get_index_defoult_change':get_index_defoult_change,
        'get_default_details' : get_default_details


    }

    return render(request,'pages/rent.html',context)


def blog(request):
    get_blog_post = blog_post_create.objects.all()
    get_default_details = defualt_detials.objects.all()
    paginator = Paginator(get_blog_post,2)
    page = request.GET.get('page')
    paged_all_post = paginator.get_page(page)
    context = {
        'get_blog_post' : paged_all_post,
        'get_default_details' : get_default_details,
        
        
    }
    return render(request,'pages/blog.html',context)


def contract(request):
    get_contract_details = contract_details.objects.all()
    get_agent_details = agent_details.objects.all()
    get_default_details = defualt_detials.objects.all()

    context = {
        'get_contract_details' : get_contract_details,
         'get_agent_details' : get_agent_details,
         'get_default_details' : get_default_details
    }
    return render(request,'pages/contract.html',context)


def about(request):
    get_ledership_details = ledership_details.objects.all()
    get_agent_details = agent_details.objects.all()
    get_default_details = defualt_detials.objects.all()
    get_about_page_defoult = about_page_defaut.objects.all()

    context = {
        'get_ledership_details' : get_ledership_details,
        'get_agent_details' : get_agent_details,
        'get_default_details' : get_default_details,
        'get_about_page_defoult' :get_about_page_defoult


        

    }
    return render(request,'pages/about.html',context)



# def  base(request):
#     get_default_details = defualt_detials.objects.all()

#     context = {
#         'get_default_details' : get_default_details
#     }
    
#     return render(request,'partials/_footer.html',context)


def serch(request):
    return render(request,'pages/serch.html')