import google.generativeai as genai
from fpdf import FPDF
from colorama import init, Fore, Style

# Inicializar o colorama
init(autoreset=True)

# Configure sua chave da API Google AI
api_key = ""
genai.configure(api_key=api_key)

generation_config = {
    "candidate_count": 1,
    "temperature": 0.8,
}

safety_settings = {
    "HARASSMENT": "BLOCK_NONE",
    "HATE": "BLOCK_NONE",
    "SEXUAL": "BLOCK_NONE",
    "DANGEROUS": "BLOCK_NONE",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest",
    generation_config=generation_config,
    safety_settings=safety_settings,
)


class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.set_text_color(0, 102, 204)  # Azul
        self.cell(0, 10, "História Infantil", 0, 1, "C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.set_text_color(128, 128, 128)  # Cinza
        self.cell(0, 10, f"Página {self.page_no()}", 0, 0, "C")

    def chapter_title(self, title):
        self.set_font("Arial", "B", 14)
        self.set_text_color(255, 0, 0)  # Vermelho
        self.cell(0, 10, title, 0, 1, "L")
        self.ln(10)

    def chapter_body(self, body):
        self.set_font("Times", "", 12)
        self.set_text_color(0, 0, 0)  # Preto
        self.multi_cell(0, 10, body)
        self.ln()

    def add_chapter(self, title, body):
        self.add_page()
        self.chapter_title(title)
        self.chapter_body(body)


def generate_story(principal_character_name, theme, keywords):
    prompt = f"Crie uma história infantil com o personagem {principal_character_name}, tema {theme} e incluindo as seguintes palavras-chave: {', '.join(keywords)}."

    response = model.generate_content(prompt)

    if response and response.text.strip():
        story = response.text.strip()
        return story
    else:
        raise ValueError("Não foi possível gerar uma história com os dados fornecidos.")


if __name__ == "__main__":
    print(Fore.CYAN + Style.BRIGHT + "📖 Gerador de Histórias Infantis 📝\n")
    print(
        Fore.GREEN
        + "👋 Bem-vindo ao gerador de histórias infantis! Insira o nome do personagem, o tema e palavras-chave para começar.\n"
    )

    principal_character_name = input(Fore.YELLOW + "🧙 Nome do Personagem: ")
    theme = input(Fore.YELLOW + "📜 Tema: ")
    keywords = input(Fore.YELLOW + "🔑 Palavras-chave (separadas por vírgula): ").split(
        ","
    )

    try:
        story = generate_story(principal_character_name, theme, keywords)
        print(Fore.CYAN + "\nHistória Gerada: \n")
        print(Fore.WHITE + "------------------------------")
        print(Fore.MAGENTA + story)
        print(Fore.WHITE + "------------------------------")

        pdf = PDF()
        pdf.add_chapter(f"Uma aventura com {principal_character_name}", story)
        pdf.output("historia_personalizada.pdf")
        print(Fore.GREEN + "\nE-book gerado: historia_personalizada.pdf")
    except Exception as e:
        print(Fore.RED + f"Erro ao gerar a história: {e}")
