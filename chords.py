from music21 import *
import pandas as pd

MIDI_PATH = "piano/pianoscore_0.mid"
keyboard_instruments = ["KeyboardInstrument", "Piano", "Harpsichord", "Clavichord", "Celesta", ]

def get_notes_chords_rests(instrument_type, path):
    try:
        midi = converter.parse(path)
        parts = instrument.partitionByInstrument(midi)
        note_list = []
        for music_instrument in range(len(parts)):
            if parts.parts[music_instrument].id in instrument_type:
                for element_by_offset in stream.iterator.OffsetIterator(parts[music_instrument]):
                    for entry in element_by_offset:
                        if isinstance(entry, note.Note):
                            note_list.append(str(entry.pitch))
                        elif isinstance(entry, chord.Chord):
                            note_list.append('.'.join(str(n) for n in entry.normalOrder))
                        elif isinstance(entry, note.Rest):
                            note_list.append('Rest')
        return note_list
    except Exception as e:
        print("failed on ", path)
        pass



if __name__ == "__main__":
    notes = get_notes_chords_rests(keyboard_instruments, MIDI_PATH)
    print(notes)