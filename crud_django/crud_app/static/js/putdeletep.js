Id = ids;
Classes = classes;
resourceId = id;
function alterarRecurso() {

    function encontrarIdPorClasse(classname) {
        // Encontrar a posição da classname na lista Classes
        let posicao = Classes.indexOf(classname);
    
        // Verificar se a classname foi encontrada
        if (posicao !== -1) {
            // Acessar o id correspondente na lista Id
            let idCorrespondente = Id[posicao];
            return idCorrespondente;
        } else {
            // Se a classname não for encontrada, retornar algo indicativo, como null
            return null;
        }
    }
    newStatus = document.getElementById('newClassStatus').value;
    let idCorrespondente = encontrarIdPorClasse(newStatus);
    // Realiza uma requisição PUT para alterar as informações do recurso
    const newData = {
        name: document.getElementById('newClassName').value,
        classes: idCorrespondente

    };
    console.log(newData)
    console.log(resourceId)
    fetch('/api/personagem/' + resourceId + '/update/', {
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
    fetch('/api/personagem/' + resourceId + '/delete/', {
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
