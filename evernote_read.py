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

    for n in notebooks:
        print(n.name)

    filter = NoteFilter()
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

    notes = noteStore.findNotesMetadata(evernote_token, filter, 0, 100, resultSpec)     
    i = 0
    for note in notes.notes:
        if i < 10:
            print(note.guid)
            content = noteStore.getNoteContent(evernote_token, note.guid)
            print(content)
            i = i + 1

main()
exit()

