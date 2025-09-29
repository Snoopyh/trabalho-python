"Testes para o Sistema de Gerenciamento de Biblioteca Pessoal"
"Demonstra casos de teste abrangentes para todas as funcionalidades"

import unittest
from datetime import datetime, timedelta
from biblioteca import Biblioteca, criar_funcao_desconto, processar_livros_funcional, calcular_estatisticas_livros


class TestBiblioteca(unittest.TestCase):
   "Classe de testes para o sistema de biblioteca"
    
    def setUp(self):
        """Configuração inicial para cada teste"""
        self.biblioteca = Biblioteca()
        
        
        self.livro1 = self.biblioteca.cadastrar_livro(
            "O Senhor dos Anéis", "J.R.R. Tolkien", 1954, "Fantasia"
        )
        self.livro2 = self.biblioteca.cadastrar_livro(
            "1984", "George Orwell", 1949, "Ficção Científica"
        )
        self.livro3 = self.biblioteca.cadastrar_livro(
            "Dom Casmurro", "Machado de Assis", 1899, "Literatura Brasileira"
        )
        self.livro4 = self.biblioteca.cadastrar_livro(
            "Duna", "Frank Herbert", 1965, "Ficção Científica"
        )
    
    def test_cadastrar_livro(self):
      "Testa o cadastro de livros"
        print("\n🧪 Testando cadastro de livros...")
        
       
        self.assertEqual(self.livro1['titulo'], "O Senhor dos Anéis")
        self.assertEqual(self.livro1['autor'], "J.R.R. Tolkien")
        self.assertEqual(self.livro1['ano'], 1954)
        self.assertEqual(self.livro1['categoria'], "Fantasia")
        self.assertTrue(self.livro1['disponivel'])
        
        
        self.assertIsNotNone(self.livro1['id'])
        
        print("✅ Cadastro de livros funcionando corretamente")
    
    def test_buscar_livros_por_titulo(self):
        "Testa busca de livros por título"
        print("\n🧪 Testando busca por título...")
        
       
        livros = self.biblioteca.buscar_livros("titulo", "Senhor")
        self.assertEqual(len(livros), 1)
        self.assertEqual(livros[0]['titulo'], "O Senhor dos Anéis")
        
        
        livros = self.biblioteca.buscar_livros("titulo", "Harry Potter")
        self.assertEqual(len(livros), 0)
        
        print("✅ Busca por título funcionando corretamente")
    
    def test_buscar_livros_por_autor(self):
       "Testa busca de livros por autor"
        print("\n🧪 Testando busca por autor...")
        
    
        livros = self.biblioteca.buscar_livros("autor", "Tolkien")
        self.assertEqual(len(livros), 1)
        self.assertEqual(livros[0]['autor'], "J.R.R. Tolkien")
        
        print("✅ Busca por autor funcionando corretamente")
    
    def test_buscar_livros_por_categoria(self):
       "Testa busca de livros por categoria"
        print("\n🧪 Testando busca por categoria...")
        
        
        livros = self.biblioteca.buscar_livros("categoria", "Ficção Científica")
        self.assertEqual(len(livros), 2)  
        
        print("✅ Busca por categoria funcionando corretamente")
    
    def test_emprestar_livro(self):
      "Testa empréstimo de livros"
        print("\n🧪 Testando empréstimo de livros...")
        
        
        emprestimo = self.biblioteca.emprestar_livro(self.livro1['id'], "João Silva")
        
        self.assertEqual(emprestimo['livro_id'], self.livro1['id'])
        self.assertEqual(emprestimo['pessoa'], "João Silva")
        self.assertFalse(emprestimo['devolvido'])
        
        
        livro = next(l for l in self.biblioteca.livros if l['id'] == self.livro1['id'])
        self.assertFalse(livro['disponivel'])
        
       
        with self.assertRaises(ValueError):
            self.biblioteca.emprestar_livro(self.livro1['id'], "Maria Santos")
        
        print("✅ Empréstimo de livros funcionando corretamente")
    
    def test_devolver_livro(self):
      "Testa devolução de livros"
        print("\n🧪 Testando devolução de livros...")
        
      
        emprestimo = self.biblioteca.emprestar_livro(self.livro2['id'], "Ana Costa")
        
      
        devolucao = self.biblioteca.devolver_livro(emprestimo['id'])
        
        self.assertTrue(devolucao['devolvido'])
        self.assertIn('data_devolucao', devolucao)
        
        
        livro = next(l for l in self.biblioteca.livros if l['id'] == self.livro2['id'])
        self.assertTrue(livro['disponivel'])
        
      
        with self.assertRaises(ValueError):
            self.biblioteca.devolver_livro(emprestimo['id'])
        
        print("✅ Devolução de livros funcionando corretamente")
    
    def test_gerar_relatorio(self):
        "Testa geração de relatório"
        print("\n🧪 Testando geração de relatório...")
        
      
        self.biblioteca.emprestar_livro(self.livro1['id'], "Pedro Santos")
        
        relatorio = self.biblioteca.gerar_relatorio()
        
       
        self.assertIn('total_livros', relatorio)
        self.assertIn('livros_disponiveis', relatorio)
        self.assertIn('livros_emprestados', relatorio)
        self.assertIn('livros_por_categoria', relatorio)
        
        
        self.assertEqual(relatorio['total_livros'], 4)
        self.assertEqual(relatorio['livros_disponiveis'], 3)
        self.assertEqual(relatorio['livros_emprestados'], 1)
        
        print("✅ Geração de relatório funcionando corretamente")
    
    def test_funcao_lambda(self):
        "Testa uso de função lambda"
        print("\n🧪 Testando função lambda...")
        
       
        livros_ficcao = self.biblioteca.filtrar_livros_por_categoria("Ficção Científica")
        self.assertEqual(len(livros_ficcao), 2)
        
        
        for livro in livros_ficcao:
            self.assertEqual(livro['categoria'], "Ficção Científica")
        
        print("✅ Função lambda funcionando corretamente")
    
    def test_list_comprehension(self):
        "Testa uso de list comprehension"
        print("\n🧪 Testando list comprehension...")
        
     
        titulos = self.biblioteca.obter_titulos_livros(self.biblioteca.livros)
        
        self.assertEqual(len(titulos), 4)
        self.assertIn("O Senhor dos Anéis", titulos)
        self.assertIn("1984", titulos)
        self.assertIn("Dom Casmurro", titulos)
        self.assertIn("Duna", titulos)
        
        print("✅ List comprehension funcionando corretamente")
    
    def test_closure(self):
        "Testa uso de closure"
        print("\n🧪 Testando closure...")
        
        
        contador = self.biblioteca.criar_contador_emprestimos()
        
        
        self.assertEqual(contador(), 1)
        self.assertEqual(contador(), 2)
        self.assertEqual(contador(), 3)
        
     
        contador2 = self.biblioteca.criar_contador_emprestimos()
        self.assertEqual(contador2(), 1) 
        
        print("✅ Closure funcionando corretamente")
    
    def test_funcao_alta_ordem(self):
        "Testa uso de função de alta ordem"
        print("\n🧪 Testando função de alta ordem...")
        
      
        funcao_desconto = criar_funcao_desconto(0.1) 
        
        
        livros_com_preco = []
        for livro in self.biblioteca.livros[:2]:
            livro_com_preco = livro.copy()
            livro_com_preco['preco'] = 100.0
            livros_com_preco.append(livro_com_preco)
        
     
        livros_com_desconto = self.biblioteca.aplicar_desconto_livros(
            livros_com_preco, funcao_desconto
        )
        
        
        for livro in livros_com_desconto:
            self.assertEqual(livro['preco'], 90.0)  
        
        print("✅ Função de alta ordem funcionando corretamente")
    
    def test_processamento_funcional(self):
        "Testa processamento funcional"
        print("\n🧪 Testando processamento funcional...")
        
        
        filtro_ano = lambda livro: livro['ano'] > 1950
        
        
        transformacao = lambda livro: f"{livro['titulo']} ({livro['ano']})"
        
       
        resultado = processar_livros_funcional(
            self.biblioteca.livros, filtro_ano, transformacao
        )
        
        
        self.assertEqual(len(resultado), 2)  
        self.assertIn("Duna (1965)", resultado)
        self.assertIn("O Senhor dos Anéis (1954)", resultado)
        
        print("✅ Processamento funcional funcionando corretamente")
    
    def test_estatisticas_funcionais(self):
        "Testa cálculo de estatísticas "
        print("\n🧪 Testando estatísticas funcionais...")
        
        stats = calcular_estatisticas_livros(self.biblioteca.livros)
        
        
        self.assertIn('total', stats)
        self.assertIn('media_ano', stats)
        self.assertIn('categorias_unicas', stats)
        self.assertIn('ano_mais_antigo', stats)
        self.assertIn('ano_mais_recente', stats)
        
        # Verifica valores
        self.assertEqual(stats['total'], 4)
        self.assertEqual(stats['categorias_unicas'], 3)  
        self.assertEqual(stats['ano_mais_antigo'], 1899)  
        self.assertEqual(stats['ano_mais_recente'], 1965) 
        
        print("✅ Estatísticas funcionais funcionando corretamente")
    
    def test_casos_limite(self):
        "Testa casos limite e tratamento de erros"
        print("\n🧪 Testando casos limite...")
        
       
        with self.assertRaises(ValueError):
            self.biblioteca.emprestar_livro(999, "João")
        
        
        with self.assertRaises(ValueError):
            self.biblioteca.devolver_livro(999)
        
        
        livros = self.biblioteca.buscar_livros("titulo", "")
        self.assertEqual(len(livros), 4)  
        
        print("✅ Casos limite funcionando corretamente")


def executar_todos_os_testes():
    "Executa todos os testes e exibe resultados"
    print("="*60)
    print("    EXECUTANDO TESTES DO SISTEMA DE BIBLIOTECA")
    print("="*60)
    
   
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBiblioteca)
    
    
    runner = unittest.TextTestRunner(verbosity=0)
    resultado = runner.run(suite)
    
    
    print("\n" + "="*60)
    print("    RESUMO DOS TESTES")
    print("="*60)
    print(f"✅ Testes executados: {resultado.testsRun}")
    print(f"❌ Falhas: {len(resultado.failures)}")
    print(f"❌ Erros: {len(resultado.errors)}")
    
    if resultado.failures:
        print("\n🔍 FALHAS DETALHADAS:")
        for teste, traceback in resultado.failures:
            print(f"  - {teste}: {traceback}")
    
    if resultado.errors:
        print("\n🔍 ERROS DETALHADOS:")
        for teste, traceback in resultado.errors:
            print(f"  - {teste}: {traceback}")
    
    if resultado.wasSuccessful():
        print("\n🎉 TODOS OS TESTES PASSARAM COM SUCESSO!")
    else:
        print(f"\n⚠️  {len(resultado.failures + resultado.errors)} TESTE(S) FALHARAM")
    
    return resultado.wasSuccessful()


if __name__ == "__main__":
    executar_todos_os_testes()
