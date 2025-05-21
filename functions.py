from hymnal import hymn
from classes import ChordFunctions

class InputSong:
    def inputs(inputSong, inputNewTone):
        # INPUTS:
        iptSong = inputSong.lower()

        my_song = hymn['song'][iptSong]
        song_chords = my_song['chords']
        tone_song = my_song['tone']
        new_tone = inputNewTone

        blank_list = []
        slash_list = []
        final_product = []
        get_tone_list = []

        for i in song_chords:
            # WORKS ON SLASHs
            slash_replacer = i.replace('/',' / ')
            slash_identify = slash_replacer.split(' ')
            slash_list.append(slash_identify)
            # WORKS ON BLANKs
            blank_replacer = i.replace('/',' ')
            identify = blank_replacer.split(' ')
            blank_list.append(identify)


        # INDEX OF SLASH SIGNS:
        slash_target_list = []

        for x in slash_list:
            slash_finder = [t for t, s in enumerate(x) if s=='/']
            slash_target_list.append(slash_finder)


        # BLANK SPACES FINDER:
        target = ''
        target_list = []
        send_list =[]
        convert_list =[]
        result_list =[]

        for bl in blank_list:
            finder = [t for t, s in enumerate(bl) if s==target]
            target_list.append(finder)

        for b in blank_list:
            get_class = ChordFunctions.toner_entry(b)
            send_list.append(get_class)

        for sl in send_list:
            item = " ".join(map(str, sl))
            convert_list.append(item)

        for cl in convert_list:
            send_tones = ChordFunctions.toner_converter(tone_song, new_tone, cl)
            result_list.append(send_tones)
        
        # RETURNING SLASHEs
        returnList = []
        for element in result_list:
            splt = element[0].split(' ')
            returnList.append(splt)

        # GETING TONES FOR THE LIST IMAGES
        for i in returnList:
            for x in i:
                if x != '' and x not in get_tone_list:
                    get_tone_list.append(x)
        
        """ OUTPUT ***************************************************************"""
        # INSERT BLANK SPACES:
        for bl_index, tl in enumerate(target_list):
            for i in tl:
                returnList[bl_index].insert(i, '')

        #print('---------------------------------------------------------------')


        # RESULT:
        for index, result in enumerate(slash_target_list):
            for r in result:
                returnList[index].insert(r, '/')

        for c in returnList:
            joined = " ".join(map(str, c))
            final_product.append(joined)

        final_product.append(get_tone_list)
        return final_product