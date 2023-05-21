#question 2
#set a class named triathlon
class triathlon(object):
    #recording should be a object to restore the results, and Here i choose the dictionary
    def __init__(self,recording) :
        self.recording=recording
    #set a method to allow user input the first name    
    def firstname(self,firstname):
        self.recording["first name"]=firstname
      #set a method to allow user input the last name       
    def lastname(self,lastname):
        self.recording["last name"]=lastname
    # to judge if the sum of the total time can be calculated
    def judge_sum(self):
        if self.recording["swim time"]!="no data" and self.recording["run time"]!="no data" and self.recording["swim time"]!="no data":
            self.recording["total time"]=self.recording["swim time"]+self.recording["run time"]+self.recording["cycle time"]
    #set a method to allow user input the swim time
    def swim_minute(self,swim):
        self.recording["swim time"]=swim
        #judge_sum method to calculate the total time if it can be calculted
        self.judge_sum()
       
    def run_minute(self,run):
        self.recording["run time"]=run
        self.judge_sum()
        
    def cycle_minute(self,cycle):
        self.recording["cycle time"]=cycle
        self.judge_sum()
    #print the result
    def get(self):
        return self.recording
#test
#input a dictionary as recording
records={"first name":"no data","last name":"no data","swim time":"no data","run time":"no data","cycle time":"no data","total time":"no data"}
record=triathlon(records)
record.firstname("a")
record.lastname("b")
record.swim_minute(16)
record.cycle_minute(20)
record.run_minute(40)
record.get()
