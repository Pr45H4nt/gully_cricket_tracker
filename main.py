import os
from time import sleep
def clear_terminal():
    """
    Clear the terminal/console screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print("CODED BY PRASH \n")


class Batsman:
    def __init__(self, name) -> None:
        self.name = name 
        self.runs = 0
        self.balls = 0
    
    def add_run(self,run, ball = 1):
        self.runs += run
        self.balls += ball
    
    def strike_rate(self):
        if self.balls != 0:
            return ((self.runs)/(self.balls))*100
        return 0
    
    def status(self):
        return f"{self.name}: {self.runs}({self.balls}) \t strike rate : {self.strike_rate()}"


class Bowler:
    def __init__(self, name) -> None:
        self.name = name
        self.balls = 0
        self.runs = 0
        self.wicket = 0
        self.over = 0

    def get_economy(self):
        try:
            return (self.runs /self.over)
        except:
            return 0    
    def Display_overs(self):
        a = self.balls//6
        return f"{a}.{abs(a*6-self.balls)}"  
     
    def add_run(self, run , ball = 1):
        self.runs += run
        self.balls += ball
        self.over = self.balls /6

    def status(self):
        return f"{self.name}: {self.wicket}-{self.runs}   overs = {self.Display_overs()} \t Economy: {self.get_economy()}"

class game:
    def __init__(self,  n_batsmen, n2_batsmen ,n_bowler , total_overs , target = None) -> None:
        self.score = 0
        self.target = target
        self.current_over = []
        self.bowler = Bowler(n_bowler)
        self.striker = Batsman(n_batsmen)
        self.runner = Batsman(n2_batsmen)
        self.total_balls = 0
        self.total_overs = total_overs
        self.wickets = 0
        self.batsmanstatus = []
        self.bowlerstatus = []
        
    def ball(self, run, b=1):
        if b == 1:
            self.total_balls += 1
            if type(run) == int:
                self.striker.add_run(run)
                self.current_over.append(run)
                self.bowler.add_run(run)
                self.score += run
                if run < 4:
                    if run%2 != 0:
                        self.striker , self.runner = self.runner , self.striker
        else:
            match run:
                case 'WD':
                    self.score += 1
                    self.current_over.append(run)
                    self.bowler.add_run(run= 1, ball= 0)

                case 'NB':
                    self.score += 1
                    self.current_over.append(run)
                    self.bowler.add_run(run= 1, ball= 0)

    def get_wicket(self, new_name, prompt = 1):
        self.total_balls += 1
        self.current_over.append('W')
        self.batsmanstatus.append(self.striker.status() + f"(Bowl by {self.bowler.name})")  
        self.wickets += 1
        self.bowler.wicket += 1
        if  prompt == 1:
            self.striker = Batsman(new_name)
        else:
            self.runner = Batsman(new_name)   

    def isover(self):
        if self.total_balls %6 == 0:
            self.current_over.clear()
            return True
        return False

    def changeBowler(self,choice=None, name=None):
        self.bowlerstatus.append(self.bowler)
        if name is not None:
            self.bowler = Bowler(name)
        else:
            self.bowler = self.bowlerstatus[choice-1]


    def overs(self):
        a = self.total_balls//6
        return f"{a}.{abs(a*6-self.total_balls)}"
        
        
    def current_rr(self):
        try:
            return (self.score/self.total_balls)*6
        except:
            return 0
    
    def required_rr(self):
        a= (self.total_overs-(self.total_balls/6))
        if a == 0:
            return 0
        if self.target != None:
            return (self.target - self.score)/a
    
    def game_status(self):
        if self.target == None:
            return f"""
                First Batting Team - {self.score}-{self.wickets}
                -- {self.striker.status()} 
                   {self.runner.status()} 
                   Current RunRate - {self.current_rr()}
                   Current Over - {self.overs()}
                   Bowler = {self.bowler.status()}
                   This Over = {self.current_over}
            """
        return f"""
                Chasing Team - {self.score}-{self.wickets}
                -- {self.striker.status()} 
                   {self.runner.status()} 
                   Current RunRate - {self.current_rr()}
                   Required RunRate - {self.required_rr()}
                   Current Over - {self.overs()}
                   Bowler = {self.bowler.status()}
                   This Over = {self.current_over}
                   Target = {self.target}
            """



def main():
    choices = ['1','2','3','4','6',"0",'W', 'WD', 'NB']
    x = input('First Batsmen Name: ')
    y = input('Second Batsmen Name: ')
    z = input('Bowlers name: ')
    w = int(input('Total Overs to be Played: '))
    avw = int(input("how many wickets are there?: "))
    g = game(x,y,z,w)
    clear_terminal()
    while g.wickets < avw and g.total_balls < (g.total_overs*6):
        while True:
            state = input("State: ").upper()
            clear_terminal()
            if state in choices:
                break
            else:
                print("Wrong input")
        if state != 'W':
            try:
                g.ball(int(state))
            except:
                g.ball(state, b=0)
        else:
            while True:
                p = input("who was out?(1/2) : ")
                if p != '1' and p != '2':
                    print('wrong input')
                else:
                    break
            n = input("New batsmen : ")
            g.get_wicket(n, int(p))
        print(g.game_status())
        if g.isover():
            for i in range(len(g.bowlerstatus)):
                print(i+1 , g.bowlerstatus[i].status())
            newb = input('New Bowlers Name or choose from above : ')
            try:
                newb = int(newb)
                g.changeBowler(choice=newb)
            except:
                g.changeBowler(name=newb)
    else:
        clear_terminal()
        print("Game Finished for First Team")   
        g.batsmanstatus.append(g.striker.status())
        g.batsmanstatus.append(g.runner.status())
        clear_terminal()
        for i in range(len(g.batsmanstatus)):
            print(i+1 , g.batsmanstatus[i]) 
        input()
        clear_terminal()
    print("CHASING TEAM")
    x = input('First Batsmen Name: ')
    y = input('Second Batsmen Name: ')
    z = input('Bowlers name: ')
    g2 = game(x,y,z,w,g.score+1)
    clear_terminal()
    while g2.wickets < avw and g2.total_balls < (g2.total_overs*6) and g2.score < g.score:
        while True:
            state = input("State: ").upper()
            clear_terminal()
            if state in choices:
                break
            else:
                print("Wrong input")
        if state != 'W':
            try:
                g2.ball(int(state))
            except:
                g2.ball(state, b=0)
        else:
            while True:
                if p != '1' and p != '2':
                    p = input("who was out?(1/2) : ").strip()
                    print('wrong input')
                else:
                    break
            n = input("New batsmen : ")
            g2.get_wicket(n, int(p))
        print(g2.game_status())
        if g2.isover():
            clear_terminal()
            for i in range(len(g2.bowlerstatus)):
                print(i+1 , g2.bowlerstatus[i].status())
            newb = input('New Bowlers Name or choose from above : ')
            try:
                newb = int(newb)
                g2.changeBowler(choice=newb)
            except:
                g2.changeBowler(name=newb)
    else:
        g2.batsmanstatus.append(g2.striker.status())
        g2.batsmanstatus.append(g2.runner.status())
        clear_terminal()
        for i in range(len(g2.batsmanstatus)):
            print(i+1 , g2.batsmanstatus[i]) 
        if g.score > g2.score:
            print("First Batting Team Wins".upper())
        elif g.score == g2.score:
            print('Game Drawed')
        else:
            print("Second Batting Team wins".upper())     
    clear_terminal()
    print("First Batting Score Card".upper())
    print(g.score)
    print("________________________")
    for i in range(len(g.batsmanstatus)):
        print(i+1 , g.batsmanstatus[i]) 
    print("________________________")
    for i in range(len(g.bowlerstatus)):
        print(i+1 , g.bowlerstatus[i].status())
    print("\n \n \n \n")
    print("chasing team Score Card".upper())
    print(g2.score)
    print("________________________")
    for i in range(len(g2.batsmanstatus)):
        print(i+1 , g2.batsmanstatus[i]) 
    print("________________________")
    for i in range(len(g2.bowlerstatus)):
        print(i+1 , g2.bowlerstatus[i].status()) 
    
main()