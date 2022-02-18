import math
import tkinter as tk
import charts


class Calculation:
    calculation = ""

    def __init__(self, name):
        self.name = name

    def add_to_calculation(self, symbol):
        # method responsible for inserting numbers, calculations to textfield, after adding it resets calculation to ""
        print(symbol)
        Calculation.calculation += str(symbol)
        text_result.delete(1.0, 'end')
        text_result.insert(1.0, Calculation.calculation)

    def evaluate_calculation(self):
        # method responsible for changing string in textfield to calculations
        try:
            Calculation.calculation = str(eval(Calculation.calculation))
            text_result.delete(1.0, 'end')
            text_result.insert(1.0, Calculation.calculation)
        except:
            Calculation.clear_field(self)
            text_result.insert(1.0, 'Error')

    def clear_field(self):
        Calculation.calculation = ''
        text_result.delete(1.0, 'end')

    def function(self):
        # method responsible for implementing specific functions
        if self.name == 'sin':
            Calculation.calculation = str(round(math.sin(math.radians(int(Calculation.calculation))), 4))
        elif self.name == 'cos':
            Calculation.calculation = str(round(math.cos(math.radians(int(Calculation.calculation))), 4))
        elif self.name == 'tan':
            Calculation.calculation = str(round(math.tan(math.radians(int(Calculation.calculation))), 4))
        elif self.name == 'cot':
            Calculation.calculation = str(round(int(math.tan(math.radians(int(Calculation.calculation)))) ^ (-1), 4))
        elif self.name == 'ln':
            Calculation.calculation = str(round(math.log((int(Calculation.calculation + '0'))), 4))
        elif self.name == 'fac':
            Calculation.calculation = str(math.factorial(int(Calculation.calculation)))
        elif self.name == 'pow_2':
            Calculation.calculation = str(math.pow(float(Calculation.calculation), 2))
        elif self.name == 'pow_3':
            Calculation.calculation = str(math.pow(float(Calculation.calculation), 3))
        elif self.name == 'approximate':
            Calculation.calculation = str(round(float(Calculation.calculation), 1))
        text_result.delete(1.0, 'end')
        text_result.insert(1.0, Calculation.calculation)

calc = Calculation(None)
calc_sin = Calculation('sin')
calc_cos = Calculation('cos')
calc_tan = Calculation('tan')
calc_ctg = Calculation('cot')
calc_ln = Calculation('ln')
calc_fac = Calculation('fac')
calc_pow_2 = Calculation('pow_2')
calc_pow_3 = Calculation('pow_3')
calc_approx = Calculation('approximate')

# appearance definition
root = tk.Tk()
root.geometry('400x450')
root.resizable(False, False)
root.configure(bg='black')
text_result = tk.Text(root, height=3, width=22, font=('Arial', 24))
text_result.grid(columnspan=5)

# button definitions
buttons = []
btn_stan = [8, ('Arial', 14)]


def my_button(text, command, bg='red'):
    return tk.Button(root, text=text, command=command, width=btn_stan[0], font=btn_stan[1], bg=bg)

# command=lambda arg=i this lets us remember the value from the proper loop step, without it after pressing any button
# lambda takes for i value from the last loop step
for i in list(range(1, 10)) + [0]:
    buttons.append(my_button(text=str(i), command=lambda arg=i: calc.add_to_calculation(arg)))

buttons.extend([my_button(text='(', command=lambda: calc.add_to_calculation('(')),
                my_button(')', command=lambda: calc.add_to_calculation(')')),
                my_button('+', command=lambda: calc.add_to_calculation('+')),
                my_button('-', command=lambda: calc.add_to_calculation('-')),
                my_button('*', command=lambda: calc.add_to_calculation('*')),
                my_button('/', command=lambda: calc.add_to_calculation('/')),
                my_button('sin()', command=calc_sin.function),
                my_button('cos()', command=calc_cos.function),
                my_button('tan()', command=calc_tan.function),
                my_button('ctg()', command=calc_ctg.function),
                my_button('ln()', command=calc_ln),
                my_button('fact!', command=calc_fac),
                my_button('^2', command=calc_pow_2),
                my_button('^3', command=calc_pow_3),
                my_button('draw_sin', command=charts.sin.draw_trig),
                my_button('draw_cos', command=charts.cos.draw_trig),
                my_button('draw_tan', command=charts.tan.draw_trig),
                my_button('draw_ln', command=charts.ln.draw_trig),
                my_button('=', command=calc.evaluate_calculation, bg='blue'),
                my_button('C', command=calc_pow_2.clear_field),
                my_button('.', command=lambda: calc.add_to_calculation('.')),
                my_button('∼', command=calc_approx.function)
                ])

first_row = 2
first_column = 1
columns = 4
for number, button in enumerate(buttons):
    button.grid(row=first_row + number // columns, column=first_column + number % columns)
root.mainloop()
