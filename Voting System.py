nominee_1 = input("Enter the nominee 1 name: ")
nominee_2 = input("Enter the nominee 2 name: ")

nom_1_votes=0
nom_2_votes=0

voter_id = [1,2,3,4,5,6,7,8,9,10]

num_of_voter=len(voter_id)

while True:
    if voter_id==[]:
        print("Voting session is over")
        if nom_1_votes>nom_2_votes:
            percent=(nom_1_votes/num_of_voter)*100
            print(nominee_1, "has won", "with", percent, "% of the votes")
            break

        elif nom_2_votes>nom_1_votes:
            percent=(nom_2_votes/num_of_voter)*100
            print(nominee_2, "has won", "with", percent, "% of the votes")
            break

    else:
        voter=int(input("Enter your voter id no: "))
        if voter in voter_id:
            print("You are a registered voter")
            voter_id.remove(voter)
            vote = int(input("Enter your vote 1 or 2: "))
            if vote==1:
                nom_1_votes+=1
                print("Thank you for casting your vote")

            elif vote==2:
                nom_2_votes+= 1
                print("Thank you for casting your vote")
        else:
            print("You are not an assigned voter here or you have already voted")