# Basicamente vou desenvolver um aplicativo para auxiliar as pessoas a identificarem os sintomas de covid, caso estejam desinformadas
# por causa da paralização de divulgação de informações sobre a COVID-19 pós pandemia, funcionará para todos os grupos(Idade, Classe e Escolaridade)
# terá uma interface de facil entendimento e acesso, funcionara como um auto atendimento com perguntas de sim ou não e de acordo com as respostas os sintomas
# serão pesquisados na base de dados do programa e informará se o paciente está com sintomas ou não e a gravidez dos seus sintomas.
# No final irá mostrar o telefone de algum hospital proximo e a geolocalização do hospital mais proximo.

class BaseDeDados:
    def __init__(self):
        self.sintomas = {
            "febre": False,
            "tosse seca": False,
            "cansaço": False,
            "dor de garganta": False,
            "dificuldade respiratoria": False,
            "perda de paladar ou olfato": False,
            "dores e desconfortos": False,
            "calafrios": False,
        }
        self.diagnostico = None

    def perguntar(self, pergunta):
        resposta = input(pergunta + " (S ou N): ").strip().lower()
        return resposta == "s"

    def checar_sintomas(self):
        print("=========== Verificador de Sintomas da COVID-19 ===========")

        for sintoma in self.sintomas.keys():
            if self.perguntar(f"Você tem {sintoma}?"):
                self.sintomas[sintoma] = True

        # Avaliação dos sintomas
        num_sintomas = sum(self.sintomas.values())
        if num_sintomas >= 4:
            self.diagnostico = "Você apresenta sintomas de COVID-19. Recomenda-se procurar assistência médica."
        else:
            self.diagnostico = "Você provavelmente não apresenta sintomas de COVID-19, mas continue monitorando sua saúde."

        print(f"Diagnóstico: {self.diagnostico}")

    def encontrar_hospital(self):
        # Lógica para encontrar o hospital mais próximo
        print(">_Encontrando o hospital mais próximo...")

    def localizacao_hospital(self):
        # Obter a geolocalização do hospital
        print(">_Obtendo a localização do hospital mais próximo...")
        print("Aguarde um instante...")


if __name__ == "__main__":
    autoteste = BaseDeDados()
    autoteste.checar_sintomas()
    autoteste.encontrar_hospital()
    autoteste.localizacao_hospital()
