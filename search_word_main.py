from crawler_module import funcSearch
import sys

def main():
    try:
        tree_arg = sys.argv[1] #jeg benytter (try:) fordi ellers allerede her vil sys.argv smide en error hvis der mangler argument
        fileExt_arg = sys.argv[2]
        word_arg = sys.argv[3]
        funcSearch(tree_arg, fileExt_arg, word_arg)
    except IndexError:
        print("\n"*5, """\n\n     
        HUSK argumenter til programmet ! \n
        se eksemple:\n
        python search_word_main.py $HOME/Downloads txt malware\n
        eller feks:\n
        python search_word_main.py $HOME pdf malware""", "\n"*5)
      
if __name__ == "__main__":
    main()




    