// app_create.js

Id = ids;
Classes = classes;


// Exemplo de listas Id e Classes

// Função para encontrar o id correspondente a uma classname
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

function createClass(event) {
    event.preventDefault();

    const newName = document.getElementById('newClassName').value;
    const newStatus = document.getElementById('newClassStatus').value;

    console.log(newName)
    console.log(newStatus)

    let idCorrespondente = encontrarIdPorClasse(newStatus)

    fetch('/api/personagem/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            name: newName,
            classes: idCorrespondente,

        }),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Classe criada com sucesso:', data);
        document.getElementById('createForm').style.display = 'none';
        fillTable();  // Atualiza a tabela após a criação bem-sucedida
    })
    .catch(error => console.error('Erro ao criar classe:', error));
}
