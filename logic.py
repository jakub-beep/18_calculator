import math
import appearance

calculation = ""


def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    appearance.text_result.delete(1.0, 'end')
    appearance.text_result.insert(1.0, calculation)


def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        appearance.text_result.delete(1.0, 'end')
        appearance.text_result.insert(1.0, calculation)
    except:
        clear_field()
        appearance.text_result.insert(1.0, 'Error')


def clear_field():
    global calculation
    calculation = ''
    appearance.text_result.delete(1.0, 'end')


def sin():
    global calculation
    calculation = str(round(math.sin(math.radians(int(calculation))), 4))
    appearance.text_result.delete(1.0, 'end')
    appearance.text_result.insert(1.0, calculation)

def cos():
    global calculation
    calculation = str(round(math.cos(math.radians(int(calculation))), 4))
    appearance.text_result.delete(1.0, 'end')
    appearance.text_result.insert(1.0, calculation)

def tan():
    global calculation
    calculation = str(round(math.tan(math.radians(int(calculation))), 4))
    appearance.text_result.delete(1.0, 'end')
    appearance.text_result.insert(1.0, calculation)

def ctg():
    global calculation
    calculation = str(round(int(math.tan(math.radians(int(calculation)))) ^ (-1), 4))
    appearance.text_result.delete(1.0, 'end')
    appearance.text_result.insert(1.0, calculation)

def ln():
    global calculation
    calculation = str(round(math.log((int(calculation))), 4))
    appearance.text_result.delete(1.0, 'end')
    appearance.text_result.insert(1.0, calculation)






