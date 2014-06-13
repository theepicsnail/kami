define([], function() {
  var DIR = {NONE:-1, CENTER:0, UP:1, DOWN:2, LEFT:3, RIGHT:4};
  var FILL_TIME = 0.35; //half a second to fill

  function Cell(color) {
    this.color = color;
    this.fill_start_time = 0;
    this.fill_color = 1;
    this.fill_dir = -1; //Math.floor(Math.random()*5);
    this.fill_percent = 0;
    this.up = undefined;
    this.down = undefined;
    this.left = undefined;
    this.right = undefined;
  }

  Cell.prototype.draw = function(ctx, x,y,size) {
    x -= 1;
    y -= 1;
    size -= 2;
    // Fill cell
    ctx.fillStyle = Cell.colors[this.color];
    ctx.fillRect(x, y, size, size);
//    console.log(x,y);
    // If we're filling this cell
    if (this.fill_percent !== 0 && this.fill_dir !== DIR.NONE) {
      ctx.fillStyle = Cell.colors[this.fill_color];
      var part = size * this.fill_percent; // 0 to size
      switch(this.fill_dir) {
        case DIR.UP: ctx.fillRect(x, y+size-part, size, part); break;
        case DIR.DOWN: ctx.fillRect(x, y, size, part); break;
        case DIR.LEFT: ctx.fillRect(x+size-part, y, part, size); break;
        case DIR.RIGHT: ctx.fillRect(x, y, part, size); break;
        case DIR.CENTER: ctx.fillRect(x + (size-part)/2, y + (size-part)/2, part, part); break;
      }
    }
  };

  Cell.prototype.onFill = function (){
    var self = this;
    function possiblyFill(node, dir) {
      if (node && node.fill_dir === DIR.NONE && node.color === self.color) {
        node.startFill(self.fill_color, dir);
      }
    }
    possiblyFill(this.up, Cell.DIR.UP);
    possiblyFill(this.left, Cell.DIR.LEFT);
    possiblyFill(this.down, Cell.DIR.DOWN);
    possiblyFill(this.right, Cell.DIR.RIGHT);
  };

  Cell.prototype.setTimestamp = function(timestamp) {
    if (this.fill_dir === DIR.NONE) {
      return;
    }
    var dt = timestamp - this.fill_start_time;
    // console.log(dt > 1, this.fill_dir);
    if( dt > FILL_TIME) {
      this.onFill();
      this.fill_dir = DIR.NONE;
      this.color = this.fill_color;
    }
    this.fill_percent = (timestamp - this.fill_start_time) % FILL_TIME * (1/FILL_TIME);
  };

  Cell.prototype.startFill = function(color, dir) {
    if (color === this.color) {
      return;
    }
    this.fill_start_time = +new Date()/1000;
    this.fill_color = color;
    this.fill_dir = dir;

  };
  Cell.colors = [
//    "#F88", "#8F8", "#88F",
    "#800", "#080", "#008",
    "#A00", "#840", "#A80",
    "#444", "#048", "A84",
  ];
  Cell.DIR = DIR;

  function shuffle(o){ //v1.0
    var j, x, i;
    for(i = o.length-1 ;i; i--) {
      j = Math.floor(Math.random() * i);
      x = o[--i];
      o[i] = o[j];
      o[j] = x;
    }
    return o;
  }

  Cell.colors = shuffle(Cell.colors);
  Cell.colors = [
    Cell.colors[0],
    Cell.colors[1],
    Cell.colors[2],
    Cell.colors[3]];

  return Cell;
});
