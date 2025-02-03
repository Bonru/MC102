def print_paths(matrix, row, col, path):
    if not (0 <= row < len(matrix)) or not (0 <= col < len(matrix[0])):
        return

    path += matrix[row][col]

    if row == len(matrix) - 1 and col == len(matrix[0]) - 1:
        print("Caminho encontrado:", path)
        return

    print_paths(matrix, row + 1, col, path)
    print_paths(matrix, row, col + 1, path)

# Exemplo de uso
if __name__ == "__main__":
    mapa = [
        ['.', '.', '.', '.'],
        ['.', '*', '*', '.'],
        ['.', '.', '*', '.'],
        ['.', '.', '.', '=']
    ]

    print("Possíveis caminhos:")
    print_paths(mapa, 0, 0, "")