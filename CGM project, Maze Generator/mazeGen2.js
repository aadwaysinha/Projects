console.log('MaxGen2 is connected');

var len = 40;
var gridSide = 400;
var rows = gridSide/len;
var cols = rows;
var grid = [];
var current;
var next = undefined;
var firstLoop = true;

function setup(){
    createCanvas(gridSide, gridSide);
    background(51);
    frameRate(5);
    var pos = 0;
    for(let x=0; x<gridSide; x+=len)
    {
        for(let y=0; y<gridSide; y+=len)
        {
            let c = new Cell(x, y);
            grid.push(c);
            c.indexxx = pos++; 
            //c.show();
            //console.log(grid.length)
        }
    }

    current = grid[0];
    current.visited = true;
}

function index(i, j)
{
    return i*cols + j;
}

function isValidIndeX(i, j, indexx)
{
    console.log(i + "  " + j);
    return ((i >= 0 && j >= 0) && (i < cols && j < cols));
}

class Cell{
    constructor(y, x){
        this.j = Math.floor(x/len);
        this.i = Math.floor(y/len);
        this.visited = false;
        this.indexxx = index(this.i, this.j);

        //Top right bottom left
        this.walls = [true, true, true, true];

        this.show = function(){
            stroke(0);
            if(this.walls[0]){
                // noStroke();
                line(x, y, x+len, y);
            }
            if(this.walls[1]){
                // noStroke();
                line(x+len, y, x+len, y+len);
            }
            if(this.walls[2]){
                // noStroke();
                line(x+len, y+len, x, y+len);
            }
            if(this.walls[3]){
                // noStroke();
                line(x, y+len, x, y);
            }

            if(this.visited){
                noStroke(); //If there is stroke() then even
                            //if the walls are removed, then
                            //it'd look like th walls are still there.
                fill(255, 0, 255);
                rect(x, y, len, len);
            }
        };

        this.markCell = function(){
            if(this.visited){
                console.log('MARKING: ' + index(this.i, this.j));
                fill(256, 0, 256);
                rect(x, y, len, len);
            }
        };

        this.nextNeighbor = function(){
            var neighbors = [];
            let topIndex = false;
            let rightIndex = false;
            let bottomIndex = false;
            let leftIndex = false;

            if(isValidIndeX(this.i-1, this.j, index(this.i-1, this.j))){
                topIndex = this.indexxx - cols;
            }
            if(isValidIndeX(this.i, this.j+1, index(this.i, this.j+1))){
                rightIndex = this.indexxx + 1;
            }
            if(isValidIndeX(this.i+1, this.j, index(this.i+1, this.j))){
                bottomIndex = this.indexxx + cols;
            }
            if(isValidIndeX(this.i, this.j-1, index(this.i, this.j-1))){
                leftIndex = this.indexxx - 1;
            }

            console.log(topIndex);
            console.log(rightIndex);
            console.log(bottomIndex);
            console.log(leftIndex);
            

            if(topIndex && !grid[topIndex].visited){
                neighbors.push(topIndex)
            }

            if(rightIndex && !grid[rightIndex].visited){
                neighbors.push(rightIndex)
            }

            if(bottomIndex && !grid[bottomIndex].visited){
                neighbors.push(bottomIndex)
            }

            if(leftIndex && !grid[leftIndex].visited){
                neighbors.push(leftIndex)
            }

            console.log('UNVISITED NEIGHBORS: ');
            for(var i=0; i<neighbors.length; i++)
                console.log(neighbors[i]);
            
            if(neighbors.length > 0){
                let randomIndex = Math.floor(Math.random()*neighbors.length);
                console.log("Selected random index: "+ randomIndex);
                console.log('Random Index: ' + randomIndex);
                console.log('N[RandomIndex]: ' + neighbors[randomIndex]);
                console.log("grid[N[randomIndex]]" + grid[neighbors[randomIndex]]);
                
                
                return grid[neighbors[randomIndex]];
            }
            else{
                return undefined;
            }
        };

        this.colorCell = function(color){
            if(1)
            {
                fill(30, 144, 255);    
                rect(x, y, len, len);
            }
            else{
                fill(255, 0, 255);
                rect(x, y, len, len);
            }
        };
    }
}

// Walls 
// 1 TOP
// 2 RIGHT
// 3 BOTTOM
// 4 LEFT
function removeWalls(x, y){
    let difference = y.indexxx - x.indexxx;
    console.log('DIFFERENCE: ' + difference);
    if(difference == cols){
        current.walls[2] = false;
        next.walls[0] = false;
    }    
    else if(difference == -cols){
        current.walls[0] = false;
        next.walls[2] = false;        
    }
    else if(difference == 1){
        next.walls[3] = false;
        current.walls[1] = false;
    }
    else if(difference == -1){
        next.walls[1] = false;
        current.walls[3] = false;
    }
};

function draw()
{
    
    //background(51);
    for(let i=0; i<grid.length; i++)
        grid[i].show();
    
    console.log('CURRENT INDEX: ' + current.indexxx)
    next = current.nextNeighbor();
    if(next){
        next.visited = true;
        next.colorCell(1);
        removeWalls(current, next);
        current = next;
        next.colorCell(0);
    }else{
        console.log('NEXT NEIGHBOR NOT FOUND!')
        for(var i=0; i<grid.length; i++)
            console.log(grid[i])
        noLoop();
    }
    console.log("\n\n\n\n");
}