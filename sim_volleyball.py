import random

def readParameters() -> tuple[int, float, float]:
    n = int(input("How many games should we simulate? "))
    pA = float(input('What is the probability that team A wins a serve? '))
    pB = float(input('What is the probability that team B wins a serve? '))
    return n, pA, pB

def gameOver(ptsA: int, ptsB: int, win_pts: int) -> bool:
    """Takes the number of points for each team and
    the number of points needed to win.  Returns a boolean
    telling whether the game is over."""
    finished: bool = True
    if ptsA < win_pts and ptsB < win_pts:
        finished = False
    elif abs(ptsA - ptsB) < 2:
        finished = False
    return finished

def simulateRally(pA: float, pB: float, a_serves: bool) -> bool:
    '''Simulate a rally between teams A and B, with
    probabilities pA and pB, respectively, of winning
    a serve.  Boolean a_serves indicates whether 
    team A is serving.  Return a boolean indicating whether 
    team A won the rally.'''
    a_wins: bool = False    # Default: Team B wins the point
    rand: float = random.random()
    #print(rand)
    if a_serves:
        if rand < pA:       # Team A won the point
            a_wins = True
    else:
        if not rand < pB:  # Team B did *not* win the point
            a_wins = True  #    so team A did.
    return a_wins

def simulate1Game(pA: float, pB: float, sideout_scoring: bool) -> bool:
    '''Simulate a volleyball game between teams A and B,
    where team A has probability pA of winning a serve
    and team B has probability pB of winning a serve.
    The SIDEOUT parameter tells whether to use sideout
    scoring, in place of rally scoring. Returns a boolean
    stating whether team A won.'''
    ptsA: int = 0
    ptsB: int = 0
    a_serving: bool = True
    win_pts = 25
    if sideout_scoring:
        win_pts = 15

    while not gameOver(ptsA, ptsB, win_pts):
        a_point: bool = simulateRally(pA, pB, a_serving)
        # if not sideout_scoring:
        #     print(ptsA, ptsB, a_serving, a_point)
        if sideout_scoring:
            if a_serving:
                if a_point:
                    ptsA = ptsA + 1
                else: # Team A lost the serve
                    a_serving = False
            else: # Team B is serving
                if a_point: # Team B lost the serve
                    a_serving = True
                else:
                    ptsB = ptsB + 1
        else: # Rally scoring
            if a_point:
                ptsA = ptsA + 1
                if not a_serving:
                    a_serving = True
            else:
                ptsB = ptsB + 1
                if a_serving:
                    a_serving = False
    # Game is over, so ptsA != ptsB
    return ptsA > ptsB

def simulateNGames(n: int, pA: float, pB: float, sideout: bool = False) -> float:
    """Simulate N games of volleyball between two teams
    A and B, with probabilities pA and pB, respectively,
    that each of the teams will win a serve.  The optional
    SIDEOUT parameter (default is False) specifies whether
    to use the older side-out scoring method or the usual
    rally method.  Returns the win percentage wA for team A.
    (The win percentage for team B, wB, is just (1 - wA).)"""
    winsA: int = 0
    winsB: int = 0
    for i in range(n):  # type: ignore
        a_won = simulate1Game(pA, pB, sideout)
        if a_won:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
        # if sideout:
        #     print(winsA, winsB, a_won)
    return winsA / n

def main(args: list[str]) -> int:
    n, pA, pB = readParameters()
    # Rally scoring
    a_wins: float = simulateNGames(n, pA, pB)
    print(f"Team A's win percentage using rally scoring was {a_wins:%}.")
    # Side-out scoring
    a_wins = simulateNGames(n, pA, pB, True)
    print(f"Team A's win percentage using side-out scoring was {a_wins:%}.")

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
