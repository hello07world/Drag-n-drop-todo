from django.shortcuts import render
from django.http import JsonResponse
from app.models import Todo
from django.views.decorators.csrf import csrf_exempt

# Create your views here. 

@csrf_exempt
def home(request):

    if request.method=='POST' and request.POST['name']=='add_todo_button':
        todo_ipnut=request.POST.get('todo')
        print(todo_ipnut)
        
        if todo_ipnut:
            Todo.objects.create(todo=todo_ipnut)
            
    if request.method=='POST' and request.POST['name']=='post_item':
        id=int(request.POST.get('itemId'))
        drop=request.POST.get('dropBlockId')
        todo_obj=Todo.objects.get(id=id)
        print(todo_obj)            
        print(drop)
        
        # pending update 
        if drop=='pending':
            todo_obj.status='pending'
            todo_obj.save()
            print('updated successfully ')
            
            response={'status':200}
            return JsonResponse(response)
        
        # doing update
        if drop=='doing':
            todo_obj.status='doing'
            todo_obj.save()
            print('updated successfully ')
            
            response={'status':200}
            return JsonResponse(response)
        
            
        # done update
        if drop=='done':
            todo_obj.status='done'
            todo_obj.save()
            print('updated successfully ')
            
            response={'status':200}
            return JsonResponse(response)
        
            
        # trash update
        if drop=='trash':
            todo_obj.status='trash'
            todo_obj.save()
            print('updated successfully ')

            response={'status':200}
            return JsonResponse(response)
        

    pending=Todo.objects.filter(status='pending')
    doing=Todo.objects.filter(status='doing')
    done=Todo.objects.filter(status='done')
    trash=Todo.objects.filter(status='trash')

    # print(pending)
    # print(doing)
    # print(done)
    # print(trash)
    context={
        'pendings':pending,
        'doings':doing,
        'dones':done,
        'trashs':trash,
    }
    return render(request, 'index.html' , context)