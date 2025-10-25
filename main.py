import sys
from stats import word_count
from stats import char_count
from stats import sort_dict

def main():
    
    if(len(sys.argv)!=2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    #path = "books/frankenstein.txt"
    path = sys.argv[1]
    character_list = get_book_text(path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {character_list[0]} total words")
    
    #sorted_dict = sorted(character_list[1]) 

    ordered_dict = sorted(character_list[1].items(), key=lambda x:x[1],reverse=True)
    converted_dict = dict(ordered_dict)


    #for k, v in character_list[1].items():
    for k, v in converted_dict.items():
        if(k.isalpha()):
            print(f"{k}: {v}")

    print("============= END ===============")

    #pprint(character_list[1])
    
    #for item in character_list[1]:
     #   if(item.isalpha()):
      #      print(item)


            
            

def get_book_text(book_path):
    with open(book_path) as f:
        book_string = f.read()
        num_of_words = word_count(book_string)
        # print(f"Found {num_of_words} total words")
        
        num_of_chars = char_count(book_string)
        #print(num_of_chars)
        return num_of_words, num_of_chars

main()