from typing import List

class MeshArray:
    def __init__(self, mesh: List[str]):
        self.mesh = mesh

    def can_mesh(self, word1, word2):
        initiator = word2[0]
        if initiator in word1:
            index = word1.rfind(initiator)
            substring = word1[index:]
            if substring in word2:
                return True, substring
        return False,''

    def check_array(self):
        output_string = ''
        for i in range(len(self.mesh) - 1):
            bool_value, substring = self.can_mesh(self.mesh[i], self.mesh[i + 1])
            if bool_value:
                output_string += substring
                print(output_string)
            else:
                print("failed to mesh")
                break 
    

my_array = ["kingdom", "dominator", "notorious", "usual", "allegory"]
mesh_array = MeshArray(my_array)
mesh_array.check_array()


#optimized
from typing import List

def mesh_words(words: List[str]) -> str:
    def get_mesh_suffix(w1, w2):
        # Start from the end of w1 and match with the start of w2
        min_len = min(len(w1), len(w2))
        for i in range(1, min_len + 1):
            if w1[-i:] == w2[:i]:
                match = w1[-i:]
        return match if 'match' in locals() else None

    output = ''
    for i in range(len(words) - 1):
        mesh = get_mesh_suffix(words[i], words[i + 1])
        if mesh:
            output += mesh
        else:
            return "failed to mesh"
    return output
