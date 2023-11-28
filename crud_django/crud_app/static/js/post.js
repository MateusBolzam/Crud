// app_create.js
function createClass(event) {
    event.preventDefault();

    const newName = document.getElementById('newClassName').value;
    const newStatus = document.getElementById('newClassStatus').value;
    const newIntStatus = document.getElementById('newClassIntStatus').value;

    fetch('/api/classes/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            name: newName,
            status: newStatus,
            intStatus: newIntStatus,
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
