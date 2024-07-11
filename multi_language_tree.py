import re
class TreeNode:
    def __init__(self, word, language):
        self.word = word
        self.language = language
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)

class WordTree:
    def __init__(self):
        self.root = None

    def get_node(self, word, language, node=None):
        if node is None:
            node = self.root
        if node.word == word and node.language == language:
            return node
        for child in node.children:
            result = self.get_node(word, language, child)
            if result:
                return result
        return None

    def add_word(self, word, language, translations):
        if self.root is None:
            self.root = TreeNode(word, language)
        parent_node = self.get_node(word, language)
        if parent_node is None:
            parent_node = TreeNode(word, language)
            self.root.children.append(parent_node)
        for child_word, child_language in translations:
            # print(child_word, child_language)
            if not self.get_node(child_word, child_language, self.root):
                parent_node.children.append(TreeNode(child_word, child_language))

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level
   
    def print_tree(self, node, level=0):
        value = f'{node.word} ({node.language})'
        spaces = ' ' * level * 3
        prefix = spaces + "|__" if level !=0 else ""
        print(prefix + value)
        for child in node.children:
            self.print_tree(child, level + 1)

    def find_direct_translations(self, word, language):
        node = self.get_node(word, language)
        if node:
            return [(child.word, child.language) for child in node.children]
        return []
    
    def find_all_translations(word, language):
        pass

    def delete_translation(self, word, language):
        pass
    
    def shortest_translation_path(word, language, translation_word, translation_language):
        pass
#---------------------------------------------------------------------------------------
def clean_data(data):
    cleaned_string = re.sub(r'[\[\]()"\' ]', '', data)
    return cleaned_string

def split_word_language(data):
    word = data[0]
    word = clean_data(word)
    language = data[1]
    language = clean_data(language)
    return word, language

def read_input(file_name):
    tree = WordTree()
    Warnings = []
    with open(file_name, 'r',encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            try:
                #split each line in command and data
                temp = line.strip().split('(',1)
                command = temp[0]
                data = temp[1].strip().split(',') #convert to list
                # print(command,": ",data)
                if command == "add_word":
                    word, language = split_word_language(data)
                    translation =[]
                    # print(f"word = {word}, language= {language}")
                    for i in range(2, len(data),2):
                        tmp =[]
                        translated_word = data[i]
                        translated_language = data[i + 1]
                        translated_word = clean_data(translated_word)
                        tmp.append(translated_word)
                        translated_language = clean_data(translated_language)
                        tmp.append(translated_language)
                        translation.append(tmp)
                    tree.add_word(word, language, translation)
                elif command == "delete_translation":
                    word, language = split_word_language(data)
                    translated_word = data[2].strip('"')
                    translated_language = data[3].strip('"')
                    # delete_translation(word, language, translated_word, translated_language)
            
                elif command == "find_direct_translations":
                    word, language = split_word_language(data)
                    translations = tree.find_direct_translations(word, language)
                    print(f"Direct translations of {word} in {language}: {translations}")
                
                elif command == "find_all_translations":
                    word, language = split_word_language(data)
                    translations = tree.find_all_translations(word, language)
                    print(f"All translations of {word} in {language}: {translations}")
                
                elif command == "shortest_translation_path":
                    word, language = split_word_language(data)
                    translation_word = data[2].strip('"')
                    translation_language = data[3].strip('"')
                    path = tree.shortest_translation_path(word, language, translation_word, translation_language)
                    print(f"Shortest translation path from {word} in {language} to {translation_word} in {translation_language}: {path}")

            except Exception as e:
                Warnings.append(f"Error executing operation: {line.strip()}. Exception: {str(e)}")

    tree.print_tree(tree.root)
    with open(Warning_file, 'w') as file:
        for warning in Warnings:
            file.write(warning + "\n")

if __name__ == "__main__":
    input_file = "multi language tree/inputPS01.txt"
    Warning_file = "multi language tree/warning.txt"
    output_file = "multi language tree/outputPS01.txt"
    read_input(input_file)
    
