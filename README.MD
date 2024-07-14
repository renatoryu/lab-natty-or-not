# 📖 Gerador de Histórias Infantis 📝

## 📒 Descrição
O Gerador de Histórias Infantis utiliza a API do Google Generative AI para criar histórias personalizadas, com base no nome do personagem, tema e palavras-chave fornecidos pelo usuário.

## 🤖 Tecnologias Utilizadas
- **Google Generative AI**: Criação de conteúdo de alta qualidade.
- **FPDF**: Exportação das histórias geradas para arquivos PDF com formatação profissional.
- **Colorama**: Melhoria da experiência do usuário no terminal.

## 🧐 Processo de Criação
1. **Clone o Repositório**

   Para começar, clone o repositório para a sua máquina local:

   ```bash
   git clone https://github.com/renatoryu/lab-natty-or-not.git
   cd lab-natty-or-not
   ```

2. **Crie e Ative o Ambiente Virtual**

   Configure um ambiente virtual para gerenciar as dependências do projeto.

   **Windows:**

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   **macOS/Linux:**

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Instale as Dependências**

   Com o ambiente virtual ativado, instale as dependências necessárias:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure a Chave da API**

   Obtenha sua chave de API do Google Generative AI e substitua `sua_chave_api` no arquivo `main.py` pela sua chave de API.

5. **Execute o Script**

   Inicie o processo de geração de histórias executando o script principal:

   ```bash
   python main.py
   ```

6. **Siga as Instruções no Terminal**

   O script solicitará algumas informações para personalizar a história:
   - Insira o nome do personagem principal.
   - Insira o tema da história.
   - Insira palavras-chave relevantes para a história, separadas por vírgula.

## 🚀 Resultados
- **Histórias Personalizadas**: Cria histórias infantis únicas baseadas nas sugestões do usuário.
- **Exportação para PDF**: Gera arquivos PDF com formatação profissional das histórias criadas.
- **Visualização no Terminal**: Exibe a história gerada diretamente no terminal e salva como `historia_personalizada.pdf`.


---

Desenvolvido com ❤️ por **Renato Caetité Cruz**.

---

