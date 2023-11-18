import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QColorDialog, QFontDialog, QInputDialog, QWidget

class TextEditorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Crear el widget principal y el layout vertical
        central_widget = QWidget(self)
        layout = QVBoxLayout()

        # Crear el área de texto
        self.text_edit = QTextEdit(self)
        layout.addWidget(self.text_edit)

        # Crear botones para cambiar fuente, tamaño y color
        font_button = QPushButton('Cambiar Fuente', self)
        font_button.clicked.connect(self.show_font_dialog)

        size_button = QPushButton('Cambiar Tamaño', self)
        size_button.clicked.connect(self.show_size_dialog)

        color_button = QPushButton('Cambiar Color', self)
        color_button.clicked.connect(self.show_color_dialog)

        # Agregar botones al layout
        layout.addWidget(font_button)
        layout.addWidget(size_button)
        layout.addWidget(color_button)

        # Aplicar el layout al widget principal
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Configuración de la ventana principal
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Editor de Texto PySide')

    def show_font_dialog(self):
        # Obtener la fuente actual del área de texto
        current_font = self.text_edit.currentFont()

        # Crear un diálogo de selección de fuente
        font_dialog = QFontDialog(current_font, self)
        font_dialog.setWindowTitle('Seleccionar Fuente')

        # Si el usuario hace clic en "Aceptar", establecer la fuente seleccionada en el área de texto
        if font_dialog.exec() == QFontDialog.Accepted:
            selected_font = font_dialog.selectedFont()
            self.text_edit.setFont(selected_font)

    def show_size_dialog(self):
        # Solicitar al usuario que ingrese el tamaño de la fuente
        size, ok = QInputDialog.getInt(self, 'Seleccionar Tamaño', 'Ingrese el tamaño de la fuente:')
        if ok:
            # Obtener la fuente actual del área de texto
            font = self.text_edit.currentFont()

            # Establecer el tamaño de la fuente y aplicar al área de texto
            font.setPointSize(size)
            self.text_edit.setCurrentFont(font)

    def show_color_dialog(self):
        # Obtener el color actual del texto en el área de texto
        color = QColorDialog.getColor(self.text_edit.textColor(), self, 'Seleccionar Color')

        # Si el color seleccionado es válido, establecerlo en el texto del área
        if color.isValid():
            self.text_edit.setTextColor(color)

if __name__ == '__main__':
    # Iniciar la aplicación
    app = QApplication(sys.argv)
    editor = TextEditorApp()
    editor.show()
    sys.exit(app.exec())
