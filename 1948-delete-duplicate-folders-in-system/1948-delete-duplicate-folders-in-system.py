from collections import defaultdict
from typing import List

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        # Build the folder tree
        tree = {}
        for path in paths:
            node = tree
            for folder in path:
                node = node.setdefault(folder, {})
        
        # Function to serialize the folder structure
        def serialize(node):
            if not node:
                return "()"
            children_serializations = []
            for child_name, child_node in node.items():
                children_serializations.append(child_name + serialize(child_node))
            serialization = "".join(sorted(children_serializations))
            duplicates[serialization].append(node)
            return "(" + serialization + ")"
        
        # Function to mark nodes for deletion
        def mark_deletion(nodes):
            for node in nodes:
                node.clear()
                node["#"] = True
        
        # Finding duplicates
        duplicates = defaultdict(list)
        serialize(tree)
        for nodes in duplicates.values():
            if len(nodes) > 1:
                mark_deletion(nodes)

        # Function to collect the remaining paths
        def collect_paths(node, path):
            for child_name, child_node in list(node.items()):
                if "#" in child_node:
                    continue
                new_path = path + [child_name]
                ans.append(new_path)
                collect_paths(child_node, new_path)
        
        # Collecting the result
        ans = []
        collect_paths(tree, [])
                
        return ans