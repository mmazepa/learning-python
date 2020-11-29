import pandas as pd
import lib.text_based_user_interface as tui

def header():
    tui.textWithIndent(" ____      _       _ _ _                 _ _         ", 3)
    tui.textWithIndent("|    \ ___| |_ ___| | | |___ ___ ___ ___| |_|___ ___ ", 3)
    tui.textWithIndent("|  |  | .'|  _| .'| | | |  _| .'|   | . | | |   | . |", 3)
    tui.textWithIndent("|____/|__,|_| |__,|_____|_| |__,|_|_|_  |_|_|_|_|_  |", 3)
    tui.textWithIndent("                                    |___|       |___|", 3)

def mainMenu():
    tui.textWithIndent("What do you want to do?", 3)
    tui.textWithIndent("1. Search by title, e.g. \"Star Wars\".", 6)
    tui.textWithIndent("2. Search by actor's full name, e.g. \"Mark Hamill\".", 6)
    tui.textWithIndent("3. Search by actress's full name, e.g. \"Carrie Fisher\".", 6)
    tui.textWithIndent("4. Search by subject, e.g. \"Science Fiction\".", 6)
    tui.textWithIndent("5. Exit", 6)

def importDataset(path):
    data = pd.read_csv(path, sep=";", header=0, engine="python")
    df = pd.DataFrame(data)
    df = df.drop(df.index[0])
    return df

def filterColumns(df, columns):
    return df.filter(columns)

def prepareActorName(actorName):
    actorName = actorName.split(" ")
    actorName = actorName[1] + ", " + actorName[0]
    return actorName.title()

def prepareActorName2(actorName):
    actorName = actorName.split(", ")
    if len(actorName) > 1:
        actorName = actorName[1] + " " + actorName[0]
    return str(actorName)

def findMovieByTitle(df, title):
    return df.query("Title.str.contains(\"" + title.title() + "\")")

def findMovieByActor(df, actor):
    return df.query("Actor == \"" + prepareActorName(actor) + "\"")

def findMovieByActress(df, actress):
    return df.query("Actress == \"" + prepareActorName(actress) + "\"")

def findMovieByName(df, name, gender):
    if gender == "male":
        return findMovieByActor(df, name)
    elif gender == "female":
        return findMovieByActress(df, name)

def findMovieBySubject(df, subject):
    return df.query("Subject == \"" + subject.title() + "\"")

df = importDataset("src/datasets/film.csv")
df = filterColumns(df, ["Year", "Title", "Subject", "Actor", "Actress"])

while True:
    tui.clear()
    header()
    tui.newLine()

    tui.framedText("Search the movie by title, cast member or subject.")
    tui.newLine()

    mainMenu()
    decision = tui.inputWithIndent("Decision:", 3)

    if decision == "1":
        type = "title"
        title = tui.inputWithIndent("Title:", 3)
        df_tmp = findMovieByTitle(df, title)
    elif decision == "2":
        type = "actor"
        name = tui.inputWithIndent("Actor's full name:", 3)
        df_tmp = findMovieByName(df, name, "male")
    elif decision == "3":
        type = "actress"
        name = tui.inputWithIndent("Actress's full name:", 3)
        df_tmp = findMovieByName(df, name, "female")
    elif decision == "4":
        type = "subject"
        subject = tui.inputWithIndent("Subject:", 3)
        df_tmp = findMovieBySubject(df, subject)
    elif decision == "5":
        tui.log("INFO", "Okay, goodbye and have a nice day!")
        tui.newLine()
        quit()
    else:
        tui.log("INFO", "Unrecognised option, type \"1\", \"2\", \"3\", \"4\" or \"5\".")
        tui.pressAnyKey()
        continue

    size = len(df_tmp)

    if size == 0:
        tui.log("INFO", "There is no movie in dataset with this " + type + ".")
    else:
        tui.newLine()
        count = 1
        for index, row in df_tmp.iterrows():
            tui.textWithIndent("[Movie #" + str(count) + "] ", 3)
            tui.textWithIndent("\"" + row["Title"] + "\" (" + row["Year"] + "), " + row["Subject"], 6)
            print("      ", end="")
            if isinstance(row["Actor"], str):
                print(prepareActorName2(row["Actor"]), end="")
            if isinstance(row["Actress"], str):
                print(", ", end="")
                print(prepareActorName2(row["Actress"]), end="")
            count += 1
            tui.newLine()

    tui.newLine()
    tui.pressAnyKey()
