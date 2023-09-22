from board import printBoard


def isSecure(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == row - i:
            return False
    return True

def searchforwardcheckingCSP(n):
    board = [-1] * n
    domain = [[x for x in range(n)] for i in range(n)] 

    return forwardcheckingCSP(board, domain, n, 0)

def selectVariableMRV(domain):
    min_domain_size = float('inf')
    selected_variable = -1
    for i, d in enumerate(domain):
        if len(d) < min_domain_size and len(d) > 0:
            min_domain_size = len(d)
            selected_variable = i
    return selected_variable

def forwardcheckingCSP(board, domain, n, row, it=0):
    if row == n:
        return board, it

    selected_variable = selectVariableMRV(domain)

    if selected_variable == -1:
        return None, it 

    for col in domain[selected_variable]:
        if isSecure(board, selected_variable, col):
            board[selected_variable] = col
            saveDomain = [list(domain[i]) for i in range(n)]
            for i in range(row + 1, n):
                domain[i].remove(col)  

            result, it = forwardcheckingCSP(board, domain, n, row + 1, it + 1)
            if result is not None:
                return result, it

            for i in range(row + 1, n):
                domain[i] = list(saveDomain[i])
            board[selected_variable] = -1

    return None, it

