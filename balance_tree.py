# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        """Retorna uma BST balanceada com os mesmos valores dos nós."""

        # Etapa 1: Atravessa em ordem para obter valores ordenados
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)

        # Lista com os valores em ordem crescente
        sorted_vals = inorder(root)

        # Etapa 2: construir uma BST balanceada a partir da lista ordenada
        def build_balanced(nums):
            if not nums:
                return None
            mid = len(nums) // 2  # escolhe o valor do meio como raiz
            node = TreeNode(nums[mid])
            # Constrói recursivamente subárvores esquerda e direita
            node.left = build_balanced(nums[:mid])
            node.right = build_balanced(nums[mid + 1:])
            return node

        return build_balanced(sorted_vals)
