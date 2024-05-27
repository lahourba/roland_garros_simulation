import pandas as pd
import numpy as np

# Load the provided Excel file to examine its structure
file_path = 'rg_2024.xlsx'
data = pd.read_excel(file_path)

# Assuming the data structure and the player categories

# Categorize players into their respective groups
def categorize_player(seed):
    if pd.isna(seed):
        return 'Non-Seeded'
    elif seed in ['Q', 'L', 'W']:
        return 'Qualifier'
    else:
        seed = int(seed)
        if seed <= 10:
            return 'Top 10'
        elif seed <= 20:
            return 'Top 20'
        elif seed <= 30:
            return 'Top 30'
        else:
            return 'Non-Seeded'

data['Category'] = data['Tête de Série'].apply(categorize_player)

# Reassemble and define all functions and variables together for proper scope access

def simulate_french_victory(n_simulations=10000):
    # Define winning probabilities matrix
    win_probs = {
        'Top 10': {'Top 10': 0.5, 'Top 20': 0.6, 'Top 30': 0.65, 'Non-Seeded': 0.7, 'Qualifier': 0.8},
        'Top 20': {'Top 10': 0.4, 'Top 20': 0.5, 'Top 30': 0.55, 'Non-Seeded': 0.6, 'Qualifier': 0.7},
        'Top 30': {'Top 10': 0.35, 'Top 20': 0.45, 'Top 30': 0.5, 'Non-Seeded': 0.55, 'Qualifier': 0.65},
        'Non-Seeded': {'Top 10': 0.2, 'Top 20': 0.3, 'Top 30': 0.4, 'Non-Seeded': 0.5, 'Qualifier': 0.65},
        'Qualifier': {'Top 10': 0.05, 'Top 20': 0.1, 'Top 30': 0.2, 'Non-Seeded': 0.4, 'Qualifier': 0.5}
    }

    # Simulate a single match between two players
    def simulate_match(player1, player2):
        cat1 = player1['Category']
        cat2 = player2['Category']
        win_prob = win_probs[cat1][cat2]
        return np.random.rand() < win_prob  # True if player1 wins, False otherwise

    # Simulate the tournament
    def simulate_tournament(players):
        # Randomly shuffle players for this simulation
        np.random.shuffle(players)
        while len(players) > 1:
            next_round = []
            for i in range(0, len(players), 2):
                if i + 1 < len(players):
                    player1 = players[i]
                    player2 = players[i + 1]
                    winner = player1 if simulate_match(player1, player2) else player2
                    next_round.append(winner)
            players = next_round
        return players[0]  # The champion

    # Count how many times a French player wins
    french_win_count = 0
    players_list = data.to_dict('records')
    for _ in range(n_simulations):
        champion = simulate_tournament(players_list)
        if champion['Nationalité'] == 'FRA':
            french_win_count += 1
    return french_win_count / n_simulations

# Re-run the simulation with all functions properly defined
french_win_probability = simulate_french_victory()
print(f"There is a {french_win_probability*100}% probability to see a French tennis player winning Roland Garros this year")