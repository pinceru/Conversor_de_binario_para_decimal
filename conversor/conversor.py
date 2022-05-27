class Conversor:
    def __init__(self, bin_number):
        self._bin_number = str(bin_number)
        self._figures_in_number = self._separate_numerals()

    def _separate_numerals(self):
        number_of_figures = len(self._bin_number)
        figures = []
        i = 0
        while i < number_of_figures:
            figures.append(int(self._bin_number[i:i+1]))
            i += 1
        return figures

    def _calculate_expoents(self):
        expoents = []
        length = len(self._figures_in_number)
        i = length
        while i >= length:
            for figure in self._figures_in_number:
                i -= 1
                expoents.append(int(figure * (2 ** i)))
        return expoents

    def calculate(self):
        numbers = self._calculate_expoents()
        dec_number = 0
        for number in numbers:
            dec_number = dec_number + number
        print('Esse número em decimal é: {}'.format(dec_number))

