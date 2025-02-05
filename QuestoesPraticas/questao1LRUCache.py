from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()  # Armazena os itens do cache
        self.capacity = capacity    # Capacidade máxima do cache

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1  # Retorna -1 se a chave não existir
        else:
            # Move o item para o final (indicando que foi usado recentemente)
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Atualiza o valor e move para o final
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # Remove o item menos recentemente usado (primeiro da OrderedDict)
            self.cache.popitem(last=False)