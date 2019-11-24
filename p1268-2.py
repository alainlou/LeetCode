class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        answer = []
        for i in range(1, len(searchWord)+1):
            w = searchWord[:i]
            products = list(filter(lambda x: x.startswith(w), products))
            answer.append(products[:3])
        return answer