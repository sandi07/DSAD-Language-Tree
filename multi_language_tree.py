class Word:
    def __init__(self, text = "", language = "", translations = []):
        self.text = text
        self.language = language
        self.translations = []
    
    # Adds a new node given by text, language and adds the list of translations to the node created
    def add_word(self, text: str, language: str, translations:  list) -> None:
        pass
    
    # Similarly other class functions can be added here

    def add_word(self, word, language, translations):
        print("Add word-----------")
        # print(f"Command: {word}")
        # print(f"Language: {language}")
        # print(f"translations: {translations}")
        
    def find_node(self, node, word, language):
        print("find node-----------")
        # print(f"node: {node}")
        # print(f"word: {word}")
        # print(f"language: {language}")

    def add_translations(self, word, language, translations):
        print("add translation------------")
        # print(f"Command: {word}")
        # print(f"Language: {language}")
        # print(f"translations: {translations}")

    def search_translation(self, word, language, target_language):
        print("search translation-----------")
        # print(f"Command: {word}")
        # print(f"Language: {language}")
        # print(f"target_language: {target_language}")

    def delete_translation(self, word, language, translation_word, translation_language):
        print("delete translation-------------")
        # print(f"Command: {word}")
        # print(f"Language: {language}")
        # print(f"translation_word: {translation_word}")
        # print(f"translation_language: {translation_language}")

    def find_direct_translations(self, word, language):
        print("find direct translation-----------")
        # print(f"Command: {word}")
        # print(f"Language: {language}")

    def find_all_translations(self, word, language):
        print("find all translation----------")
        # print(f"Command: {word}")
        # print(f"Language: {language}")

    def shortest_translation_path(self, word, language, translation_word, translation_language):
        print("find shortest translation--------")
        # print(f"Command: {word}")
        # print(f"Language: {language}")
        # print(f"translation_word: {translation_word}")
        # print(f"translation_language: {translation_language}")

    def print_tree(self, node, level):
        print("print trees-----")
        print(f"node: {node}")
        print(f"level: {level}")



def read_input(file_name):
    tree = Word()
    Warnings = []
    with open(file_name, 'r',encoding='utf-8') as file:
        operations = file.readlines()
        for operation in operations:
            try:
                eval(tree.operation.strip())  # Using eval cautiously assuming input is trusted and formatted correctly
            except Exception as e:
                Warnings.append(f"Error executing operation: {operation.strip()}. Exception: {str(e)}")

    with open(Warning_file, 'w') as file:
        for warning in Warnings:
            file.write(warning + "\n")


if __name__ == "__main__":
    input_file = "inputPS01.txt"
    Warning_file = "warning.txt"
    output_file = "outputPS01.txt"
    query_task =read_input(input_file)
    # print(query_task)

