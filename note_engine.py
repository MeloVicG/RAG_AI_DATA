from llama_index.core.tools import FunctionTool
import os

note_file = os.path.join("data", "notes.txt")


def save_note(note, note_type=""):
    full_note = f"{note_type}: {note}" if note_type else note
    if not os.path.exists(note_file):
        open(note_file, "w")

    with open(note_file, "a") as f:
        f.writelines([full_note + "\n"])

    # The LLM is able to look at the value of the return function
    # ex. "successful" or "failed"
    return "note saved"


note_engine = FunctionTool.from_defaults(
    fn=save_note,
    name="note_saver",
    description="this tool can save a text based note to a file for the user"
)