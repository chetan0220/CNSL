# Implement Rail fence encryption algo
	
def encrypt(plaintext, rails):
    result = ""
    matrix = [["" for _ in range(0, len(plaintext))] for _ in range(0, rails)]
    increment = 1
    row = 0
    col = 0

    for char in plaintext:
        if row + increment < 0 or row + increment >= len(matrix):
            increment = increment * -1
        matrix[row][col] = char
        row = row + increment
        col = col + 1
    
    for list in matrix:
        result = result + "".join(list)
    
    return result

def transpose(matrix):
    result = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[j][i] = matrix[i][j]
    
    return result

def decrypt(cipher, rails):
    result = ""
    matrix = [["" for _ in range(0, len(cipher))] for _ in range(0, rails)]
    increment = 1
    index = 0

    for selectedRow in range(len(matrix)):
        row = 0
        for col in range(len(matrix[row])):
            if row + increment < 0 or row + increment >= len(matrix):
                increment = increment * -1
            if row == selectedRow:
                matrix[row][col] = cipher[index]
                index += 1
            row += increment

    matrix = transpose(matrix)
    for list in matrix:
        result += "".join(list)
    
    return result


def main():
    plaintext = "Hello World!"
    rails = 3
    encrypted_txt = encrypt(plaintext, rails)
    print(encrypted_txt)

    decrypted_txt = decrypt(encrypted_txt, rails)
    print(decrypted_txt)

if __name__ == "__main__":
    main()