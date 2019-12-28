from ast import literal_eval

def day25(inps):
    words = inps.strip().split()
    row,col = (int(words[k][:-1]) for k in (-3,-1))
    code = 20151125
    a = 252533
    m = 33554393
    for _ in range(get_ind(row, col)-1):
        code = (a * code) % m
    return code

def get_ind(row,col):
    # get linear index of (row,col) code, 1-based indexing

    # row 1 goes 1 -> +2 -> +3 -> +4 -> ... -> +col
    # so row 1 in column col is 1+2+3+4+...+col == (1+col)/2*col == n0

    # and in column col the numbers go down as n0 -> +col -> +col+1 -> +col+2 -> ... -> +col+row-2 (row-1 additions to n0)
    # so row row in column col is n0 + (row-1)*col + 1+2+3+...+(row-2) == n0 + (row-1)*col + (row-1)*(row-2)/2  (last term is 0 if row==1 or row==2) == col*(col+1)/2 + (row-2)*(row-1)/2 + (row-1)*col
    return (col*(col+1))//2 + ((row-2)*(row-1))//2 + (row-1)*col

if __name__ == "__main__":
    inps = open('day25.inp').read()
    print(day25(inps))
