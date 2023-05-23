class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        current_line = []
        current_length = 0
        
        for word in words:
            if current_length + len(word) + len(current_line) > maxWidth:
                # We need to start a new line
                lines.append(self.justifyLine(current_line, maxWidth, current_length))
                current_line = []
                current_length = 0
            current_line.append(word)
            current_length += len(word)
        
        # Handle the last line
        last_line = " ".join(current_line)
        last_line += " " * (maxWidth - len(last_line))
        lines.append(last_line)
        
        return lines
    
    def justifyLine(self, line: List[str], maxWidth: int, current_length: int) -> str:
        if len(line) == 1:
            # Left-justify if there's only one word on the line
            return line[0] + " " * (maxWidth - len(line[0]))
        
        total_spaces = maxWidth - current_length
        space_gaps = len(line) - 1
        spaces_per_gap = total_spaces // space_gaps
        extra_spaces = total_spaces % space_gaps
        
        justified_line = ""
        for i, word in enumerate(line):
            justified_line += word
           # Add spaces between words
            if i < len(line) - 1:
                spaces_to_add = spaces_per_gap
                if i < extra_spaces:
                    spaces_to_add += 1
                justified_line += " " * spaces_to_add
        
        return justified_line
