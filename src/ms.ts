// You are given an m x n grid where each cell can have one of three values:
 
// 0 representing an empty cell,
// 1 representing a fresh orange, or
// 2 representing a rotten orange.
// Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
 
// Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
 
 
// Example 1:
// Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
// [2,1,1]
// [1,1,0]
// [0,1,1]
// Output: 4

async function getRottenTime(grid: number[][], time: number = 0): Promise<number>{
    const hasFresh = grid.some(row => row.some(fruit => fruit === 1));
    if(!hasFresh){
        return time;
    } else {
        let isolatedRotten: Boolean[] = []
        const currGrid = grid.map(row => [...row]);
        for (let i = 0; i < grid.length; i++){
            const row = grid[i]
            for (let j = 0; j < row.length; j++){
                const up = (grid[i-1]?.[j]) ?? 0;
                const down = (grid[i+1]?.[j]) ?? 0;
                const left = row[j-1] ?? 0;
                const right = row[j+1] ?? 0;
                const isFresh = row[j] === 1
                const isRotten = row[j] === 2
                
                if (isRotten){
                    const isIsolated = (up != 1 && down != 1 && left != 1 && right != 1)
                    isolatedRotten.push(isIsolated)
                }
                if(isFresh){
                    if (left === 2 || right === 2 || up === 2 || down === 2) {
                        currGrid[i][j] = 2
                    }
                }
            }
        }
        if (isolatedRotten.every(value => value === true)) {
            return -1;
        }
        time++
        return getRottenTime(currGrid, time)
    } 
}

(async (): Promise<void> => {
    const tests = ([
        // [2,1,1]
        // [1,1,0]
        // [0,1,1]
        [[2,1,1],[1,1,0],[0,1,1]], // 4

        // [2,2,1]
        // [1,1,0]
        // [0,1,1]        
        [[2,2,1],[1,1,0],[0,1,1]], // 3

        // [0,0,0]
        // [0,0,0]
        // [0,0,1]
        [[0,0,0],[0,0,0],[0,0,1]], // -1

        // [2,0,1]
        // [0,1,1]
        // [1,1,1]
        [[2,0,1],[0,1,1],[1,1,1]], // -1

        // [1,1,1,1]
        // [2,0,0,1]
        // [0,2,0,1]
        // [0,0,0,0]
        [[1,1,1,1],[2,0,0,1],[0,2,0,1],[0,0,0,0]], // 6

        [
            [1, 1, 1, 1, 1, 1, 1, 1],
            [2, 0, 0, 1, 1, 0, 1, 1],
            [0, 2, 0, 1, 0, 1, 0, 1],
            [0, 0, 0, 0, 1, 1, 1, 1],
            [1, 2, 1, 0, 0, 0, 1, 1],
            [2, 1, 0, 2, 1, 0, 0, 1],
            [1, 0, 2, 1, 2, 0, 2, 0],
            [0, 1, 1, 1, 1, 2, 0, 0] // 14
        ]
    ])
    const promises = tests.map(test => getRottenTime(test));

    const results = await Promise.all(promises);

    results.forEach((result, index) => {
        console.log(`Test ${index + 1}: Time = ${result}`);
    });
})();
