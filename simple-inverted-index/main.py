from past.builtins import raw_input

from database import Database
from inverted_index import InvertedIndex


def highlight_term(id, term, text):
    replaced_text = text.replace(term, "\033[1;32;40m {term} \033[0;0m".format(term=term))
    return "--- document {id}: {replaced}".format(id=id, replaced=replaced_text)


def run():
    db = Database()
    index = InvertedIndex(db)
    document1 = {
        'id': '1',
        'text': 'The big sharks of Belgium drink beer.'
    }
    document2 = {
        'id': '2',
        'text': 'Belgium has great beer. They drink beer all the time.'
    }
    index.index_document(document1)
    index.index_document(document2)

    search_term = raw_input("Enter term(s) to search: ")
    result = index.lookup_query(search_term)

    for term in result.keys():
        for appearance in result[term]:
            # Belgium: { docId: 1, frequency: 1}
            document = db.get(appearance.docId)
            print(highlight_term(appearance.docId, term, document['text']))
        print("-----------------------------")


if __name__ == '__main__':
    run()
