def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        ret = []
        while matrix:
            ret+=(matrix.pop(0)) # take the first going to the right.
            if matrix and matrix[0]:
                for row in matrix:
                    ret.append(row.pop())
            if matrix: # reversed
                ret+=(matrix.pop()[::-1])
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ret.append(row.pop(0))
        return ret
