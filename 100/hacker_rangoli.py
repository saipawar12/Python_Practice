def print_rangoli(size):
    lines = []

    for i in range(size):
        # Generate characters from 'a' + size - 1 down to 'a' + i
        left = [chr(ord('a') + j) for j in range(size - 1, i, -1)]
        right = [chr(ord('a') + j) for j in range(i, size)]
        row = '-'.join(left + right)
        lines.append(row.center(4 * size - 3, '-'))

    for line in lines[::-1] + lines[1:]:
        print(line)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)