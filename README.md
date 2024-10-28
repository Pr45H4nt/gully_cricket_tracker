
# Gully Cricket Tracker

## Project Overview

The Gully Cricket Tracker is a terminal-based scoring tool specifically designed for informal cricket games (often known as "gully cricket"). This script allows users to track scores, wickets, overs, and player statistics throughout the game, with simplified rules tailored for casual gameplay. While there is a known bug involving missed bowler overs, it does not impact the overall functionality of the program.

## Features

1. **Player Management**:
   - Tracks the performance of batsmen, including runs, balls faced, and strike rate.
   - Tracks the performance of bowlers, including runs conceded, wickets taken, and economy rate.

2. **Match Progression**:
   - Displays real-time updates on current scores, wickets, and overs.
   - Allows users to input runs, wides, no-balls, and wickets for each ball bowled.
   - Tracks the game status for both the first batting team and the chasing team.

3. **Flexible Commands**:
   - Change bowlers and manage players during overs and wickets.
   - Built-in terminal-based interface for a classic, minimalistic feel.

## Usage Instructions

### Initial Setup
1. **Clone the repository** and navigate to the project directory:

   ```bash
   git clone <repository-link>
   cd gully-cricket-tracker
   ```

2. **Run the script**:

   ```bash
   python gully_cricket_tracker.py
   ```

### In-Game Commands

1. **Start the Game**: Follow the prompts to input initial players' names, total overs, and available wickets.

2. **Enter Ball Outcomes**:
   - **Enter runs** (e.g., `1`, `2`, `4`, `6`, `0`) for each ball bowled.
   - **Special Inputs**:
     - `W` - Wicket
     - `WD` - Wide Ball (adds 1 run)
     - `NB` - No Ball (adds 1 run)
   - **New Bowler**: After each over, you can choose a new bowler by name or by selecting from previous bowlers.

3. **Track Progress**: The program displays the current score, overs, and individual player statistics as the game progresses.

4. **End of Innings**: After the first team completes its innings, input the details for the chasing team. The program will continue tracking scores until either team wins or the game ends in a draw.

## Known Bug

There is a minor bug involving bowler overs being occasionally missed, but this does not affect the overall scoring functionality or the final results.

## Future Enhancements

- **Bug Fix**: Resolve the missed bowler overs tracking issue.
- **Graphical Interface**: Implement a GUI for easier input and tracking.
- **Enhanced Statistics**: Provide more detailed stats, such as average, economy rate trends, and graphical summaries.

## Author

Prashant Paneru
