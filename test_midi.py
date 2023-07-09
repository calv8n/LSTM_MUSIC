import os
import json
import music21 as m21
import numpy as np
import tensorflow.keras as keras

MIDI_DATASET_PATH = "piano/pianoscore_0.mid"
SAVE_DIR = "dataset_mid"
SINGLE_FILE_DATASET = "file_dataset_mid"
MAPPING_PATH = "mapping_mid.json"
SEQUENCE_LENGTH = 64

song = m21.converter.parse(MIDI_DATASET_PATH)
song.show(fmt='musicxml')
