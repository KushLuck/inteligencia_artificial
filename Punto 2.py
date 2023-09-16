import matplotlib.pyplot as plt
import pandas as pd

class DataAnalyzer:
    def __init__(self, file_path):
        self.dataframe = pd.read_csv(file_path)

    def calculate_basic_stats(self):
        return self.dataframe.describe()

    def get_variable_names(self):
        return list(self.dataframe.columns)

    def analyze_variable(self, variable):
        if variable in self.dataframe.columns:
            variable_data = self.dataframe[variable]
            mean = variable_data.mean()
            median = variable_data.median()
            std = variable_data.std()
            q25 = variable_data.quantile(0.25)
            q50 = median
            q75 = variable_data.quantile(0.75)

            plt.hist(variable_data, bins='auto', alpha=0.7, color='b', edgecolor='black')
            plt.title(f'Histograma de {variable}')
            plt.xlabel(variable)
            plt.ylabel('Frecuencia')
            plt.show()

            return {
                'Media': mean,
                'Mediana': median,
                'Desviación Estándar': std,
                'Percentil 25 (q25)': q25,
                'Percentil 50 (q50)': q50,
                'Percentil 75 (q75)': q75
            }
        else:
            return f'La variable {variable} no existe en el conjunto de datos.'

if __name__ == "__main__":
    data_analyzer = DataAnalyzer("iris.csv")

    basic_stats = data_analyzer.calculate_basic_stats()
    print("Estadísticas Descriptivas Básicas:")
    print(basic_stats)

    variable_names = data_analyzer.get_variable_names()
    print("Nombres de las Variables Disponibles:")
    print(variable_names)

    variable_name_to_analyze = "sepal.length"
    variable_stats = data_analyzer.analyze_variable(variable_name_to_analyze)
    print(f"Análisis de la Variable '{variable_name_to_analyze}':")
    print(variable_stats)