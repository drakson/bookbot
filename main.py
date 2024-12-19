


def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    num_of_words = get_num_words(text)
    
    num_of_chars = char_count(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_of_words} words found in the document")  
    print("\n")
    characters = []
    for key in num_of_chars:
        if key.isalpha():
            characters.append({key:num_of_chars[key]})
    characters.sort(reverse=True, key=sort_on)   
    for i in characters:
        for key in i:
            print(f"The '{key}' character was found {i[key]} times") 

    print("--- End report ---")    

def get_text(path):
    with open(path) as f:
        return f.read()      
      

def get_num_words(text):
    words = text.split()
    return len(words)

def char_count(text):
    char_dict = {}
    
    for char in text:
        lower = char.lower()
        if lower not in char_dict:
            char_dict[lower] = 1
        else:
            char_dict[lower] = char_dict[lower] + 1    
        
    return char_dict

def sort_on(dic):
    for key in dic:
        if key.isalpha():
            return dic[key]

main()