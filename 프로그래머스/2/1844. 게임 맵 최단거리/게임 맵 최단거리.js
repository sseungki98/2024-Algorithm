function solution(maps) {
    var answer = 0;
    const dx = [0, 0, 1, -1];
    const dy = [1, -1, 0, 0];
    const visited = new Array(maps.length);
    const move = new Array(maps.length);
    for(let i=0; i<maps.length; i++) {
        visited[i] = new Array(maps[i].length).fill(false);
        move[i] = new Array(maps[i].length).fill(0);
    }
    
    function bfs(x, y) {
        const stack = [];
        stack.push([x, y]);
        visited[x][y] = true;
        
        while (stack.length > 0){
            const shifted = stack.shift();
            const _x = shifted[0];
            const _y = shifted[1];
            for(let i=0; i<4; i++) {
                ddx = _x + dx[i];
                ddy = _y + dy[i];
                if(ddx >= 0 && ddx < maps.length && ddy >= 0 && ddy < maps[0].length) {
                    if (maps[ddx][ddy] === 1 && visited[ddx][ddy] === false) {
                        move[ddx][ddy] = move[_x][_y] + 1;
                        visited[ddx][ddy] = true;
                        stack.push([ddx, ddy]);
                    }
                }
            }
        }
    }
    bfs(0, 0);
    if(move[maps.length-1][maps[0].length-1] === 0) {
        return -1
    } else {
        return move[maps.length-1][maps[0].length-1]+1;   
    }
}