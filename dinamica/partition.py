# É verdadeiro se existir uma sublista da lista `nums[0…n]` com o total dado
def subsetSum(nums, n, total):
 
    # true se a soma se tornar 0 (subconjunto encontrado)
    if total == 0:
        return True
 
    # Caso base: nenhum item restante ou a soma se torna negativa
    if n < 0 or total < 0:
        return False
 
    # Caso 1. Inclua o item atual `nums[n]` no subconjunto e se repita
    # para itens restantes `n-1` com a soma restante `total-nums[n]`
    include = subsetSum(nums, n - 1, total - nums[n])
 
    # true se obtivermos subconjunto incluindo o item atual
    if include:
        return True
 
    # Caso 2. Exclua o item atual `nums[n]` do subconjunto e repita para
    # itens restantes `n-1`
    exclude = subsetSum(nums, n - 1, total)
 
    # true se obtivermos subconjunto excluindo o item atual
    return exclude
 
 
# É verdadeiro se a lista fornecida `nums[0…n-1]` puder ser dividida em duas
# Sublistas # com soma igual
def partition(nums):
 
    total = sum(nums)
 
    # true se a soma for par e a lista puder ser dividida em
    # duas sublistas com soma igual
    return (total & 1) == 0 and subsetSum(nums, len(nums) - 1, total/2)
 
 
if __name__ == '__main__':
 
    # Entrada #: um conjunto de itens
    nums = [7, 3, 1, 5, 4, 8]
 
    if partition(nums):
        print('Set can be partitioned')
    else:
        print('Set cannot be partitioned')
