import wikipedia

def summary(landmark_description):
#from landmark_detect import landmark_description

# Search function (1 result)

    landmark_name = (wikipedia.search(landmark_description, results=1))

    landmark_summary = (wikipedia.summary(landmark_name, sentences=4))

    # Suggestion function

    #print(wikipedia.suggest("alpe d'huez"))
    #landmark_description = (wikipedia.suggest("alpe d'huez"))

    return landmark_summary