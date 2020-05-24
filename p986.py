class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ans = []
        idx1, idx2 = 0, 0
        curr = [None, None]

        def get_overlap(interval1, interval2):
            if interval1[1] < interval2[0] or interval2[1] < interval1[0]:
                return
            return [max(interval1[0], interval2[0]), min(interval1[1], interval2[1])]

        while idx1 < len(A) and idx2 < len(B):
            if curr[0] is None:
                tmp = get_overlap(A[idx1], B[idx2])
                if tmp is not None:
                    curr = tmp
            else:
                tmp = get_overlap(A[idx1], B[idx2])
                if tmp is None:
                    ans.append(curr)
                    curr = [None, None]
                elif tmp[0] > curr[1]:
                    ans.append(curr)
                    curr = tmp
                else:
                    curr[1] = tmp[1]

            if A[idx1][1] < B[idx2][1] or idx2 == len(B) - 1:
                idx1 += 1
            else:
                idx2 += 1

        if curr[1] is not None:
            ans.append(curr)

        return ans
