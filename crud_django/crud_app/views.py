from django.shortcuts import render
# api/views.py
from .models import classe, personagem


# classe Views
def create_class_view(request):
    # Garante que as opções específicas do modelo de status sejam carregadas
    status_options = [status[0] for status in classe._meta.get_field('status').choices]

    # Renderize o template passando as opções de status para o contexto
    return render(request, 'create.html', {'status_options': status_options})

def list_classes_view(request):
    # Lógica para obter todas as instâncias do modelo e renderizar a página de listagem
    classes = classe.objects.all()
    return render(request, 'index.html', {'classes': classes})

def update_delete_view(request, class_id):

    c = classe.objects.get(pk=class_id)
    
    status_field = classe._meta.get_field('status')
    status_options = [status[0] for status in status_field.choices]

    status_options.remove(c.status)
    status_options.insert(0, c.status)
    
    # Renderiza a página de atualização/exclusão com o contexto
    return render(request, 'update_delete.html',{'default_class_name':c.name,'status_options': status_options,'default_int_status':c.intStatus,'id': class_id})

# personagem views
def create_personagem_view(request):
    # Garante que as opções específicas do modelo de status sejam carregadas

    classes_instances = classe.objects.all()

    # Extraia os nomes das instâncias do modelo 'classe'
    classes_names = [c.name for c in classes_instances]
    classes_ids = [c.pk for c in classes_instances]

    print(classes_ids)
    print(classes_names)
    # Renderize o template passando as opções de status para o contexto
    return render(request, 'pcreate.html', {'classes_options': classes_names,'ids': classes_ids})

def list_personagem_view(request):
    # Lógica para obter todas as instâncias do modelo e renderizar a página de listagem
    persona = personagem.objects.all()
    return render(request, 'pindex.html', {'personagem': persona})

def update_delete_persona(request, persona_id):
    p = personagem.objects.get(pk=persona_id)
    
    classes_instances = classe.objects.all()
    
    # Extraia os nomes das instâncias do modelo 'classe'
    classes_names = [c.name for c in classes_instances]
    classes_ids = [c.pk for c in classes_instances]

    class_ordem = [c.name for c in classes_instances]
    class_ordem.remove(p.classes.name)
    
    # Adiciona o nome da classe atual de volta no início da lista
    class_ordem.insert(0, p.classes.name)
    print(class_ordem)
    print(classes_names)


    # Renderiza a página de atualização/exclusão com o contexto
    return render(request, 'pupdate_delete.html', {'default_class_name': p.name, 'classes_ordem': classes_names, 'classes_options': class_ordem, 'id': persona_id,'ids': classes_ids})