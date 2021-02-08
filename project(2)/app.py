import copy
import sys
import constants

players_copy = copy.deepcopy(constants.PLAYERS)
teams_copy = copy.deepcopy(constants.TEAMS)

bandits = []
panthers = []
warriors = []
experienced_players = []
inexperienced_players = []

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

#display teams name as string, players names as a string, num players, num of exp and inexp players, avg height of team, guardians 
def display_stats():
    Team_A = 'Warriors'
    Team_B = 'Bandits'
    Team_C = 'Panthers'
    if user_choice.lower() == 'a':
        team_choice = input("\nEnter (A) for Warriors, (B) for Bandits or (C) for Panthers:  ")
        if team_choice.lower() == 'a':
            print(f"\nTeam: {Team_A}\n")
            show_stats()
            each_team(warriors)aa
            show_stats_again()
        elif team_choice.lower() == 'b':
            print(f"\nTeam: {Team_B}\n") 
            show_stats()
            each_team(bandits)
            show_stats_again()
        elif team_choice.lower() == 'c':
            print(f"\nTeam: {Team_C}:\n")
            show_stats()
            each_team(panthers)
            show_stats_again()
    elif user_choice.lower == 'b':
        print("\nThanks for visiting the Basketball Team Stats Tool! Have a great day!\n")
        sys.exit()
    
    
def show_stats_again():
    user_input = input("\nWould you like to see the stats for another team? Enter (Y) for Yes or (N) to exit:  ")
    if user_input.lower() == 'y':
        display_stats()
    else:
        print("\nOk, have a great day!\n")
        sys.exit()
        
def show_stats():
    print("-" * 5, "Stats:", "-" * 5,"\n")
    print(f"Number of players on team: {int(len(players_copy) / len(teams_copy))}")
    print(f"Number of experienced players: {int(len(experienced_players) / len(teams_copy))}")
    print(f"Number of inexperienced players: {int(len(inexperienced_players) / len(teams_copy))}") 
          
def each_team(team_name):
    names = []
    heights = []
    guardians_list_within_list = []
    guardians_list = []
    for player in team_name:
        player_name = player['name']
        names.append(player_name)
        player_height = player['height']
        heights.append(player_height)
        player_guardians = player['guardians']
        guardians_list_within_list.append(player_guardians)
    for guardians in guardians_list_within_list:
        for guardian in guardians:
            guardians_list.append(guardian)
    avg_height = round(sum(heights) / len(team_name), 1)
    print("Average Height:", avg_height, "\n")
    print("Players:", ", ".join(names))
    print("Guardians:", ", ".join(guardians_list))
    
    
            
if __name__ == '__main__':
    
    print("""
Welcome to Basketball Teams Stat Tool!
      
----------MENU----------
    """)
    
    user_choice = input("Enter (A) to see team stats or (B) to quit:  ")
    clean_data()
    balance_teams()
    display_stats()
    

    
    

    

    
        


    

