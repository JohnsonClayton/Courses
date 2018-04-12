class BossesState:
    def writeMood(context, shiftrequests):
        print("")
class StateHappy():
    def writeMood(self, context, shiftrequests):
        callins = context.requests(shiftrequests)
        if (callins > 0):
            print("Manager is Concerned because " + str(callins) + " employee has called out")
            context.setState(StateStressed())
        else:
            print("Manager is Happy because all shifts are covered!")

class StateStressed(BossesState):
    def writeMood(self, context, shiftrequests):
        callins = context.requests(shiftrequests)
        if (callins == 2):
            print("Manager is Getting Irritated because " + str(callins) + " employees have called out!")
        if (callins == 1):
            print("Manager is Feeling Better because only " + str(callins) + " shift needs covered now!")
        if (callins > 2):
            context.setState(StatePissed())
            print("Manager is Full on Pissed because " + str(callins) + " employees have called out!")
        if (callins < 1): 
            context.setState(StateHappy());
            print("Manager is Happy because all shifts are covered")
class StatePissed(BossesState):
    def writeMood(self, context, shiftrequests):
        callins = context.requests(shiftrequests)
        if(callins < 3) :
            context.setState(StateStressed())
            print("Manager has Cooled Down because only " + str(callins) + " shifts need covered!")
        else:
            print("Manager is Full on Pissed because " + str(callins) + " employees have called out")
class StateContext:
    def __init__(self):
        self.myState = StateHappy()
        self.numrequests = 0;
    def writeMood(self, shiftrequests):
        self.myState.writeMood(self, shiftrequests)
    def setState(self, newState):
        self.myState = newState
    def requests(self, request):
        if (request == "Can't Work"):
            self.numrequests = self.numrequests + 1
        elif (request == "Can Work"):
            self.numrequests = self.numrequests - 1
            if (self.numrequests < 0):
                self.numrequests = 0
        else:
            self.numrequests = 0
        return self.numrequests
class StateDesignPattern:
    def __init__(self):
        sc = StateContext()
        sc.writeMood("No Changes")
        sc.writeMood("Can't Work")
        sc.writeMood("Can Work")
        sc.writeMood("Can't Work")
        sc.writeMood("Can't Work")
        sc.writeMood("Can't Work")
        sc.writeMood("Can't Work")
        sc.writeMood("Can Work")
        sc.writeMood("Can Work")
        sc.writeMood("Can Work")
        sc.writeMood("Can Work")
if __name__ == '__main__':
    sc = StateDesignPattern()
