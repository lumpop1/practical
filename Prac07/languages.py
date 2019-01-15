from Prac07.programming_language import ProgrammingLanguage

def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    dynamic =[]
    print(ruby,"\n",python,"\n",visual_basic,"\n","The dynamically typed languages are:")
    if ruby.is_dynamic:
        dynamic.append(ruby.name)
    if python.is_dynamic:
        dynamic.append(python.name)
    if visual_basic.is_dynamic:
        dynamic.append(visual_basic.name)
    print(dynamic)
main()