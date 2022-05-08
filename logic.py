import math
import tkinter as tk
import charts


class Calculation:

    def __init__(self, text_result):
        self.calculation = ''
        self.text_result = text_result

    def add_to_calculation(self, symbol):
        # method responsible for inserting numbers, calculations to textfield, after adding it resets calculation to ""
        self.calculation += symbol
        self.text_result.delete(1.0, 'end')
        self.text_result.insert(1.0, self.calculation)

    def evaluate_calculation(self):
        # method responsible for changing string in textfield to calculations
        try:
            self.calculation = str(eval(self.calculation))
            text_result.delete(1.0, 'end')
            text_result.insert(1.0, self.calculation)
        except:
            self.clear_field()
            text_result.insert(1.0, 'Error')

    def clear_field(self):
        self.calculation = ''
        text_result.delete(1.0, 'end')

    def estimate_function(self, math_function):
        # method responsible for implementing specific functions
        self.calculation = str(math_function(self.calculation))
        # float czy działa dla wszystkich
        text_result.delete(1.0, 'end')
        text_result.insert(1.0, self.calculation)


calc_sin = lambda formula: round(math.sin(math.radians(int(formula))), 4)
calc_cos = lambda formula: round(math.cos(math.radians(int(formula))), 4)
calc_tan = lambda formula: round(math.tan(math.radians(int(formula))), 4)
calc_ctg = lambda formula: round(int(math.tan(math.radians(int(formula)))) ^ (-1), 4)
calc_ln = lambda formula: round(math.log((int(formula + '0'))), 4)
calc_fac = lambda formula: math.factorial(int(formula))
calc_pow_2 = lambda formula: math.pow(float(formula), 2)
calc_pow_3 = lambda formula: math.pow(float(formula), 3)
calc_approx = lambda formula: math.ceil(float(formula))

if __name__ == "__main__":

    # appearance definition
    root = tk.Tk()
    root.geometry('400x450')
    root.resizable(False, False)
    root.configure(bg='black')
    text_result = tk.Text(root, height=3, width=22, font=('Arial', 24))
    text_result.grid(columnspan=5)

    calc = Calculation(text_result)

    # button definitions
    buttons = []
    btn_stan = [8, ('Arial', 14)]


    def my_button(text, command, bg='red'):
        return tk.Button(root, text=text, command=command, width=btn_stan[0], font=btn_stan[1], bg=bg)


    # command=lambda arg=i this lets us remember the value from the proper loop step, without it after pressing any button
    # lambda takes for i value from the last loop step
    # adding zero outside of the loop
    for i in list(range(1, 10)) + [0]:
        buttons.append(my_button(text=str(i), command=lambda arg=i: calc.add_to_calculation(str(arg))))

    buttons.extend([my_button('(', command=lambda: calc.add_to_calculation('(')),
                    my_button(')', command=lambda: calc.add_to_calculation(')')),
                    my_button('+', command=lambda: calc.add_to_calculation('+')),
                    my_button('-', command=lambda: calc.add_to_calculation('-')),
                    my_button('*', command=lambda: calc.add_to_calculation('*')),
                    my_button('/', command=lambda: calc.add_to_calculation('/')),
                    my_button('sin()', command=lambda: calc.estimate_function(calc_sin)),
                    my_button('cos()', command=lambda: calc.estimate_function(calc_cos)),
                    my_button('tan()', command=lambda: calc.estimate_function(calc_tan)),
                    my_button('ctg()', command=lambda: calc.estimate_function(calc_cot)),
                    my_button('ln()', command=lambda: calc.estimate_function(calc_ln)),
                    my_button('fact!', command=lambda: calc.estimate_function(calc_fac)),
                    my_button('^2', command=lambda: calc.estimate_function(calc_pow_2)),
                    my_button('^3', command=lambda: calc.estimate_function(calc_pow_3)),
                    my_button('draw_sin', command=charts.sin.draw_trig),
                    my_button('draw_cos', command=charts.cos.draw_trig),
                    my_button('draw_tan', command=charts.tan.draw_trig),
                    my_button('draw_ln', command=charts.ln.draw_ln),
                    my_button('=', command=calc.evaluate_calculation, bg='blue'),
                    my_button('C', command=calc.clear_field),
                    my_button('.', command=lambda: calc.add_to_calculation('.')),
                    my_button('∼', command=lambda: calc.estimate_function(calc_approx))
                    ])

    first_row = 2
    first_column = 1
    columns = 4
    for number, button in enumerate(buttons):
        button.grid(row=first_row + number // columns, column=first_column + number % columns)
    root.mainloop()
else:
    pass
