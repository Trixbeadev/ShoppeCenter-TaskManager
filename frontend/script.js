const api = "http://127.0.0.1:5000/tarefas"

async function carregarTarefas() {
    const res = await fetch(api)
    const tarefas = await res.json()

    const lista = document.getElementById("lista")
    lista.innerHTML = ""

    tarefas.forEach(t => {
        const prioridadeClasse = t.prioridade.toLowerCase()

        lista.innerHTML += `
        <div class="tarefa-card">
            <div>
                <b>${t.titulo}</b><br>
                ${t.setor} | ${t.status} <br>
                <span class="badge ${prioridadeClasse}">${t.prioridade}</span>
                <div>📅 ${t.prazo_entrega ?? "Sem prazo"}</div>
            </div>
            <button class="delete-btn" onclick="deletarTarefa(${t.id})">🗑</button>
        </div>
        `
    })
}

async function criarTarefa() {
    const nova = {
        titulo: titulo.value,
        setor: setor.value,
        prioridade: prioridade.value,
        status: status.value,
        responsavel: responsavel.value,
        prazo_entrega: prazo.value
    }

    await fetch(api, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(nova)
    })

    carregarTarefas()
}

async function deletarTarefa(id) {
    await fetch(`${api}/${id}`, { method: "DELETE" })
    carregarTarefas()
}

carregarTarefas()
