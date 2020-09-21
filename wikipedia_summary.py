import wikipedia

# Search function (1 result)

landmark_description = (wikipedia.search("burj al arab", results=1))

print(wikipedia.summary(landmark_description, sentences=4))

# Suggestion function

#print(wikipedia.suggest("alpe d'huez"))
#landmark_description = (wikipedia.suggest("alpe d'huez"))