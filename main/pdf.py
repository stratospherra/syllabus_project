from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Выберите шрифт Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Переместиться вправо
        self.cell(100)
        # Заголовок
        self.cell(60, 10, 'Title', 1, 0, 'C')
        # Переход на новую строку
        self.ln(20)

    # Page footer
    def footer(self):
        # Позиционирование на 1.5 cm от нижнего края
        self.set_y(-15)
        # Выберите шрифт Arial italic 8
        self.set_font('Arial', 'I')
        # Номер страницы
        self.cell(0, 10, 'Page %s' % self.page_no(), 0, 0, 'C')

    # Chapter title
    def chapter_title(self, num, label):
        # Arial 12
        self.set_font('Arial', '', 12)
        # Background color
        self.set_fill_color(200, 220, 255)
        # Title
        self.cell(0, 6, 'Chapter %d : %s' % (num, label), 0, 1, 'L', 1)
        # Line break
        self.ln(4)

    # Chapter body
    def chapter_body(self, body):
        # Read text file
        # Times 12
        self.set_font('Times', '', 12)
        # Output justified text
        self.multi_cell(0, 5, body)
        # Line break
        self.ln()
        # Mention in italics
        self.set_font('', 'I')
        self.cell(0, 5, '(end of excerpt)')

    def print_chapter(self, num, title, body):
        self.add_page()
        self.chapter_title(num, title)
        self.chapter_body(body)

# Создание экземпляра класса PDF и определение формата страницы
pdf = PDF('P', 'mm', 'A4') # P - портретная ориентация, mm - миллиметры, A4 - формат страницы

# Добавление страницы
pdf.add_page()

# Установка шрифта
pdf.set_font("Arial", size = 15)

# Добавление изображения (логотипа). Укажите путь к файлу изображения.
pdf.image("logo.jpg", x = 18, y = 10, w = 60)

# Добавление текста
pdf.cell(200, 10, txt = "Welcome to Python", ln = True, align = 'C')

# Сохранение PDF
pdf.output("output.pdf")