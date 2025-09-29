

from datetime import datetime, timedelta
from typing import List, Dict, Callable, Any
import json


class Biblioteca:

    
    def __init__(self):
        self.livros = []
        self.emprestimos = []
        self.contador_id = 1
    
    def cadastrar_livro(self, titulo: str, autor: str, ano: int, categoria: str) -> Dict[str, Any]:
         "Cadastrar"
        livro = {
            'id': self.contador_id,
            'titulo': titulo,
            'autor': autor,
            'ano': ano,
            'categoria': categoria,
            'disponivel': True,
            'data_cadastro': datetime.now().isoformat()
        }
        
        self.livros.append(livro)
        self.contador_id += 1
        
        return livro
    
    def buscar_livros(self, criterio: str, valor: str) -> List[Dict[str, Any]]:
        "Busca livros"
        
        filtro_lambda = lambda livro: valor.lower() in livro[criterio].lower()
        
        return list(filter(filtro_lambda, self.livros))
    
    def filtrar_livros_por_categoria(self, categoria: str) -> List[Dict[str, Any]]:
        "Filtra livros por categoria"
        
        return list(filter(lambda livro: livro['categoria'] == categoria, self.livros))
    
    def obter_titulos_livros(self, livros: List[Dict[str, Any]]) -> List[str]:
        "Extrai títulos de uma lista"
       
        return [livro['titulo'] for livro in livros]
    
    def criar_contador_emprestimos(self) -> Callable[[], int]:
        "Cria um contador de empréstimos"
        
        contador = 0
        
        def incrementar_contador():
            nonlocal contador
            contador += 1
            return contador
        
        return incrementar_contador
    
    def aplicar_desconto_livros(self, livros: List[Dict[str, Any]], 
                               funcao_desconto: Callable[[Dict[str, Any]], Dict[str, Any]]) -> List[Dict[str, Any]]:
        "Aplica uma função de desconto a uma lista de livros"
       
        return list(map(funcao_desconto, livros))
    
    def emprestar_livro(self, livro_id: int, pessoa: str) -> Dict[str, Any]:
        "Registra empréstimo de um livro"
        livro = next((l for l in self.livros if l['id'] == livro_id), None)
        
        if not livro:
            raise ValueError("Livro não encontrado")
        
        if not livro['disponivel']:
            raise ValueError("Livro não está disponível")
        
        emprestimo = {
            'id': len(self.emprestimos) + 1,
            'livro_id': livro_id,
            'pessoa': pessoa,
            'data_emprestimo': datetime.now().isoformat(),
            'data_vencimento': (datetime.now() + timedelta(days=15)).isoformat(),
            'devolvido': False
        }
        
        self.emprestimos.append(emprestimo)
        livro['disponivel'] = False
        
        return emprestimo
    
    def devolver_livro(self, emprestimo_id: int) -> Dict[str, Any]:
        "Registra devolução de um livro"
        
        emprestimo = next((e for e in self.emprestimos if e['id'] == emprestimo_id), None)
        
        if not emprestimo:
            raise ValueError("Empréstimo não encontrado")
        
        if emprestimo['devolvido']:
            raise ValueError("Livro já foi devolvido")
        
       
        data_vencimento = datetime.fromisoformat(emprestimo['data_vencimento'])
        data_devolucao = datetime.now()
        
        multa = 0
        if data_devolucao > data_vencimento:
            dias_atraso = (data_devolucao - data_vencimento).days
            multa = dias_atraso * 2.0  
        
        emprestimo['devolvido'] = True
        emprestimo['data_devolucao'] = data_devolucao.isoformat()
        emprestimo['multa'] = multa
        
        
        livro = next((l for l in self.livros if l['id'] == emprestimo['livro_id']), None)
        if livro:
            livro['disponivel'] = True
        
        return emprestimo
    
    def gerar_relatorio(self) -> Dict[str, Any]:
        "Gera relatório sobre o acervo"
        
        total_livros = len(self.livros)
        livros_disponiveis = len([l for l in self.livros if l['disponivel']])
        livros_emprestados = total_livros - livros_disponiveis
        
       
        livros_por_categoria = {}
        for livro in self.livros:
            categoria = livro['categoria']
            if categoria not in livros_por_categoria:
                livros_por_categoria[categoria] = []
            livros_por_categoria[categoria].append(livro['titulo'])
        
      
        emprestimos_em_atraso = []
        for emprestimo in self.emprestimos:
            if not emprestimo['devolvido']:
                data_vencimento = datetime.fromisoformat(emprestimo['data_vencimento'])
                if datetime.now() > data_vencimento:
                    emprestimos_em_atraso.append(emprestimo)
        
        return {
            'total_livros': total_livros,
            'livros_disponiveis': livros_disponiveis,
            'livros_emprestados': livros_emprestados,
            'livros_por_categoria': livros_por_categoria,
            'emprestimos_em_atraso': len(emprestimos_em_atraso),
            'data_relatorio': datetime.now().isoformat()
        }
    
    def salvar_dados(self, arquivo: str = 'biblioteca.json'):
        "Salva os dados em JSON"
        dados = {
            'livros': self.livros,
            'emprestimos': self.emprestimos,
            'contador_id': self.contador_id
        }
        
        with open(arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)
    
    def carregar_dados(self, arquivo: str = 'biblioteca.json'):
        "Carrega os dados da biblioteca de arquivo JSON"
        try:
            with open(arquivo, 'r', encoding='utf-8') as f:
                dados = json.load(f)
            
            self.livros = dados.get('livros', [])
            self.emprestimos = dados.get('emprestimos', [])
            self.contador_id = dados.get('contador_id', 1)
        except FileNotFoundError:
            print("Arquivo não encontrado. Iniciando biblioteca vazia.")




def criar_funcao_desconto(percentual: float) -> Callable[[Dict[str, Any]], Dict[str, Any]]:
    "Cria uma função de desconto"
    
    def aplicar_desconto(livro: Dict[str, Any]) -> Dict[str, Any]:
        livro_com_desconto = livro.copy()
        if 'preco' in livro_com_desconto:
            livro_com_desconto['preco'] *= (1 - percentual)
        return livro_com_desconto
    
    return aplicar_desconto


def processar_livros_funcional(livros: List[Dict[str, Any]], 
                              filtro: Callable[[Dict[str, Any]], bool],
                              transformacao: Callable[[Dict[str, Any]], Any]) -> List[Any]:
    "Processa livros"
                                  
    return [transformacao(livro) for livro in livros if filtro(livro)]


def calcular_estatisticas_livros(livros: List[Dict[str, Any]]) -> Dict[str, Any]:
    "Calcula estatísticas dos livros"
    if not livros:
        return {'total': 0, 'media_ano': 0, 'categorias_unicas': 0}
    
  
    anos = [livro['ano'] for livro in livros]
    
  
    categorias_unicas = len(set(livro['categoria'] for livro in livros))
    
    return {
        'total': len(livros),
        'media_ano': sum(anos) / len(anos),
        'categorias_unicas': categorias_unicas,
        'ano_mais_antigo': min(anos),
        'ano_mais_recente': max(anos)
    }
