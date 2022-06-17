import os

class CadastroVoo:
    def __init__(self, voo_number, origem, destino, quantidade_assentos, valor_assento):
        self.voo_number = voo_number
        self.origem = origem
        self.destino = destino
        self.quantidade_assentos = quantidade_assentos
        self.reservas = 0
        self.valorReservas = []
        self.valor_assento = valor_assento

    def cadastrarVoo(self):
        self.voo_number = input("Digite o número do voo: ")
        self.origem = input("Digite a origem: ")
        self.destino = input("Digite o destino: ")
        self.quantidade_assentos = int(input("Digite a quantidade de assentos: "))
        self.valor_assento = float(input("Digite o valor do assento: "))

    def mostrarVoo(self):
        return f"Voo: {self.voo_number} - Origem: {self.origem} - Destino: {self.destino} - Quantidade de assentos disponíveis: {self.quantidade_assentos - self.reservas} - Valor do assento: {self.valor_assento}"

    def reservarAssento(self):
        self.reservas += 1
        self.valorReservas.append(self.valorReserva())
        return f"Voo: {self.voo_number} - Origem: {self.origem} - Destino: {self.destino} - Quantidade de assentos disponíveis: {self.quantidade_assentos - self.reservas} - Valor do assento: {self.valor_assento}"

    def quantidadeReservas(self):
        return self.reservas

    def quantidadeAssentosDisponiveis(self):
        return self.quantidade_assentos - self.reservas

    def valorReserva(self):
        return self.valor_assento - self.descontoReserva()

    def descontoReserva(self):
        if self.reservas < 10:
            return self.valor_assento * 0.25
        elif self.reservas < 15:
            return self.valor_assento * 0.15
        elif self.reservas < 20:
            return self.valor_assento * 0.05
        else:
            return 0

    def valorTotal(self):
        return sum(self.valorReservas)

    def descontosDados(self):
        reservas_efetuadas = self.quantidadeReservas()

        if reservas_efetuadas <= 10:
            print(f"{reservas_efetuadas} receberam o desconto de 25%")

        if reservas_efetuadas > 10 and reservas_efetuadas <= 15:
            print(f"{reservas_efetuadas - 10} receberam o desconto de 15%")

        if reservas_efetuadas > 15 and reservas_efetuadas <= 20:
            print(f"{reservas_efetuadas - 15} receberam o desconto de 5%")

        if reservas_efetuadas > 20:
            print(f"{reservas_efetuadas - 20} não receberam desconto")


print("-" * 15 + "Controle de voo e assentos" + "-" * 15)

while True:

    opcao = int(
        input(
            """Controle de Reservas de assentos
    [1] Cadastrar voo
    [2] Reservar assento
    [3] Mostrar voo
    [4] Quantidade de reservas
    [5] Quantidade de assentos disponíveis
    [6] Valor da reserva
    [7] Valor total voo
    [8] Descontos dados
    [9] Sair do programa
    
    """
        )
    )

    os.system("cls")
    if opcao in range(1, 9):

        if opcao == 1:
            voo = CadastroVoo(0, "", "", 0, 0)
            voo.cadastrarVoo()
            print(voo.mostrarVoo())
        elif opcao == 2:
            if voo.quantidadeAssentosDisponiveis() > 0:

                confirma = input(
                    f"O valor para reserva é de {voo.valorReserva()}. Deseja confirmar a reserva do assento? (S/N) "
                )
                if confirma == "s" or confirma == "S":
                    voo.reservarAssento()
                    print("Assento reservado com sucesso!")
                    print(voo.mostrarVoo())
                else:
                    continue
            else:
                print("Não há assentos disponíveis")
        elif opcao == 3:
            print(voo.mostrarVoo())
        elif opcao == 4:
            print(f"Quantidade de reservas: {voo.quantidadeReservas()}")
        elif opcao == 5:
            print(
                f"Quantidade de assentos disponíveis: {voo.quantidadeAssentosDisponiveis()}"
            )
        elif opcao == 6:
            print(f"Valor da reserva: {voo.valorReserva()}")
        elif opcao == 7:
            print(f"Valor total: {voo.valorTotal()}")
        elif opcao == 8:
            print(f"Descontos dados: {voo.descontosDados()}")
        elif opcao == 9:
            break