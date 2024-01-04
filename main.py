with open("books/frankenstein.txt") as f:
    file_conatents = f.read()
    words = file_conatents.split()
    num_words = len(words) 
    
    lower_case_file_conatents = file_conatents.lower()
    dic_letters = {}
    for i in lower_case_file_conatents:
        if i in dic_letters:
            dic_letters[i] = dic_letters[i] + 1
        else:
            dic_letters[i] = 1
    
    print(f"{num_words} words found in the document")
    sorted_list_letters = sorted(dic_letters.items(),key=lambda x:x[1], reverse= True)
    sorted_dic_letters = dict(sorted_list_letters)
    
    for letter in sorted_dic_letters:
        if letter.isalpha():
            print(f"the {letter} character was found {sorted_dic_letters[letter]} times")
    print("--- End report ---")