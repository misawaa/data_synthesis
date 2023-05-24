class Solution:
    def simplifyPath(self, path: str) -> str:
        # Split the input path by slashes
        path_list = path.split("/")
        
        # Initialize a stack to keep track of the directories
        stack = []
        
        # Traverse through each directory in the path
        for directory in path_list:
            # Ignore empty directories and current directory (".")
            if directory == "" or directory == ".":
                continue
            
            # Move up one level if the directory is the parent directory ("..")
            if directory == "..":
                if stack:
                    stack.pop()
            
            # Otherwise, add the directory to the stack
            else:
                stack.append(directory)
        
        # Join the directories in the stack with slashes to form the simplified canonical path
        return "/" + "/".join(stack)
      
