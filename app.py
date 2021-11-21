from flask import Flask,render_template,request, template_rendered
app=Flask(__name__,template_folder="template")
import pypyodbc

global connection
connection=''

@app.route("/")
def login():
    return render_template("Login.html")

@app.route("/loginpage",methods=["GET","POST"])
def cred():
    if request.method=="POST":
        uid=request.form.get("uid")
        pwd=request.form.get("pwd")
        uid=str(uid)
        pwd=str(pwd)
        try:
            connection=pypyodbc.connect('Driver={SQL Server};Server=LAPTOP-C1RC1D4R;UID='+uid+';pwd='+pwd+';DATABASE=IPL_DATABASE')
            #print("Connected")
            global cur
            cur=connection.cursor()
            print("Connected")
            return render_template("AdminHome.html")
        except:
            print("Not able to connect")
            return render_template("LoginPage.html")
    return render_template("LoginPage.html")

@app.route("/adminhome")
def adminhome():
    return render_template("AdminHome.html")

@app.route("/home")
def home():
    try:
        connection=pypyodbc.connect('Driver={SQL Server};Server=LAPTOP-C1RC1D4R;UID=sa1;pwd=12345;DATABASE=IPL_DATABASE')
        #print("Connected")
        global cur
        cur=connection.cursor()
        print("Connected")
        return render_template("Home.html")
    except:
        print("Not able to connect")

@app.route("/query",methods=["GET","POST"])
def query():
    data=""
    if request.method=="POST":
        query=request.form.get("query")
        cur.execute(query)
        data=cur.fetchall()
    return render_template("query.html",data=data)

@app.route("/player")
def player():
    return render_template("Player.html")

@app.route("/playerbyname",methods=["GET","POST"])
def PlayerName():
    query="SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME ='Player'"
    cur.execute(query)
    column=cur.fetchall()
    data=""
    if request.method=="POST":
        name=request.form.get("name")
        cur.execute("select * from Player where Name=\'"+name+"\'")
        data=cur.fetchall()
        print(data)
    return render_template("PlayerByName.html",data=[column,data])

@app.route("/playercountry",methods=["GET","POST"])
def SelectPlayer():
    data=""
    if request.method=="POST":
        name=request.form.get("name")
        cur.execute("select * from Player where Nationality=\'"+name+"\'")
        data=cur.fetchall()
    return render_template("PlayerbyCountry.html",data=data)

@app.route("/playerteam",methods=["GET","POST"])
def SelectTeam():
    data=""
    if request.method=="POST":
        name=request.form.get("name")
        cur.execute("select * from Player where Team_Name=\'"+name+"\'")
        data=cur.fetchall()
    return render_template("PlayerbyTeamName.html",data=data)

@app.route("/batsman",methods=["GET","POST"])
def Batsman():
    return render_template("Batsman.html")

@app.route("/batsmanID",methods=["GET","POST"])
def BatsmanID():
    data=""
    if request.method=="POST":
        name=request.form.get("name")
        cur.execute("select * from Batsman where Player_ID=\'"+name+"\'")
        data=cur.fetchall()
    return render_template("BatsmanID.html",data=data)

@app.route("/bowler",methods=["GET","POST"])
def Bowler():
    return render_template("Bowler.html")

@app.route("/bowlerID",methods=["GET","POST"])
def BowlerID():
    data=""
    if request.method=="POST":
        name=request.form.get("name")
        cur.execute("select * from Bowler where Player_ID=\'"+name+"\'")
        data=cur.fetchall()
    return render_template("BowlerID.html",data=data)

@app.route("/coach")
def coach():
    return render_template("Coach.html")

@app.route("/coachname",methods=["GET","POST"])
def CoachName():
    data=""
    if request.method=="POST":
        name=request.form.get("name")
        cur.execute("select * from Coach where Name=\'"+name+"\'")
        data=cur.fetchall()
    return render_template("CoachName.html",data=data)

@app.route("/coachrole",methods=["GET","POST"])
def CoachRole():
    data=""
    if request.method=="POST":
        name=request.form.get("name")
        cur.execute("select * from Coach where Role=\'"+name+"\'")
        data=cur.fetchall()
    return render_template("CoachRole.html",data=data)

@app.route("/coachteam",methods=["GET","POST"])
def CoachTeam():
    data=""
    if request.method=="POST":
        name=request.form.get("name")
        cur.execute("select * from Coach where Team_ID=\'"+name+"\'")
        data=cur.fetchall()
    return render_template("CoachTeam.html",data=data)

@app.route("/match")
def match():
    return render_template("Match.html")

@app.route("/matchid", methods=["GET","POST"])
def matchID():
    data=""
    if request.method=="POST":
        name=request.form.get("name")
        cur.execute("select * from Match where Match_ID=\'"+name+"\'")
        data=cur.fetchall()
    return render_template("MatchID.html",data=data)

@app.route("/matchlocation", methods=["GET","POST"])
def matchlocation():
    data=""
    if request.method=="POST":
        name=request.form.get("name")
        cur.execute("select * from Match where Location=\'"+name+"\'")
        data=cur.fetchall()
    return render_template("MatchLocation.html",data=data)

@app.route("/matchstadiumid", methods=["GET","POST"])
def matchstadiumID():
    data=""
    if request.method=="POST":
        name=request.form.get("name")
        cur.execute("select * from Match where Stadium_ID=\'"+name+"\'")
        data=cur.fetchall()
    return render_template("MatchStadiumID.html",data=data)

@app.route("/matchtossdecision", methods=["GET","POST"])
def matchtossdecision():
    data=""
    if request.method=="POST":
        name=request.form.get("name")
        cur.execute("select * from Match where Toss_Decision=\'"+name+"\'")
        data=cur.fetchall()
    return render_template("MatchTossDecision.html",data=data)

@app.route("/matchtossoutcome", methods=["GET","POST"])
def matchtossoutcome():
    data=""
    if request.method=="POST":
        name=request.form.get("name")
        cur.execute("select * from Match where Toss_Winner=\'"+name+"\'")
        data=cur.fetchall()
    return render_template("MatchTossOutcome.html",data=data)

@app.route("/matchtosswinner", methods=["GET","POST"])
def matchtosswinner():
    data=""
    if request.method=="POST":
        name=request.form.get("name")
        cur.execute("select * from Match where Win_Team_ID=\'"+name+"\'")
        data=cur.fetchall()
    return render_template("MatchTossWinner.html",data=data)

@app.route("/matchwinteamid", methods=["GET","POST"])
def matchwinteamid():
    data=""
    if request.method=="POST":
        name=request.form.get("name")
        cur.execute("select * from Match where Win_Team_ID=\'"+name+"\'")
        data=cur.fetchall()
    return render_template("MatchWinTeamID.html",data=data)

@app.route("/matchwinmethod", methods=["GET","POST"])
def matchwinmethod():
    data=""
    if request.method=="POST":
        name=request.form.get("name")
        cur.execute("select * from Match where Win_Method=\'"+name+"\'")
        data=cur.fetchall()
    return render_template("MatchWinMethod.html",data=data)

@app.route("/insertinto")
def insertinto():
    return render_template("InsertReturn.html")

@app.route("/insertintoplayer", methods=["GET","POST"])
def insertintoplayer():
    data=''
    try:
        if request.method=="POST":
            playerid=request.form.get("playerid")
            name=request.form.get("name")
            dob=request.form.get("dob")
            nationality=request.form.get("nationality")
            teamname=request.form.get("teamname")
            cur.execute("Insert into Player values(\'"+playerid+"\',\'"+name+"\',\'"+dob+"\',\'"+nationality+"\',\'"+teamname+"\');")
            return render_template("Success.html")
    except:
        return render_template("Failure.html")
    return render_template("InsertIntoPlayer.html",data=data)

@app.route("/insertintobatsman", methods=["GET","POST"])
def insertintobatsman():
    data=''
    try:
        if request.method=="POST":
            ballsplayed=request.form.get("ballsplayed")
            scored=request.form.get("scored")
            fours=request.form.get("fours")
            sixes=request.form.get("sixes")
            playerid=request.form.get("playerid")
            cur.execute("Insert into Batsman values("+ballsplayed+","+scored+","+fours+","+sixes+",\'"+playerid+"\');")
            return render_template("Success.html")
    except:
        return render_template("Failure.html")
    return render_template("InsertIntoBatsman.html",data=data)

@app.route("/insertintobowler", methods=["GET","POST"])
def insertintobowler():
    data=''
    try:
        if request.method=="POST":
            runsgiven=request.form.get("runsgiven")
            ballsbowled=request.form.get("ballsbowled")
            wicketstaken=request.form.get("wicketstaken")
            wides=request.form.get("wides")
            dotballs=request.form.get("dotballs")
            noballs=request.form.get("noballs")
            playerid=request.form.get("playerid")
            cur.execute("Insert into Bowler values("+runsgiven+","+ballsbowled+","+wicketstaken+","+wides+","+dotballs+","+noballs+",\'"+playerid+"\');")
            return render_template("Success.html")
    except:
        return render_template("Failure.html")
    return render_template("InsertIntoBowler.html",data=data)

# @app.route("/insertintoplayer", methods=["GET","POST"])
# def insertintobatsman():
#     data=''
#     try:
#         if request.method=="POST":
#             playerid=request.form.get("playerid")
#             name=request.form.get("name")
#             dob=request.form.get("dob")
#             nationality=request.form.get("nationality")
#             teamname=request.form.get("teamname")
#             cur.execute("Insert into Player values(\'"+playerid+"\',\'"+name+"\',\'"+dob+"\',\'"+nationality+"\',\'"+teamname+"\');")
#             return render_template("Success.html")
#     except:
#         return render_template("Failure.html")
#     return render_template("insertIntoPlayer.html",data=data)

# @app.route("/insertintoplayer", methods=["GET","POST"])
# def insertintobatsman():
#     data=''
#     try:
#         if request.method=="POST":
#             playerid=request.form.get("playerid")
#             name=request.form.get("name")
#             dob=request.form.get("dob")
#             nationality=request.form.get("nationality")
#             teamname=request.form.get("teamname")
#             cur.execute("Insert into Player values(\'"+playerid+"\',\'"+name+"\',\'"+dob+"\',\'"+nationality+"\',\'"+teamname+"\');")
#             return render_template("Success.html")
    # except:
    #     return render_template("Failure.html")
    # return render_template("insertIntoPlayer.html",data=data)