from django.shortcuts import render
from datetime import date, time, timedelta
import os 
from .models import Entry
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from collections import namedtuple
from collections import defaultdict
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

WB_ROOT = "/uploaded_workbooks"
    

# Create your views here.
def user_login(request):
    if request.method == "GET":
        return render(request, "mainapp/login.html")
    if request.method == "POST":
        error_msg = None
        usr = request.POST["username"]
        passwd = request.POST["password"]
        next_url = request.POST["next"]
        user = authenticate(username=usr, password=passwd)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(next_url)
            else:
                error_msg = u"账户已冻结"
        else:
            if User.objects.get(username=usr):
                error_msg = "用户密码错误"
            else:
                error_msg = "该账户不存在"
        return render(request,"mainapp/login.html",{"error": error_msg})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(request.META["HTTP_REFERER"])



def overview(request):
    yesterday = date.today() - timedelta(days=1)
    updates = Entry.objects.filter(last_updated=yesterday)
    return render(request, "mainapp/overview.html", {"updates_yesterday": updates, "all_entries": Entry.objects.all(), "page_title":"browse"})


def get_search_page(request):
    return render(request, "mainapp/search.html",{"page_title":"search"})


def _str_2_date(s):
    year, month, day = list(map(int, s.split("-")))
    return date(year=year, month=month, day=day)


def search(request):
    option = request.GET["option"]
    if option == "texture":
        keyword = request.GET["texture"]
    else:
        keyword = request.GET["process"]

    start_date = _str_2_date(request.GET["start-date"])
    end_date = _str_2_date(request.GET["end-date"])
    if option == "texture":
        return _search_by_texture(request, keyword, start_date, end_date)
    elif option == "process":
        return _search_by_process(request, keyword, start_date, end_date)

    
def _search_by_texture(request, texture, start_date, end_date):
    data_to_render = dict()
    query_info = {
        "texture": texture,
        "start_date": start_date,
        "end_date": end_date
    }
    data_to_render["query_info"] = query_info
    data_to_render["data"] = dict()
    
    labels_indexes = {
        "greign_yarn":("length", "sum_price"),
        "painting":("length", "sum_price"),
        "winding": ("length", "sum_price"),
        "weaving": ("length", "sum_price", "full_page_proof_sum"),
        "post_processing": ("length", "sum_price"),
        "bleaching":("length","sum_price", "design_drawing_sum"),
        "printing": ("length", "sum_price", "machine_work_sum", "layout_sum"),
        "storing": (
            "a_class_length", "a_class_roll_sum",
            "b_class_length", "b_class_roll_sum",
            "c_class_length", "c_class_roll_sum"),
        "delivering": ("length", "sum_price","roll_sum")
    }
    entry = Entry.objects.get(texture=texture)
    for process in labels_indexes:
        records = getattr(entry, process+"_summury").records.filter(
            created_at__gte=start_date, created_at__lte=end_date)
        sum_info = defaultdict(lambda: 0)
        labels = labels_indexes[process]
        for label in labels:
            sum_info[label] = sum(map(lambda record:getattr(record, label), records))
        data_to_render[process] = {"sum": sum_info, "records": records}
    data_to_render["page_title"] = "search"
    return render(request, "mainapp/search_by_texture_result.html", data_to_render)


def _search_by_process(request, process, start_date, end_date):
    process = process.replace("-", "_")
    labels_indexes = {
        "greign_yarn":{
            "zh_name":u"原纱",
            "summury_labels":("length", "sum_price"),
            "summury_labels_zh": ("花色编号", "总长", "总额"),
            "record_labels_zh":("录入时间","长度","单价","总价","供应商",)
        },
        "painting":{
            "zh_name":u"染色",
            "summury_labels":("length", "sum_price"),
            "summury_labels_zh": ("花色编号", "总长", "总额"),
            "record_labels_zh":("录入时间","长度","单价","总价","供应商",)
        },
    }
    query_info = {
        "process_zh": labels_indexes[process]["zh_name"],
        "process_en": process,
        "start_date": start_date,
        "end_date": end_date
    }
    summury_labels = labels_indexes[process]["summury_labels"]
    summury_labels_zh = labels_indexes[process]["summury_labels_zh"]
    record_labels_zh = labels_indexes[process]["record_labels_zh"]

    data = list()
    for entry in Entry.objects.all():
        records = getattr(entry, process + "_summury").records.filter(
            created_at__gte=start_date, created_at__lte=end_date)
        if records:
            texture = entry.texture
            summury_info = [texture,]
            for label in summury_labels:
                summury_info.append(sum(map(lambda record: getattr(record, label), records)))
            data.append(summury_info)
    
    data_to_render = {
        "query_info": query_info,
        "record_labels_zh": record_labels_zh,
        "summury_labels_zh": summury_labels_zh,
        "data": data,
        "url_placeholder":{"texture":"texture","process":"process", "start":"0000-00-00", "end":"0000-00-00"},
        "page_title": "search"
        }
    return render(request, "mainapp/search_by_process_result.html", data_to_render)


def get_records(request, texture, process, start_date_str, end_date_str):
    labels_indexes = {
        "greign_yarn":("created_at", "length", "price", "sum_price", "supplier"),
        "painting":("created_at", "length", "price", "sum_price", "supplier")
    }
    process = process.replace("-","_")
    start_date = _str_2_date(start_date_str)
    end_date = _str_2_date(end_date_str)
    entry = Entry.objects.get(texture=texture)
    records = getattr(entry, process + "_summury").records.filter(
        created_at__gte=start_date, created_at__lte=end_date)
    data = list()
    for record in records:
        record_info = list()
        for label in labels_indexes[process]:
            value = getattr(record, label)
            if isinstance(value, date):
                value = value.strftime("%Y-%m-%d")
            elif label == "supplier":
                value = value.name
            record_info.append(value)
        data.append(record_info)
    return JsonResponse({"data":data})


def import_data(request):
    if request.method == "GET":
        return render(request, "mainapp/import.html", {"page_title": "import"})
    elif request.method == "POST":
        src_file = request.FILES[0]
        process = request.POST.get("process")
        today = date.today()
        year, month, day = today.year, today.month, today.day
        dir_path = os.path.sep.join((WB_ROOT, year, month, day))
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
