from rich import print as rprint
from rich.console import Console 

rprint = Console(highlight = False).print


print("What type of work are you citing?")
print('''(1): Journal Article\n
(2): Book\n
(3): Dataset\n
(4): Other''')
full_citation = ""
while True:
    work_type = input()
    if work_type == "1": 
        print("Provide the following details in the following format: Names of authros (formatted last, first)|year of publication|title of paper|title of journal|volume of journal|issue or citation number|page range|DOI")
        break
        # TASK: Need to make journal citation
    # TASK: Make this handle None as an input. 
    # TASK: Make this handle multi-author works. 
    elif work_type == "2": 
        print("Are you citing a whole book (1) or a chaper in a book (2)?")
        book_pOw = input()
        if book_pOw == "1": 
            print("Provide the following details in the following format: Names of authors (formatted last, first)|year of publication|title of book|publisher's name|total pages")
            citation_information = input()
            citation_information = citation_information.strip()
            citation_information = list(citation_information.split("|"))
            count = 0
            for i in range(len(citation_information)):
                if i == 0: # Name
                    for char in citation_information[0]: 
                        if char == ',': 
                            first_initial = citation_information[0][citation_information[0].index(char) + 2]
                            last_name = citation_information[0][:citation_information[0].index(char)] 
                else: 
                    continue
            print("This is your full citation:")
            rprint(f"{last_name}, {first_initial}., {citation_information[1]}: [italic]{citation_information[2]}[/italic]. {citation_information[3]}, {citation_information[4]} pp.")

        elif book_pOw == "2": 
            print("Provide the following details in the following format: Names of the auhors|year of publication|title of chapter|title of book|editors|publisher's name|page range")
            
    elif work_type == "3": 
        print("Provide the following details in the following format: Dataset Title|version|archive/distributor|access date (DD, MM, YYYY)|data locaor/identifier (doi or URL): ")
        break
        # TASK: Need to make dataset citations

    elif work_type == "4": 
        print('''Which of the following are you citing:\n
            (1): Conference proceedings, preprints, extended abstracts\n
            (2): Dissertation/thesis\n
            (3): Report/note/memo\n
            (4): Web page\n
            (5): Unpublished material''')
        other_choice = input()
        if other_choice == "1": 
            print()
        elif other_choice == "2": 
            print()
        elif other_choice == "3":
            print()
        elif other_choice == "4": 
            print()
        elif other_choice == "5": 
            print()
        else: 
            print()
        break
        #TASK: Need to make 'other' citations
    else: 
        print("Invalid choice, try again.")