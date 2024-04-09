from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from .models import *
from datetime import datetime

# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def list_staff(request):
    staffs = Staff.objects.all().values()
    template = loader.get_template('list_staff.html')
    context={
        'staffs': staffs
    }
    return HttpResponse(template.render(context, request))

def list_branch(request):
    branches = Branch.objects.all().values()
    template = loader.get_template('list_branch.html')
    context={
        'branches': branches
    }
    return HttpResponse(template.render(context, request))

def list_clients(request):
    clients = Client.objects.all().values()
    template = loader.get_template('list_clients.html')
    context={
        'clients': clients
    }
    return HttpResponse(template.render(context, request))

def find_branch(request):
    template = loader.get_template('find_branch.html')
    if request.method == 'POST':
        branch_class = Branch()
        branchno = request.POST['branchno']
        branch = branch_class.search_branch(branchno)
        context = {
            'branch': f'Branch {branch[2]} Address: {branch[1][0]}' if branch[1] != None else 'Branch not found',
            'branch_found': f'{branch[0]}'
        }
        if branch[0]:
            return render(request, 'find_branch.html', context)
        return HttpResponse(template.render(context, request))
    return render(request, 'find_branch.html')

##def hire_staff(request):
  ##  template = loader.get_template('hire_staff.html')
    ##return HttpResponse(template.render())

def hire_staff(request):
    template = loader.get_template('hire_staff.html')
    if request.method == 'POST':
        staffno = request.POST['staffno']
        fname = request.POST['fname']
        lname = request.POST['lname']
        position = request.POST['position']
        sex = request.POST['sex']
        dob = request.POST['dob']
        salary = request.POST['salary']
        branchno = request.POST['branchno']
        telephone = request.POST['telephone']
        mobile = request.POST['mobile']
        email = request.POST['email']

        staff = Staff()
        hire_success = staff.hire_staff(staffno, fname, lname, position,sex, dob, salary, branchno, telephone, mobile, email)
        if hire_success:
            staffs = Staff.objects.all().values()
        return render(request, 'hire_staff.html', {'staffs':staffs, 'hire_success': hire_success})
    return render(request, 'hire_staff.html')

def register_client(request):
    template = loader.get_template('register_client.html')
    if request.method == 'POST':
        clientno = request.POST['clientno']
        fname = request.POST['fname']
        lname = request.POST['lname']
        telno = request.POST['telno']
        street = request.POST['street']
        city = request.POST['city']
        email = request.POST['email']
        preftype = request.POST['preftype']
        maxrent = request.POST['maxrent']

        client = Client()
        register_success = client.register_client(clientno, fname, lname, telno, street, city, email, preftype, maxrent)
        if register_success:
            clients = Client.objects.all().values()
        return render(request, 'register_client.html', {'clients':clients, 'register_success': register_success})
    return render(request, 'register_client.html')

def update_staff(request):
    print(request.POST)
    staffs = Staff.objects.all().values()
    if request.method == 'POST':
        staffno = request.POST['staffno']
        salary = request.POST['salary']
        telephone = request.POST['telephone']
        mobile = request.POST['mobile']
        email = request.POST['email']

        staff = Staff()
        updated_sucessfully = staff.update_staff(staffno, salary, telephone, mobile, email)
        if updated_sucessfully:
            staffs = Staff.objects.all().values()
    
        return render(request, 'list_staff.html', {'staffs':staffs,'update_success': updated_sucessfully})
    return redirect('list_staff')

def update_client(request):
    print(request.POST)
    if request.method == 'POST':
        clientno = request.POST['clientno']
        fname = request.POST['fname']
        lname = request.POST['lname']
        telno = request.POST['telno']
        street = request.POST['street']
        city = request.POST['city']
        email = request.POST['email']
        preftype = request.POST['preftype']
        maxrent = request.POST['maxrent']

        client = Client()
        update_success = client.update_client(clientno, fname, lname, telno, street, city, email, preftype, maxrent)
        if update_success:
            clients = Client.objects.all().values()
    
        return render(request, 'list_clients.html', {'clients':clients,'update_success': update_success})
    return redirect('list_clients')
    
def update_branch(request):
    branches = Branch.objects.all().values()
    if request.method == 'POST':
        branchno = request.POST['branchno']
        street = request.POST['street']
        city = request.POST['city']
        postcode = request.POST['postalcode']

        branch = Branch()
        update_success = branch.update_branch(branchno, street, city, postcode)
        
        if update_success:
            branches = Branch.objects.all().values()
        return render(request, 'list_branch.html', {'branches': branches, 'update_success': update_success})
    
    return redirect('list_branch')

def open_branch(request):
    branches = Branch.objects.all().values()
    if request.method == 'POST':
        branchno = request.POST['branchno']
        street = request.POST['street']
        city = request.POST['city']
        postcode = request.POST['postalcode']

        branch = Branch()
        create_success = branch.open_branch(branchno, street, city, postcode)
        if create_success:
            branches = Branch.objects.all().values()
        return render(request, 'open_branch.html', {'branches':branches, 'create_success': create_success})
    
    return render(request, 'open_branch.html')