def  calculate_experience_points(game_mode, missions_completed, difficulty):
    total = 0
    if game_mode == "campaign":
        if difficulty == "easy":
            total = 50 * missions_completed
        elif difficulty == "normal":
            total = 85 * missions_completed
        elif difficulty == "hard":
            total = 150 * missions_completed
    if game_mode == "multiplayer":
        if difficulty == "easy":
            total = 30 * missions_completed
        elif difficulty == "normal":
            total = 55 * missions_completed
        elif difficulty == "hard":
            total = 95 * missions_completed
    if game_mode == "tutorial":
        if difficulty == "easy":
            total = 15 * missions_completed
        elif difficulty == "normal":
            total = 25 * missions_completed
        elif difficulty == "hard":
            total = 40 * missions_completed
    return total

def calculate_skill_rating(play_hours, baseline_score, current_score):
    expected_score = 1000 + (play_hours * 100)
    score_range = expected_score - baseline_score
    skill_percentage = (current_score - baseline_score) / score_range * 100
    return skill_percentage

def determine_player_rank(skill_percent):
    if skill_percent < 50:
        rank = "Bronze rank"
    elif skill_percent < 60:
        rank = "Silver rank"
    elif skill_percent < 70:
        rank = "Gold rank"
    elif skill_percent < 85:
        rank = "Platinum rank"
    else:
        rank = "Diamond rank"
    return rank

def calculate_reward_coins(xp_points, missions, rank_bonus):
    Base_coins = xp_points * 0.05 + missions * 2
    if rank_bonus == "Bronze rank":
        final_bonus = Base_coins * 0.5
    elif rank_bonus == "Silver rank":
        final_bonus = Base_coins * 1.0
    elif rank_bonus == "Gold rank":
        final_bonus = Base_coins * 1.2
    elif rank_bonus == "Platinum rank":
        final_bonus = Base_coins * 1.5
    elif rank_bonus == "Diamond rank":
        final_bonus = Base_coins * 1.8
    return round(final_bonus, 1)


def needs_practice_mode(gaming_days, total_missions, avg_skill):
    if gaming_days >= 6 and avg_skill < 50:
        return True
    if total_missions < 100 and avg_skill < 60:
        return True
    if gaming_days >= 4 and avg_skill < 40:
        return True
    else:
        return False


def generate_achievement_summary(player_name, game_mode, missions_completed, difficulty, play_hours, baseline_score, current_score, gaming_days):
    value = calculate_experience_points(game_mode, missions_completed, difficulty)
    efficiency = calculate_skill_rating(play_hours, baseline_score, current_score)
    rank = determine_player_rank(efficiency)
    bonus = calculate_reward_coins(value, missions_completed, rank)
    training_needed = needs_practice_mode(gaming_days, missions_completed, efficiency)

    print("GAMING ACHIEVEMENT TRACKER")
    print("========================================")
    print(f"Achievement Summary for: {player_name}")
    print("----------------------------------------")
    print(f"Game Mode: {game_mode}")
    print(f"Missions Completed: {missions_completed}")
    print(f"Difficulty: {difficulty}")
    print(f"Experience Points: {value}")
    print("Skill Analysis:")
    print(f"  Play Hours: {play_hours}, Baseline: {baseline_score}, Current Score: {current_score}")
    print(f"  Skill Rating: {efficiency:.1f}%")
    print(f"  Player Rank: {rank}")
    print(f"Reward Coins: {bonus}")
    print(f"Gaming Days: {gaming_days}")
    print(f"Practice Mode Needed: {'Yes' if training_needed else 'No'}")
    

print("\n")
generate_achievement_summary("Phoenix", "campaign", 45, "hard", 3, 800, 1150, 3)
print("\n")
generate_achievement_summary("Storm", "multiplayer", 60, "normal", 5, 900, 1300, 5)
print("\n")
generate_achievement_summary("Echo", "tutorial", 30, "easy", 8, 850, 950, 7)