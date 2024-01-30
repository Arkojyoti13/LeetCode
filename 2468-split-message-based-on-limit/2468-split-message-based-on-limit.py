class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        def splitable_within(parts_limit):
            # check the message length achievable with <parts_limit> parts
            length = sum(limit - len(str(i)) - len(str(parts_limit)) - 3 for i in range(1, parts_limit + 1))
            return length >= len(message)
        
        parts_limit = 9
        if not splitable_within(parts_limit):
            parts_limit = 99
        if not splitable_within(parts_limit):
            parts_limit = 999
        if not splitable_within(parts_limit):
            parts_limit = 9999
        if not splitable_within(parts_limit):
            return []
        
        # generate the actual message parts
        parts = []
        m_index = 0  # message index
        for part_index in range(1, parts_limit + 1):
            if m_index >= len(message): break
            length = limit - len(str(part_index)) - len(str(parts_limit)) - 3
            parts.append(message[m_index:m_index + length])
            m_index += length
        
        return [f'{part}<{i + 1}/{len(parts)}>' for i, part in enumerate(parts)]