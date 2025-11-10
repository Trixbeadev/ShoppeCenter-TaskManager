const api = "http://127.0.0.1:5000/tarefas"
let tarefaEditando = null

async function carregarTarefas() {
    const res = await fetch(api)
    const tarefas = await res.json()

    const lista = document.getElementById("lista")
    lista.innerHTML = ""

    tarefas.forEach(t => {
        const prioridadeClasse = t.prioridade.toLowerCase();
        const dataFormatada = t.prazo_entrega ? new Date(t.prazo_entrega).toLocaleDateString('pt-BR') : "Sem prazo";

        lista.innerHTML += `
        <div class="tarefa-card">
            <div class="tarefa-info">
                <div class="tarefa-titulo">${t.titulo}</div>
                <div class="tarefa-detalhes">
                    ${t.setor} | ${t.status}
                    <br>
                    <span class="badge ${prioridadeClasse}">${t.prioridade}</span>
                    <div>📅 ${dataFormatada}</div>
                    <div>👤 ${t.responsavel}</div>
                </div>
            </div>

            <div class="tarefa-acoes">
                <button class="edit-btn" onclick='abrirModal(${JSON.stringify(t)})'>✏</button>
                <button class="delete-btn" onclick="deletarTarefa(${t.id})">🗑</button>
            </div>
        </div>
        `
    })
}

async function criarTarefa() {
    try {
        // Validar campos obrigatórios
        if (!titulo.value) {
            alert('Por favor, preencha o título da tarefa');
            titulo.focus();
            return;
        }
        if (!setor.value) {
            alert('Por favor, selecione o setor');
            setor.focus();
            return;
        }
        if (!prioridade.value) {
            alert('Por favor, selecione a prioridade');
            prioridade.focus();
            return;
        }
        if (!responsavel.value) {
            alert('Por favor, preencha o responsável');
            responsavel.focus();
            return;
        }

        const nova = {
            titulo: titulo.value,
            setor: setor.value,
            prioridade: prioridade.value,
            status: status.value || 'A Fazer',
            responsavel: responsavel.value,
            prazo_entrega: prazo.value || null
        }

        console.log('Enviando dados para criar tarefa:', nova);

        const response = await fetch(api, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(nova)
        });

        const responseData = await response.json();

        if (!response.ok) {
            console.error('Erro ao criar tarefa:', responseData);
            alert(responseData.error || 'Erro ao criar tarefa');
            return;
        }

        console.log('Tarefa criada com sucesso:', responseData);

        // Limpar os campos após criar com sucesso
        titulo.value = '';
        setor.value = '';
        prioridade.value = '';
        status.value = 'A Fazer';
        responsavel.value = '';
        prazo.value = '';

        await carregarTarefas();
        
        alert('Tarefa criada com sucesso!');
    } catch (error) {
        console.error('Erro ao criar tarefa:', error);
        alert('Erro ao criar tarefa: ' + error.message);
    }
}

function abrirModal(tarefa) {
    tarefaEditando = tarefa.id
    editTitulo.value = tarefa.titulo
    editSetor.value = tarefa.setor
    editPrioridade.value = tarefa.prioridade
    editStatus.value = tarefa.status
    editResponsavel.value = tarefa.responsavel
    editPrazo.value = tarefa.prazo_entrega ?? ""

    modal.style.display = "flex"
}

function fecharModal() {
    modal.style.display = "none"
}

async function salvarEdicao() {
    const atualizada = {
        titulo: editTitulo.value,
        setor: editSetor.value,
        prioridade: editPrioridade.value,
        status: editStatus.value,
        responsavel: editResponsavel.value,
        prazo_entrega: editPrazo.value
    }

    await fetch(`${api}/${tarefaEditando}`, {
        method: "PUT",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(atualizada)
    })

    fecharModal()
    carregarTarefas()
}

async function deletarTarefa(id) {
    await fetch(`${api}/${id}`, { method: "DELETE" })
    carregarTarefas()
}

carregarTarefas()
