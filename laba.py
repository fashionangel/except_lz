import pandas as pd

class Cash:
    def __init__(self, file_path):
        self.df = file_path

    def process(self):
        ex_columns = ['Участники гражданского оборота', 'Тип операции', 'Сумма операции', 'Вид расчета', 'Место оплаты', 'Терминал оплаты', 'Дата оплаты', 'Время оплаты', 'Результат операции', 'Cash-back', 'Сумма cash-back']
        ex_data = {'Участники гражданского оборота': 'object', 'Тип операции':'object', 'Сумма операции' : 'float64', 'Вид расчета' : 'object', 'Место оплаты' : 'object', 'Терминал оплаты' : 'object', 'Дата оплаты': 'object', 'Время оплаты': 'object', 'Результат операции':'object', 'Cash-back': 'object', 'Сумма cash-back': 'float64'} 
        
        try:
            self.dF = pd.read_csv(self.df)

            actual_col = list(self.dF.columns)
            if actual_col != ex_columns:
                raise KeyError(f'-Названия столбцов не совпадают. \n f"Ожидаемые: {ex_columns}/n Фактические: {actual_col}\n')
                
            for i, j in ex_data.items():
                if i not in self.dF.columns:
                    raise TypeError(f"Отсутствует обязательный столбец: '{i}'\n")
                else:
                    actual_type = str(self.dF[i].dtype)
                    if actual_type != j:
                        raise TypeError(f"В столбце: '{i}' тип данных не соответствует оиждаемому\n" f"Ожидается: {j}, Фактически: {actual_type}\n")
        
        except FileNotFoundError as e:
            print(f'Возникла ошибка следующего типа: {e}')
        except ValueError as e:
            print(f'Возникла ошибка: {e}(Ваш датафрейм пуст)')        
        except TypeError as e:
            print(f"Возникла ошибка: {e} ")
        except KeyError as e:
            print(f"Возникла ошибка структуры данных:\n{e}")
        else:
            print(f'Чтение завершено успешно')
        


x = Cash('var4.csv')
x.process()