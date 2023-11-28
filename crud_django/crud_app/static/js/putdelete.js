
console.log("ID do Django:", id);
resourceId = id;
console.log(resourceId)
function alterarRecurso() {

    
    // Realiza uma requisição PUT para alterar as informações do recurso
    const newData = {
        name: document.getElementById('newClassName').value,
        status: document.getElementById('newClassStatus').value,
        intStatus: document.getElementById('newClassIntStatus').value
    };
    console.log(resourceId)
    fetch('/api/classes/' + resourceId + '/update/', {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(newData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Recurso alterado com sucesso:', data);
    })
    .catch(error => console.error('Erro ao alterar recurso:', error));
}

function deletarRecurso() {

    
    // Realiza uma requisição DELETE para deletar o recurso
    console.log(resourceId)
    fetch('/api/classes/' + resourceId + '/delete/', {
        method: 'DELETE',
    })
    .then(response => {
        if (response.ok) {
            console.log('Recurso deletado com sucesso.');
        } else {
            console.error('Erro ao deletar recurso.');
        }
    })
    .catch(error => console.error('Erro ao deletar recurso:', error));
}
