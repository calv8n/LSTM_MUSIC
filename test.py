from music21 import environment

env = environment.UserSettings()
#env.create()

# check the path
#'''print('Environment settings:') print('musicXML:  ', env['musicxmlPath']) print('musescore: ', env['musescoreDirectPNGPath'])'''


#env['musicxmlPath'] = 'C:/Program Files/MuseScore 4/bin/MuseScore4.exe'
#env['musescoreDirectPNGPath'] = 'C:/Program Files/MuseScore 4/bin/MuseScore4.exe'
print(env['musicxmlPath'])