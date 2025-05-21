class ChordFunctions:
    
    def toner_entry(a):
        clear_list = []
        for i in a:
            if i != '':
                clear_list.append(i)
        return clear_list

    def toner_converter(a, b, c):
        main_tone = a
        new_tone = b
        result_box = []

        toneList = ["Do","Do#","Re","Re#","Mi","Fa","Fa#","Sol","Sol#","La","La#","Si",
                      "Do","Do#","Re","Re#","Mi","Fa","Fa#","Sol","Sol#","La","La#","Si"]
        signList = ["m","6","7","9"]

        
        listed = c.split(' ')

    # DETECT SINGs:
        resBox = []
        for ls in signList:
            if ls in c:
                response = "yes"
                if response not in resBox:
                    resBox.append(response)

        auto_bool = "".join(map(str, resBox))

        indDecodBox = []
        namElemenBox = []
        sigElemenBox = []
        
        for li in listed:
            for ls in signList:
                if ls in li:
                    
                    # INDEX INPUTs
                    indDecod = listed.index(li)
                    indDecodBox.append(indDecod)

                    # ELEMENT NAME
                    namElem = listed[indDecod]
                    namElemenBox.append(namElem)

                    # SIGN
                    sigElemen = ls
                    sigElemenBox.append(sigElemen)
        # SIGNs REMOVED
        clearInput = c.replace("m","").replace("6","").replace("7","").replace("9","")
        inputBox = clearInput.split(" ")
        
    # TONE CATCHER
        start = toneList.index(main_tone)
        end = toneList.index(new_tone)

        # BOOLEAN METHOD
        mainOperation = start > end
        
        mainBox = [] # contiene los cambios
        dltBox = [] # contiene los elementos a sustituir
        newItem = [] # contiene la formacion de los nuevos elementos
        convBox = []
        get_new_tone = []

        if mainOperation == True:
            if auto_bool == "yes":
                op = start - end

                try:
                    for l in inputBox:
                        searchIndex = toneList.index(l)
                        changeIndex = searchIndex - op

                        elemIndex = toneList[changeIndex]
                        mainBox.append(elemIndex)

                    # GET THE CHANGED ELEMENTS ACCORDING TO THE INDEX ***
                    for ind in indDecodBox:
                        new = mainBox[ind]
                        convBox.append(new)
                    # RETURN THE SIGN TO THE ORIGINAL ELEMENT
                    for elem, sign in zip(convBox, sigElemenBox):
                        result = f"{elem}{sign}"
                        newItem.append(result)
                    
                    for i in indDecodBox:
                        dlt = mainBox[i]
                        dltBox.append(dlt)
                    
                    for dlt in dltBox:
                        mainBox.remove(dlt)

                    # END PROCESS
                    indexs = indDecodBox
                    strings = newItem

                    for ib, sb in zip(indexs, strings):
                        mainBox.insert(ib, sb)
                    
                    process_finished = " ".join(map(str, mainBox))
                    result_box.append(process_finished)
                except:
                    result_box.append('')

            else:
                op = start - end
                
                try:
                    for l in inputBox:
                        searchIndex = toneList.index(l)
                        changeIndex = searchIndex - op

                        elemIndex = toneList[changeIndex]
                        mainBox.append(elemIndex)

                    process_finished = " ".join(map(str, mainBox))
                    result_box.append(process_finished)
                except:
                    result_box.append('')


        else:
            if auto_bool == "yes":
                op = end - start

                try:
                    for l in inputBox:
                        searchIndex = toneList.index(l)
                        changeIndex = searchIndex + op

                        elemIndex = toneList[changeIndex]
                        mainBox.append(elemIndex)

                    # GET THE CHANGED ELEMENTS ACCORDING TO THE INDEX ***
                    for ind in indDecodBox:
                        new = mainBox[ind]
                        convBox.append(new)
                    # RETURN THE SIGN TO THE ORIGINAL ELEMENT
                    for elem, sign in zip(convBox, sigElemenBox):
                        result = f"{elem}{sign}"
                        newItem.append(result)
                    
                    for i in indDecodBox:
                        dlt = mainBox[i]
                        dltBox.append(dlt)
                    
                    for dlt in dltBox:
                        mainBox.remove(dlt)

                    # END PROCESS
                    indexs = indDecodBox
                    strings = newItem

                    for ib, sb in zip(indexs, strings):
                        mainBox.insert(ib, sb)

                    process_finished = " ".join(map(str, mainBox))
                    result_box.append(process_finished)
                    
                except:
                    result_box.append('')

            else:
                op = end - start
                
                try:
                    for l in inputBox:
                        searchIndex = toneList.index(l)
                        changeIndex = searchIndex + op

                        elemIndex = toneList[changeIndex]
                        mainBox.append(elemIndex)

                    process_finished = " ".join(map(str, mainBox))
                    result_box.append(process_finished)
                except:
                    result_box.append('')
        return result_box