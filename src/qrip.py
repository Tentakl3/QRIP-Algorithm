import pandas as pd
class Qrip:
    """This class apply the qrip algorith to find the language accepted by a dfa"""
    def __init__(self, matrix, matrix_values) -> None:
        self.qrip = ""
        self.nodes = list(matrix.keys())
        self.matrix = matrix
        self.matrix_values = matrix_values

    def preprocesing(self):
        """Class for preprocesing matrixes to dataframe"""
        self.matrix = pd.DataFrame.from_dict(self.matrix)
        self.matrix.index = self.nodes

        self.matrix_values = pd.DataFrame.from_dict(self.matrix_values)
        self.matrix_values.index = self.nodes
    
if __name__ == "__main__":
    nodes = ["q0", "q1", "q2", "q3"]
    matrix = {"q0": [0, 1, 0, 1], "q1": [1, 0, 1, 0], "q2": [0, 1, 0, 1], "q3": [1, 0, 1, 0]}
    matrix_values ={"q0": ["", "x", "", "x"], "q1": ["x", "", "y", ""], "q2": ["", "y", "", "x"], "q3": ["y", "", "x", ""]}
    qrip = Qrip(matrix, matrix_values)