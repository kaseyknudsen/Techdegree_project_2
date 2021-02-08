import copy
import sys
import constants

#create copies of the lists using deep copy
players_copy = copy.deepcopy(constants.PLAYERS)
teams_copy = copy.deepcopy(constants.TEAMS)

#create empty lists for each team to append
bandits = []
panthers = []
warriors = []

#create empty lists of experienced and inexperienced players 
experienced_players = []
inexperienced_players = []

#create clean data function to turn player_height into an integer; eliminate the 'and' in player guardians; Turn player experience into True or False boolean value; append the experienced and inexperienced players lists
def clean_data():
    for player in players_copy:
        player_height = player['height'].split()
        player['height'] = int(player_height[0])
        player['guardians'] = player['guardians'].split(" and " )
        if player['experience'] == 'YES':
            player['experience'] = True
            experienced_players.append(player)
        elif player['experience'] == 'NO':
            player['experience'] = False
            inexperienced_players.append(player)
    return experienced_players, inexperienced_players

#create balance_teams function to balance each team equally with experienced and inexperienced players
def balance_teams():
    num_exp_players_per_team = int(len(experienced_players) / len(teams_copy))
    num_inexp_players_per_team = int(len(inexperienced_players) / len(teams_copy))
    total_num_players_per_team = num_exp_players_per_team + num_inexp_players_per_team
    for player in experienced_players:
        if len(bandits) < num_exp_players_per_team:
            bandits.append(player)
        elif len(panthers) < num_exp_players_per_team:
            panthers.append(player)
        elif len(warriors) < num_exp_players_per_team:
            warriors.append(player)
    for player in inexperienced_players:
        if len(bandits) < total_num_players_per_team:
            bandits.append(player)
        elif len(panthers) < total_num_players_per_team:
            panthers.append(player)
        elif len(warriors) < total_num_players_per_team:
            warriors.append(player)
    return bandits, panthers, warriors

#display team's name as string; display total number of players and amount of experienced and inexperienced players; display average height; display players names as a comma separated string; display guardians as a comma separated string
def display_stats():
    Team_A = 'Warriors'
    Team_B = 'Bandits'
    Team_C = 'Panthers'
    if user_choice.lower() == 'a':
        while True:
            try:
                team_choice = input("\nEnter (A) for Warriors, (B) for Bandits or (C) for Panthers:  ")
                if team_choice.lower() != 'a' and team_choice.lower() != 'b' and team_choice.lower() != 'c':
                    raise ValueError()
            except ValueError:
                print("\n***Uh oh, that's not a valid entry. Please try again.***")
            else:
                if team_choice.lower() == 'a':
                    print(f"\nTeam: {Team_A}\n")
                    show_stats()
                    each_team(warriors)
                    show_stats_again()
                    break
                elif team_choice.lower() == 'b':
                    print(f"\nTeam: {Team_B}\n") 
                    show_stats()
                    each_team(bandits)
                    show_stats_again()
                    break
                elif team_choice.lower() == 'c':
                    print(f"\nTeam: {Team_C}:\n")
                    show_stats()
                    each_team(panthers)
                    show_stats_again()
                    break
    elif user_choice.lower == 'b':
        print("\nThanks for visiting the Basketball Team Stats Tool! Have a great day!\n")
        sys.exit()
    
#function to call inside of display_stats to ask user if they'd like to see the stats for another team or quit    
def show_stats_again():
    user_input = input("\nWould you like to see the stats for another team? Enter (Y) for Yes or (N) to exit:  ")
    if user_input.lower() == 'y':
        display_stats()
    else:
        print("\nOk, have a great day!\n")
        sys.exit()

#function to call inside of display_stats that lists the number of players and the number of experienced and inexperienced players        
def show_stats():
    print("-" * 5, "Stats", "-" * 5,"\n")
    print(f"Number of players on team: {int(len(players_copy) / len(teams_copy))}")
    print(f"Number of experienced players: {int(len(experienced_players) / len(teams_copy))}")
    print(f"Number of inexperienced players: {int(len(inexperienced_players) / len(teams_copy))}")
    
#function to call inside of display_stats that lists the players as a string as well as their average height and guardians          
def each_team(team_name):
    names = [player['name'] for player in team_name]
    heights = [player['height'] for player in team_name]
    guardians_list = []
    for player in team_name:
        player_guardians = player['guardians']
        guardians_list.extend(player_guardians)
    avg_height = round(sum(heights) / len(team_name), 1)
    print("Average Height:", avg_height, "\n")
    print("Players:", ", ".join(names))
    print("Guardians:", ", ".join(guardians_list))
    
    
if __name__ == '__main__':
    
    print("""
Welcome to Basketball Teams Stat Tool!
      
----------MENU----------
    """)
        
    while True:
        try:
            user_choice = input("Enter (A) to see team stats or (B) to quit:  ")
            if user_choice.upper() != 'A' and user_choice.upper() != 'B':
                raise ValueError()
        except ValueError:
            print("\n***Uh oh, that's not a valid value. Please try again.***\n")
        else:
            clean_data()
            balance_teams()
            display_stats()
            break
                
            
                
    

    
    

    

    
        


    

