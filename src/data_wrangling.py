import pandas as pd

def importDataset(path):
    data = pd.read_csv(path, sep=";", header=0, engine="python")
    df = pd.DataFrame(data)
    df = df.drop(df.index[0])
    return df

def filterColumns(df, columns):
    return df.filter(columns)

def prepareActorName(actorName):
    actorName = actorName.split()
    actorName = actorName[1] + ", " + actorName[0]
    return actorName

def prepareSubject(subjectName):
    return subjectName.title()


def findMovieByActor(df, actor):
    return df.query("Actor == \"" + prepareActorName(actor) + "\"")

def findMovieBySubject(df, subject):
    return df.query("Subject == \"" + prepareSubject(subject) + "\"")

def findMovieByActorAndSubject(df, actor, subject):
    df = findMovieByActor(df, actor)
    df = findMovieBySubject(df, subject)
    return df

df = importDataset("src/datasets/film.csv")
df = filterColumns(df, ["Year", "Title", "Subject", "Actor", "Actress"])

print("")
actors = ["Nicolas Cage", "Sean Connery"]
subjects = ["Comedy", "Drama", "Horror"]
for actor in actors:
    print("There are " + str(len(findMovieByActor(df, actor))) + " movies with " + actor + " in the dataset.")
    for subject in subjects:
        print("There are " + str(len(findMovieByActorAndSubject(df, actor, subject))) + "/" + str(len(findMovieBySubject(df, subject))) + " " + subject + " movies with " + actor + " in the dataset.")
    print("")
