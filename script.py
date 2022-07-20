from backend.api.snippet import get_all_snippets, get_random_snippet

text = get_random_snippet()
# text = snippet.snippet
print(text)
text = text.replace("\n","<enter>")
text = text.replace("\t","<tab>")
text = text.replace("    ","<tab>")
print(text)