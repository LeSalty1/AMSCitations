from rich import print as rprint
from rich.console import Console 
import arxiv 

rprint = Console(highlight = False).print

def format_authors(full_name): 
    parts = full_name.strip().split()
    last_name = parts[-1] 
    first_mid = parts[:-1]

    initials = [f"{name[0]}." for name in first_mid] 

    return f"{' '.join(initials)} {last_name}"  

def generate_ams_citation(id):
    format_id = str(id) 
    client = arxiv.Client()
    search = arxiv.Search(id_list = [format_id])
    paper = next(client.results(search), None)
  
    if not paper: 
        raise ValueError("No paper was found with this ID.")

    authors = [auth.name for auth in paper.authors]
    formatted_auths = [format_authors(auth) for auth in authors]
    if len(formatted_auths) == 1: 
        author_str = formatted_auths[0]
    elif len(formatted_auths) == 2: 
        author_str = f"{formatted_auths[0]} and {formatted_auths[1]}"
    else: 
        author_str = f"{', '.join(formatted_auths[:-1])}, and {formatted_auths[-1]}"

    year = paper.published.year
    title = paper.title.strip().replace("\n", " ")

    rprint(f"{author_str}, [italic]{title}[/italic], arXiv:{format_id}, {year}.")
