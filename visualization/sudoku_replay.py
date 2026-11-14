"""Create a standalone HTML recording of the real CSP Sudoku solver.

Run from project root:
    python -m visualization.sudoku_replay
    python -m visualization.sudoku_replay --puzzle puzzles/my_grid.json

Input JSON can be a 9x9 array or {"grid": [[...], ...]}.
"""
import argparse
import json
from pathlib import Path
from sudoku.puzzle import SudokuPuzzle

SAMPLE = [
    [5,3,0,0,7,0,0,0,0], [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0], [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1], [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0], [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9],
]

HTML = r'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Sudoku CSP Replay</title>
<style>
:root{font-family:system-ui,Segoe UI,sans-serif;color-scheme:dark;background:#101827;color:#e8eef9}
body{max-width:980px;margin:28px auto;padding:0 18px}h1{margin-bottom:6px}p{color:#b4c4d9}
.layout{display:grid;grid-template-columns:minmax(290px,500px) 1fr;gap:28px;align-items:start}
#board{display:grid;grid-template-columns:repeat(9,1fr);border:3px solid #a6b7d2;aspect-ratio:1;background:#1c2940}
.cell{display:flex;justify-content:center;align-items:center;position:relative;font-size:clamp(16px,3vw,29px);border-right:1px solid #42536e;border-bottom:1px solid #42536e}
.cell:nth-child(3n){border-right:3px solid #a6b7d2}.cell:nth-child(n+19):nth-child(-n+27),.cell:nth-child(n+46):nth-child(-n+54){border-bottom:3px solid #a6b7d2}
.cell.given{font-weight:800;color:#f6f9ff}.cell.derived{color:#73d7f6}.cell.guess{color:#ffd18a}.cell.changed{background:#284c6d} .cell.empty{color:#7489a5}
.cell .pencils{display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:repeat(3,1fr);width:100%;height:100%;align-items:center;justify-items:center;font-size:clamp(8px,1.25vw,12px);line-height:1}
.cell .pencil{opacity:.8}.cell .pencil.removed{color:#ff687a;opacity:1;text-decoration:line-through;font-weight:800}
.cell .pencil.kept{color:#8aa6c7}
.cell.in-scope{background:#21324d}.cell.changed{background:#284c6d}
.cell .new-digit{color:#7ff2b0;font-weight:800}
#details{margin-top:10px;max-height:190px;overflow:auto;font-size:13px;line-height:1.6}
#details .removed{color:#ff8c9b}#details .added{color:#7ff2b0}
.panel{border:1px solid #354560;border-radius:12px;padding:18px;background:#19253a}
.controls{display:flex;flex-wrap:wrap;gap:8px;margin:14px 0}button,select{background:#293d5d;color:white;border:1px solid #536b8f;border-radius:7px;padding:9px 12px;cursor:pointer}button:hover{background:#36537c}
input[type=range]{width:100%;accent-color:#74c9ef}#event{min-height:88px;line-height:1.6;overflow-wrap:anywhere}#event strong{color:#a5dbff}
#log{max-height:270px;overflow:auto;font:12px/1.5 Consolas,monospace;white-space:pre-wrap;color:#b6c5d9}
small{color:#b4c4d9}.key{display:flex;gap:12px;flex-wrap:wrap;margin-top:10px;font-size:13px}
@media(max-width:760px){.layout{grid-template-columns:1fr}}
</style></head><body>
<h1>Sudoku CSP — solver replay</h1><p>Actual constraint propagation and search. Small digits are candidates; red crossed-out digits were removed in this step. Highlighted cells belong to the active constraint.</p>
<div class="layout"><section><div id="board" aria-label="Sudoku grid"></div>
<div class="key"><span>⬜ Original givens</span><span style="color:#73d7f6">● Deductions</span><span style="color:#ffd18a">● Search decisions</span></div>
</section><section class="panel"><div><strong id="counter"></strong> <small id="stats"></small></div>
<input id="seek" type="range" min="0" value="0" aria-label="Replay position">
<div class="controls"><button id="first">⏮</button><button id="prev">◀ Previous</button><button id="play">▶ Play</button><button id="next">Next ▶</button><button id="last">⏭</button></div>
<label>Speed <select id="speed"><option value="1000">1 step/s</option><option value="350" selected>3 steps/s</option><option value="100">10 steps/s</option><option value="25">40 steps/s</option></select></label>
<div id="event"></div><div id="details"></div><h3>Recent events</h3><div id="log"></div></section></div>
<script id="recording" type="application/json">__DATA__</script>
<script>
const data=JSON.parse(document.getElementById('recording').textContent);
const events=data.events, original=data.grid;
const initial=Array.from({length:9},(_,r)=>Array.from({length:9},(_,c)=>original[r][c]?[original[r][c]]:Array.from({length:9},(_,i)=>i+1)));
let states=[initial], state=initial, index=0, timer=null;
for(const e of events){state=state.map(row=>row.map(domain=>domain.slice()));for(const [r,c,before,after] of e.changes)state[r][c]=after.slice();states.push(state)}
const board=document.getElementById('board'),seek=document.getElementById('seek');seek.max=events.length;
const cells=[];
for(let r=0;r<9;r++)for(let c=0;c<9;c++){const cell=document.createElement('div');cell.className='cell';board.appendChild(cell);cells.push(cell)}
function describe(e){if(!e)return 'Initial givens';const where=e.cell?`R${e.cell[0]+1}C${e.cell[1]+1}`:'';
const changed=e.changes.filter(x=>x[3].length===1&&x[2].length!==1).map(x=>`R${x[0]+1}C${x[1]+1}=${x[3][0]}`);
const removed=e.changes.reduce((n,x)=>n+x[2].filter(v=>!x[3].includes(v)).length,0);
return `${e.type.toUpperCase()} ${where}${e.value?' = '+e.value:''} — ${e.reason||''}${changed.length?' | Filled: '+changed.slice(0,12).join(', ')+(changed.length>12?' …':''):''}${removed?' | '+removed+' candidates removed':''}`}
function render(){
const state=states[index],e=events[index-1],prior=states[index-1]||states[0];
const changed=new Set(e?e.changes.map(x=>x[0]*9+x[1]):[]);
const scope=new Set(e&&e.scope?e.scope.map(x=>x[0]*9+x[1]):[]);
for(let r=0;r<9;r++)for(let c=0;c<9;c++){
 const cell=cells[r*9+c],domain=state[r][c],old=prior[r][c],given=original[r][c],id=r*9+c;
 const removed=old.filter(v=>!domain.includes(v));
 cell.replaceChildren();
 cell.className='cell '+(given?'given':domain.length===1?'derived':'empty')+(scope.has(id)?' in-scope':'')+(changed.has(id)?' changed':'');
 if(domain.length===1){
   const digit=document.createElement('span');
   digit.textContent=domain[0];
   if(old.length>1)digit.className='new-digit';
   cell.appendChild(digit);
 }else if(!given){
   const pencils=document.createElement('div');pencils.className='pencils';
   for(let v=1;v<=9;v++){
     const mark=document.createElement('span');mark.className='pencil';
     if(domain.includes(v)){mark.textContent=v;mark.classList.add('kept')}
     else if(removed.includes(v)){mark.textContent=v;mark.classList.add('removed')}
     pencils.appendChild(mark);
   }
   cell.appendChild(pencils);
 }
 cell.title=`R${r+1}C${c+1}: ${domain.join(', ')||'CONTRADICTION'}`;
}
if(e&&e.type==='decision'&&e.cell)cells[e.cell[0]*9+e.cell[1]].classList.add('guess');
seek.value=index;
document.getElementById('counter').textContent=`Step ${index} / ${events.length}`;
document.getElementById('stats').textContent=`| ${data.decisions} decisions, ${data.backtracks} backtracks`;
const eventBox=document.getElementById('event');eventBox.replaceChildren();
const strong=document.createElement('strong');strong.textContent=e?e.type.toUpperCase():'START';
const description=document.createElement('div');description.textContent=describe(e);
eventBox.append(strong,description);
const details=document.getElementById('details');details.replaceChildren();
if(e){
 const heading=document.createElement('div');
 heading.textContent=e.reason?`Constraint: ${e.reason}`:'';
 details.appendChild(heading);
 for(const [r,c,before,after] of e.changes){
   const gone=before.filter(v=>!after.includes(v));
   const line=document.createElement('div');
   const label=document.createElement('strong');label.textContent=`R${r+1}C${c+1}: `;
   line.appendChild(label);
   if(gone.length){const span=document.createElement('span');span.className='removed';span.textContent=`removed ${gone.join(', ')}`;line.appendChild(span)}
   if(after.length===1&&before.length>1){
     const span=document.createElement('span');span.className='added';span.textContent=` → assigned ${after[0]}`;line.appendChild(span);
   }
   if(after.length>1){const span=document.createElement('span');span.textContent=` | remaining: ${after.join(', ')}`;line.appendChild(span)}
   details.appendChild(line);
 }
}
document.getElementById('log').textContent=events.slice(Math.max(0,index-12),index).map((ev,i)=>`${Math.max(0,index-12)+i+1}. ${describe(ev)}`).join('\\n');
}
function pause(){if(timer!==null){clearInterval(timer);timer=null}document.getElementById('play').textContent='▶ Play'}
function go(i){index=Math.max(0,Math.min(events.length,i));render();if(index===events.length)pause()}
function play(){if(timer!==null){pause();return}if(index===events.length)go(0);document.getElementById('play').textContent='⏸ Pause';timer=setInterval(()=>go(index+1),Number(document.getElementById('speed').value))}
document.getElementById('first').onclick=()=>{pause();go(0)};document.getElementById('last').onclick=()=>{pause();go(events.length)};
document.getElementById('prev').onclick=()=>{pause();go(index-1)};document.getElementById('next').onclick=()=>{pause();go(index+1)};
document.getElementById('play').onclick=play;seek.oninput=()=>{pause();go(Number(seek.value))};document.getElementById('speed').onchange=()=>{if(timer!==null){pause();play()}};
document.addEventListener('keydown',e=>{if(e.target.tagName==='SELECT')return;if(e.key==='ArrowRight'){pause();go(index+1)}if(e.key==='ArrowLeft'){pause();go(index-1)}if(e.key===' '){e.preventDefault();play()}});
render();
</script></body></html>'''


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--puzzle', type=Path, help='JSON file containing a 9x9 grid')
    parser.add_argument('--output', type=Path, default=Path('output/solver_replay.html'))
    args = parser.parse_args()
    grid = SAMPLE
    if args.puzzle:
        raw = json.loads(args.puzzle.read_text(encoding='utf-8'))
        grid = raw['grid'] if isinstance(raw, dict) else raw
    puzzle = SudokuPuzzle(grid)
    solution, solver = puzzle.solve(trace=True)
    if solution is None:
        print('No solution found; recording the failed search.')
    record = {
        'grid': grid, 'events': solver.trace_events,
        'decisions': solver.nodes, 'backtracks': solver.backtracks,
        'solved': solution is not None,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(record, separators=(',', ':')).replace('<', '\\u003c')
    args.output.write_text(HTML.replace('__DATA__', payload), encoding='utf-8')
    print(f'Replay: {args.output} ({len(solver.trace_events)} steps, {solver.nodes} decisions, {solver.backtracks} backtracks)')


if __name__ == '__main__':
    main()
