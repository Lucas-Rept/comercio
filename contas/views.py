from django.shortcuts import render, redirect
from .forms import ClienteForm, ItemForm
from .models import Cliente, Item, Payment 
from datetime import datetime
from django.core.paginator import Paginator


# Create your views here.

def contas(request):
    section = 'Contas'
    name = ''
    if request.method == 'GET':
        name = request.GET.get('cliente') if request.GET.get('cliente') != None else ''
    
    clientes = Cliente.objects.filter(name__istartswith=name)
    form = ClienteForm()
    date = datetime.today().strftime('%d/%m/%Y')

    paginator = Paginator(clientes, 10)
    page = int(request.GET.get("page")) if request.GET.get("page") != None else 1
    page_obj = paginator.get_page(page)
    num_pages = paginator.num_pages

    urlContext= 'contas'
    pages = {'antPage': (page - 1), 'page': page, 'proxPage':(page + 1)}


    if request.method == 'POST' and "createSubmitButton" in request.POST:
        form = ClienteForm(request.POST)
        if form.is_valid():
            conta = form.save(commit=False)
            conta.name = conta.name.upper()
            conta.save()
            return redirect('contas')
    elif request.method == "POST" and "deleteSubmitButton" in request.POST:
        cliente_name = request.POST.get("cliente_name")
        cliente = Cliente.objects.get(name=cliente_name)
        cliente.delete()
        return redirect('contas')
    
    elif request.method == "POST" and "editSubmitButton" in request.POST:
        old_cliente_name = request.POST.get("old_cliente_name")
        new_cliente_name = request.POST.get("new_cliente_name")
        new_cliente_cellphone = request.POST.get("new_cliente_cellphone")
        cliente = Cliente.objects.get(name=old_cliente_name)
        cliente.name = new_cliente_name.upper()
        cliente.telefone = new_cliente_cellphone
        cliente.save()
        return redirect('contas')

    context = {'form':form, 'clientes':page_obj, 'date':date, 'section':section , 'pages':pages, 'urlContext':urlContext, 'num_pages':num_pages, 'name':name}
    return render(request, 'contas/contas.html', context)

def clientPage(request, pk):

    cliente = Cliente.objects.get(id=pk)
    form = ItemForm()
    
    section = 'Cliente'
    date = datetime.today().strftime('%d/%m/%Y')
    try:
        cliente = Cliente.objects.get(id=pk)
    except:
        return redirect('contas')
    items = cliente.item_set.all()
    payments = cliente.payment_set.all()
    items = items.union(payments).order_by('createdDate')

    if request.method == 'POST' and "createSubmitButton" in request.POST:
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.cliente = cliente
            item.save()
            return redirect('cliente', cliente.id)
        
    if request.method == "POST" and "deleteSubmitButton" in request.POST:
        id = request.POST.get("item_id")
        item = Item.objects.get(id=id)
        item.delete()
        return redirect('cliente', cliente.id)
    
    if request.method == "POST" and "editSubmitButton" in request.POST:
        id = request.POST.get("edit_item_id")
        item = Item.objects.get(id=id)
        item.name = request.POST.get("new_item_name")
        item.quantity = request.POST.get("new_item_quantity")
        item.price = request.POST.get("new_item_price")
        item.unit = request.POST.get("new_item_unit")
        item.save()

    if request.method == "POST" and "paymentSubmitButton" in request.POST:
        price = request.POST.get('price')
        Payment.objects.create(cliente=cliente, price=price)
        price = request.POST.get("price")

    context = {'cliente':cliente, 'date':date, 'section':section, 'items':items, 'form':form}
    return render(request, 'contas/cliente.html', context)

