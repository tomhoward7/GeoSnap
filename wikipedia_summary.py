import wikipedia

def summary(landmark_description):

    landmark_name = (wikipedia.search(landmark_description, results=1))

    landmark_summary = (wikipedia.summary(landmark_name, sentences=4))

    return landmark_summary