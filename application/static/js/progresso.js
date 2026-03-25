const Progresso = {

  // Retorna a chave única por curso
  _chave(conteudoId) {
    return `progresso_curso_${conteudoId}`;
  },

  // Carrega o estado salvo ou retorna objeto vazio
  carregar(conteudoId) {
    const raw = localStorage.getItem(this._chave(conteudoId));
    return raw ? JSON.parse(raw) : { aulas: {} };
  },

  // Salva o estado no localStorage
  salvar(conteudoId, estado) {
    localStorage.setItem(this._chave(conteudoId), JSON.stringify(estado));
  },

  // Marca/desmarca uma aula e recalcula o módulo
  toggleAula(conteudoId, aulaId, aulasDosModulos) {
    const estado = this.carregar(conteudoId);
    const key = String(aulaId);

    estado.aulas[key] = !estado.aulas[key];

    this.salvar(conteudoId, estado);
    this.aplicarUI(estado, aulasDosModulos);
    return estado;
  },

  // Aplica checks nas aulas e módulos na sidebar
  aplicarUI(estado, aulasDosModulos) {
    // Aulas
    document.querySelectorAll('[data-aula-id]').forEach(el => {
      const id = el.dataset.aulaId;
      el.classList.toggle('aula-concluida', !!estado.aulas[id]);
      const check = el.querySelector('.check-aula');
      if (check) check.style.display = estado.aulas[id] ? 'inline' : 'none';
    });

    // Módulos — verifica se todas as aulas do módulo estão concluídas
    document.querySelectorAll('[data-modulo-id]').forEach(el => {
      const moduloId = el.dataset.moduloId;
      const aulas = aulasDosModulos[moduloId] || [];
      const todasconcluidas = aulas.length > 0 && aulas.every(id => !!estado.aulas[String(id)]);
      el.classList.toggle('modulo-concluido', todasconcluidas);
      const check = el.querySelector('.check-modulo');
      if (check) check.style.display = todasconcluidas ? 'inline' : 'none';
    });
  },

  // Inicializa a UI ao carregar a página
  init(conteudoId, aulasDosModulos) {
    const estado = this.carregar(conteudoId);
    this.aplicarUI(estado, aulasDosModulos);
  }
};