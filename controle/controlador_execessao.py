class Controlador_excessao:
    def handle_exception(self, exception):
        try:
            # Tratamento específico para diferentes tipos de exceções
            if isinstance(exception, ValueError):
                self.handle_value_error(exception)

            else:
                self.handle_generic_exception(exception)
        except Exception as e:
            self.handle_unexpected_exception(e)

    def handle_value_error(self, exception, mensagem):
        # Tratamento para exceções do tipo ValueError
        if isinstance(exception, ValueError):
            print(f"Erro: {exception}.\n {mensagem}")

    def handle_generic_exception(self, exception):
        print(f"Erro genérico: {exception}")

    def handle_unexpected_exception(self, exception):
        # Tratamento para exceções não previstas
        print(f"Erro inesperado: {exception}")
