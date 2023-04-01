    # try:
    if request.method=='POST':
        todo=request.POST.get('todo')
        if todo:
            todo_model=Todo(todo=todo)
            todo_model.save()
    
    if request.method=='GET':
        id=request.GET.get('id')
        if id:
            id_field=id.split('_')
            id, field  =id_field
            print( 'ID And Field :  ', id , field )
        
        # get todo object
            todo_object=Todo.objects.get(id=int(id))
            print(todo_object)
            
            if field=='todo':
                Todo.objects.filter(id=int(id)).update(todo='',doing='sada')
                print('object saved successsfully')
                
            if field=='doing':
                pass
            
            if field=='done':
                pass
            
            if field=='trash':
                pass
            
    # except Exception as e:
        # print(e)