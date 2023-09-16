import pandas as pd

class Evens(object):
    def __init__(self, file_path):
        self.dataframe = pd.read_csv(file_path)
        self.index = 0
        self.max_batches = len(self.dataframe) // 2 

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.dataframe) or self.index // 2 >= self.max_batches:
            raise StopIteration("error")
        else:
            data = self.dataframe.iloc[self.index:self.index+2]
            self.index += 2
            return data

    def select_starting_position(self, position):
        self.index = position+1

if __name__ == "__main__":
    iris_iterator = Evens("iris.csv")

    iris_iterator.select_starting_position(139)

    try:
        data1 = next(iris_iterator)
        print(data1)
        
    except StopIteration:
        print("error")
