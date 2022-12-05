import datetime
#Read evernote note
import PASS
from evernote.edam.type.ttypes import NoteSortOrder
from evernote.edam.notestore.ttypes import NoteFilter, NotesMetadataResultSpec
from evernote.api.client import EvernoteClient

def main():
    #find the token by going to evernote web and finding it in the cookies. "auth" cookie
    evernote_token = PASS.evernote_token
    client = EvernoteClient(token=evernote_token, sandbox=False)
    userStore = client.get_user_store()
    noteStore = client.get_note_store()
    notebooks = noteStore.listNotebooks()

    # sortOrder = NoteSortOrder("UPDATED")

    for n in notebooks:
        print(n.name)
        filter = NoteFilter(order=2, ascending=False, notebookGuid=n.guid) #reverse chronological
        resultSpec = NotesMetadataResultSpec()
        resultSpec.includeTitle = True
        resultSpec.includeContentLength = True
        resultSpec.includeCreated = True
        resultSpec.includeContent = True
        resultSpec.includeUpdated = True
        resultSpec.includeNotebookGuid = True
        resultSpec.includeAttributes = True
        resultSpec.includeTagGuids = True
        resultSpec.includeLargestResourceMime = True
        resultSpec.includeLargestResourceSize = True        

        notes = noteStore.findNotesMetadata(evernote_token, filter, 0, 1, resultSpec)
        #Evernote stores its date/time values in epoch time - the number of seconds since 1/1/1970.
        for note in notes.notes:
            print(note.guid)
            #print(note.updated)
            title = note.title
            date = note.updated
            formatted_date = float(note.updated)/1000
            print(datetime.datetime.fromtimestamp(formatted_date))#has to be in seconds not milliseconds
            content = noteStore.getNoteContent(evernote_token, note.guid)
            print(title)
            print(formatted_date)
            print(content)    
        print()        
    
main()
exit()