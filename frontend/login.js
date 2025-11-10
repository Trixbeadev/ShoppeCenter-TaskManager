const api = "http://127.0.0.1:5000";

// Verificar se usuário já está logado
async function verificarLogin() {
    try {
        const response = await fetch(`${api}/auth/verificar`, {
            credentials: 'include'
        });
        
        if (response.ok) {
            window.location.href = "/tarefas.html";
        }
    } catch (error) {
        console.error('Erro ao verificar login:', error);
    }
}

async function fazerLogin() {
    try {
        const email = document.getElementById('email').value;
        const senha = document.getElementById('senha').value;

        if (!email || !senha) {
            alert('Por favor, preencha todos os campos');
            return;
        }

        const response = await fetch(`${api}/auth/login`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email, senha }),
            credentials: 'include'
        });

        const data = await response.json();

        if (response.ok) {
            alert('Login realizado com sucesso!');
            window.location.href = "/tarefas.html";
        } else {
            alert(data.error || 'Erro ao fazer login');
        }
    } catch (error) {
        console.error('Erro:', error);
        alert('Erro ao fazer login');
    }
}

async function fazerCadastro() {
    try {
        const nome = document.getElementById('nomeRegistro').value;
        const email = document.getElementById('emailRegistro').value;
        const senha = document.getElementById('senhaRegistro').value;

        if (!nome || !email || !senha) {
            alert('Por favor, preencha todos os campos');
            return;
        }

        const response = await fetch(`${api}/auth/cadastro`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ nome, email, senha })
        });

        const data = await response.json();

        if (response.ok) {
            alert('Cadastro realizado com sucesso! Faça login para continuar.');
            mostrarLogin();
        } else {
            alert(data.error || 'Erro ao fazer cadastro');
        }
    } catch (error) {
        console.error('Erro:', error);
        alert('Erro ao fazer cadastro');
    }
}

function mostrarCadastro() {
    document.getElementById('loginForm').style.display = 'none';
    document.getElementById('cadastroForm').style.display = 'block';
}

function mostrarLogin() {
    document.getElementById('cadastroForm').style.display = 'none';
    document.getElementById('loginForm').style.display = 'block';
}

// Verificar login ao carregar a página
verificarLogin();