class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in board:
            rows={}
            for j in i:
                if j==".":
                    continue
                if j in rows:
                    rows[j]+=1
                else:
                    rows[j]=1
            for i in rows:
                if rows[i]>1:
                    return False 
        for j in range(9):
            cols={}
            for i in range(9):
                x=board[i][j]
                if x==".":
                    continue
                if x in cols:
                    cols[x]+=1
                else:
                    cols[x]=1
            for i in cols:
                if cols[i]>1:
                    return False
        row=8
        while row>=0:
            col=8
            while col>=0:
                boxes={}
                for r in range(row,row-3,-1):
                    for c in range (col,col-3,-1):
                        x=board[r][c]
                        if x==".":
                            continue
                        if x in boxes:
                            boxes[x]+=1
                        else:
                            boxes[x]=1
                for i in boxes:
                    if boxes[i]>1:
                        return False
                col-=3
            row-=3
        return True