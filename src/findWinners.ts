function findWinners(matches: number[][]): number[][] {
    let playerStats = new Map();
    for (const match of matches){
        for (let i = 0; i < 2; i++){            
            playerStats.set(match[i], (playerStats.get(match[i]) || 0) + i)
        };
    };
    let winners = []
    let losers = []
    for (let [key, value] of playerStats) {
        if (value === 0){
            winners.push(key)
        }
        else if (value === 1){
            losers.push(key)
        }
    }
    
    // Sort winners and losers in ascending order
    winners.sort((a, b) => a - b);
    losers.sort((a, b) => a - b);
    
    return [winners,losers]
};