pointer = 0
cell = []
code=""

def main():
    """Main function"""
    global code, cell, pointer
    code = input("Enter the code: ")
    print("\n\n")
    if code != "":
        for i in range(len(code)):
            interpreter(code[i] ,i)
    print("\n\n")


def interpreter(znak, i):
    """Brainfuck interpreter
        > increment the data pointer (to point to the next cell to the right).
        < decrement the data pointer (to point to the next cell to the left).
        + increment (increase by one) the byte at the data pointer.
        - decrement (decrease by one) the byte at the data pointer.
        . output the byte at the data pointer.
        , accept one byte of input, storing its value in the byte at the data pointer.
        [ if the byte at the data pointer is zero, then instead of moving the instruction pointer forward to the next command, jump it forward to the command after the matching ]
        ] if the byte at the data pointer is nonzero, then instead of moving the instruction pointer forward to the next command, jump it back to the command after the matching [."""
    global code, cell, pointer
    match znak:
        case ">":
            pointer += 1
        case "<":
            pointer -= 1
            if pointer<0:
                pointer = 0
        case "+":
            try:
                cell[pointer] += 1
            except:
                cell.append(0)
                cell[pointer] += 1
        case "-":
            try:
                cell[pointer] -= 1
            except:
                cell.append(0)
                cell[pointer] -= 1
        case ".":
            if cell[pointer]==10 or cell[pointer]==13:
                print("\n")
            else:
                print(chr(cell[pointer]), end="")
        case ",":
            cell[pointer] = ord(input("Enter a character: "))
        case "[":
            loop_begin = i
            loop_end = code.find("]", i)
            if cell[pointer] != 0:
                loop_end = code.find("]", i)
                for a in range(0,cell[pointer]-1):
                    for j in range(1,loop_end-loop_begin):
                        interpreter(code[loop_begin + j], loop_begin + j)

if __name__ == '__main__':
    main()
