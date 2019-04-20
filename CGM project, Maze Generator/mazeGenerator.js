console.log('maxGen is connected');

var len = 400;
var side = 40;
var rows = len/side;
var cols = len/side;
var grid = [];
var firstLoop = true;

function setup()
{
    createCanvas(len, len);
    background(50);
    for(var i=0; i<len; i+=side)
    {    
        for(var j=0; j<len; j+=side)
        {
            console.log('running')
            var c = new Cell(i, j);
            grid.push(c);
        }
    }

    for(var i=0; i<grid.length; i++)
        grid[i].show();
    
    console.log('All cells are ready!');

}

function isValid(index)
{
    return (index >= 0 && index < 100)
}

class Cell {
    constructor(x, y) {
        this.walls = [true, true, true, true]; //Top, Right, Bottom, Left
        this.visited = false;
        this.i = floor(x/40);
        this.j = floor(y/40);
        console.log(this.i, this.j);
        console.log(this.i*cols + this.j);

        this.show = function () {
            stroke(255);
            if (this.walls[0])
                line(x, y, x + len, y);
            if (this.walls[1])
                line(x + len, y, x + len, y + len);
            if (this.walls[2])
                line(x + len, y + len, x, y + len);
            if (this.walls[3])
                line(x, y + len, x, y);
        };

        
        this.checkNeighbors = function(){
            console.log("CHECKNEIGHBORS WAS CALLED");
            let neighbors = [];

            let topIndex = (this.i-1)*cols + this.j;
            let rightIndex = this.i*cols + this.j+1;
            let bottomIndex = (this.i+1)*cols + this.j;
            let leftIndex = this.i*cols + this.j-1;

            if(isValid(topIndex) && !grid[topIndex].visited)
                {
                    console.log('is valid 1')
                    neighbors.push(topIndex);
                }
            if(isValid(rightIndex) && !grid[rightIndex].visited)
                {
                    console.log('is valid 2')
                    neighbors.push(rightIndex);
                }
            if(isValid(bottomIndex) && !grid[bottomIndex].visited)
                {
                    console.log('is valid 3')
                    neighbors.push(bottomIndex);
                }
            if(isValid(leftIndex) && !grid[leftIndex].visited)
                {
                    console.log('is valid 4')
                    neighbors.push(leftIndex);
                }
            
            console.log('Unvisited neighbors: ')
            for(var i=0; i<neighbors.length; i++)
            {
                console.log(neighbors[i]);
            }

            if(neighbors.length > 0){
                var randomIndex = Math.floor(Math.random()*neighbors.length);
                console.log('RandomIndex: ' + randomIndex);
                return grid[randomIndex];
            }
            else{
                return undefined;
            }
        };   

        this.markCell = function(){
            if(this.visited)
            {
                fill(255, 0, 255);
                rect(x, y, x+side, y+side);
            }
        };
    }
}

function draw()
{
    //background(50);  
    frameRate(5);
    if(firstLoop){
        current = grid[0];
        firstLoop = false;
    }

    current.visited = true;
    current.markCell();
    console.log('marked first cell');
    var nextIndex = current.checkNeighbors();
    var nextCell = nextIndex; 
    console.log('found next cell');
    if(nextCell){
        console.log('Index of next cell is: ');
        console.log(nextCell.i, nextCell.j);
        nextCell.visited = true;
        nextCell.markCell();
        current = nextCell;
    }
    else{
        noLoop();
    }
}