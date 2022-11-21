#Read evernote note
import PASS
from evernote.edam.type.ttypes import NoteSortOrder
from evernote.edam.notestore.ttypes import NoteFilter, NotesMetadataResultSpec
from evernote.api.client import EvernoteClient


def main():
    client = EvernoteClient(token=PASS.personal_token, sandbox=False)
    userStore = client.get_user_store()
    #user = userStore.getUser()
    #print(user.username)
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
    notes = noteStore.findNotesMetadata(PASS.personal_token, filter, 0, 100, resultSpec) #(authenticationToken, filter, offset, maxNotes)

    
    #notes = [self.getNoteByGuid(i.guid) for i in notes.notes]

    #meta = notes.getNotes()
    #print(notes)
    #print(notes.notes)
    
    i = 0
    for note in notes.notes:
        if i < 10:
            print(note.guid)
            content = noteStore.getNoteContent(PASS.personal_token, note.guid)
            print(content)
            i = i + 1

main()
exit()

