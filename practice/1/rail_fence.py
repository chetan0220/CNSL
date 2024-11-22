def encrypt(plaintext, rails):
    result = ''
    matrix = [["" for _ in range(len(plaintext))] for _ in range(rails)]
    row = 0
    col = 0
    increment = 1
    for char in plaintext:
        if row + increment < 0 or row + increment >= len(matrix):
            increment = increment * -1

        matrix[row][col] = char
        row = row + increment
        col = col + 1
    
    for list in matrix:
        result += "".join(list)

    return result

def transpose(matrix):
    result = [["" for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[j][i] = matrix[i][j]
    
    return result

def decrypt(cipher, rails):
    result = ''
    matrix = [["" for _ in range(len(cipher))] for _ in range(rails)]
    index = 0
    increment = 1
    for selected_row in range(len(matrix)):
        row = 0
        for col in range(len(cipher)):
            if row + increment < 0 or row + increment >= len(matrix):
                increment = increment * -1
            
            if row == selected_row:
                matrix[row][col] = cipher[index]
                index += 1
            
            row = row + increment
    
    matrix = transpose(matrix)

    for list in matrix:
        result += "".join(list)
    
    return result
                              

def main():
    plaintext = "Hello World!"
    rails = 3
    encrypted = encrypt(plaintext, rails)
    print(encrypted)
    decrypted = decrypt(encrypted, rails)
    print(decrypted)


if __name__ == "__main__":
    main()