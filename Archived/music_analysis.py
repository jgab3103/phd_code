

import music21 as mu
import json as js
import simplejson as sjs

#get example from file, convert into an mu object
notes = mu.converter.parse('keithjarrett.xml')

#create list of parts
i = 0
parts_list = []
while i < len(notes.parts):
    parts_list.append(notes.parts[i])
    i = i + 1

notes_list = []
part_name_list = []
for part in parts_list:
    a = part.flat.getElementsByClass(mu.note.Note)
    b = part.id
    notes_list.append(a)
    part_name_list.append(b)
    


iterator = 0
all_parts_list = []
for each_list in notes_list:
    list_of_note_dicts = []
    song_location = 0
    for each_note in each_list:
        note_dict = {}
        note_dict['frequency'] = each_note.midi
        note_dict['duration'] = each_note.quarterLength
        note_dict['current_position'] = each_note.offset
        note_dict[str(each_note.offset)] = each_note.offset
        note_dict['part'] = part_name_list[iterator]
        note_dict['current_tempo'] = 180
        note_dict['current_time_signature'] = '4/4'
        note_dict['composer'] = 'KeithJarrett'
        note_dict['creation_date'] = ''
        note_dict['song_location'] = song_location
        
        song_location = song_location + 1
        
        list_of_note_dicts.append(note_dict) 
    all_parts_list.append(list_of_note_dicts)
    iterator = iterator + 1
   

print all_parts_list


class AnalyseParts:
    def __init__(self, parts):
        print 'init'
        self.points_in_time = []
        self.parts_list = parts
        
        #lookup for chord types
        self.dom_seventh_chord = [(4,3,3)]
        self.maj_seventh_chord = [(4,3,4)]
        self.min_seventh_flat_five_chord = [(3,3,4)]
        self.min_seventh_chord = [(3,4,3)]
        
        #init from list of parts
        for parts in parts_list:
            seventh_count = 0
            prev_root_freq = -1
            prev_third_freq = -1
            prev_fifth_freq = -1
            prev_seventh_freq = -1
            prev_ninth_freq = -1
            prev_eleventh_freq = -1
            prev_thirteenth_freq = -1
            prev_mel_freq = -1
    
        #find related frequencies
            for note in parts:
                if note['part'] == 'solo':
                    current_freq = note['frequency']
                    current_loc = note['current_position']
                    points_in_time.append([current_loc, current_freq])
        print points_in_time
    

    def get_summary(self):
        print self.points_in_time

'''    def look_up_chord(chord_to_look_up):
        if chord_to_look_up == dom_seventh_chord:
            print 'This is a seventh chord'
        elif chord_to_look_up == maj_seventh_chord:
            print "Major Chord"
        elif chord_to_look_up == min_seventh_flat_five_chord:
            print 'Min 7b5 chord'
        elif chord_to_look_up == min_seventh_chord:
            print 'min 7 '
        else:
            print 'could not figure out chord'
        return chord
    
    
    def look_up_related_frequencies(current_freq, current_loc): 
        print 'here'
        root_freq = None
        third_freq = None
        fifth_freq = None
        seventh_freq = None
        ninth_freq = None
        eleventh_freq = None
        thirteenth_freq = None
        mel_freq = None
    
        for parts in all_parts_list:
            for note in parts:
                if note['part'] == 'root' and note['current_position'] == current_loc:
                    root_freq = note['frequency']
                elif note['part'] == 'third' and note['current_position'] == current_loc:
                    third_freq = note['frequency']
                elif note['part'] == 'fifth' and note['current_position'] == current_loc:
                    fifth_freq = note['frequency']
                elif note['part'] == 'seventh' and note['current_position'] == current_loc:
                    seventh_freq = note['frequency']
                elif note['part'] == 'ninth' and note['current_position'] == current_loc:
                    ninth_freq = note['frequency']
                elif note['part'] == 'thirteenth' and note['current_position'] == current_loc:
                    thirteenth_freq = note['frequency']
                elif note['part'] == 'mel' and note['current_position'] == current_loc:
                    mel_freq = note['frequency']
                else:
                    print '_exception_raised'
    
        return root_freq, third_freq, fifth_freq, seventh_freq, ninth_freq, eleventh_freq, thirteenth_freq, mel_freq'''

model = AnalyseParts(all_parts_list)
model.get_summary()


    
    