const $ = (id) => document.getElementById(id);
const repo = 'https://github.com/matteoroda05/leetcode/blob/main/';
const colors = {Easy:'#64dba7', Medium:'#f5c76d', Hard:'#fa897e'};
let problems = [];
$('year').textContent = new Date().getFullYear();

function countBy(items, key) {
  return items.reduce((counts, item) => (counts[item[key]] = (counts[item[key]] || 0) + 1, counts), {});
}
function renderStats() {
  const byDifficulty = countBy(problems, 'difficulty');
  for (const difficulty of ['Easy','Medium','Hard']) $(difficulty.toLowerCase()).textContent = byDifficulty[difficulty] || 0;
  $('total').textContent = $('ring-value').firstChild.textContent = problems.length;
  const total = problems.length || 1;
  let cursor = 0;
  const stops = [];
  const legend = $('difficulty-legend');
  for (const difficulty of ['Easy','Medium','Hard']) {
    const fraction = (byDifficulty[difficulty] || 0) / total * 100;
    stops.push(`${colors[difficulty]} ${cursor}% ${cursor + fraction}%`);
    cursor += fraction;
    const row = document.createElement('div'); row.className = 'legend-row';
    const dot = document.createElement('i'); dot.className = `dot ${difficulty.toLowerCase()}`;
    const label = document.createElement('span'); label.textContent = difficulty;
    const number = document.createElement('strong'); number.textContent = byDifficulty[difficulty] || 0;
    row.append(dot,label,number); legend.append(row);
  }
  $('ring').style.background = `conic-gradient(${stops.join(',')})`;
  const languages = Object.entries(countBy(problems, 'lang')).sort((a,b) => b[1]-a[1]);
  const display = {Python3:'Python',Python:'Python',cpp:'C++',golang:'Go',javascript:'JavaScript',typescript:'TypeScript',csharp:'C#'};
  const combined = {};
  for (const [lang,n] of languages) combined[display[lang] || lang] = (combined[display[lang] || lang] || 0) + n;
  for (const [lang,n] of Object.entries(combined).sort((a,b) => b[1]-a[1]).slice(0,5)) {
    const item = document.createElement('div');
    const line = document.createElement('div'); line.className='language-line';
    const name=document.createElement('span'); name.textContent=lang;
    const amount=document.createElement('span'); amount.textContent=`${n} · ${Math.round(n/total*100)}%`;
    line.append(name,amount);
    const track=document.createElement('div'); track.className='track';
    const fill=document.createElement('span'); fill.style.width=`${n/total*100}%`;
    track.append(fill); item.append(line,track); $('language-list').append(item);
  }
  for (const lang of [...new Set(problems.map(p=>p.lang))].sort()) {
    const option=document.createElement('option'); option.value=lang; option.textContent=display[lang] || lang;
    $('language-filter').append(option);
  }
  const newest = problems.map(p=>p.date).sort().at(-1);
  $('updated').textContent = newest ? `Latest archived solution · ${newest}` : 'No solutions archived yet';
}
function cell(row, content, className) {
  const td=document.createElement('td'); if(className) td.className=className;
  if(typeof content==='string') td.textContent=content; else td.append(content);
  row.append(td); return td;
}
function renderTable() {
  const query=$('search').value.trim().toLowerCase();
  const difficulty=$('difficulty-filter').value, language=$('language-filter').value;
  const items=problems.filter(p=>(difficulty==='all'||p.difficulty===difficulty)&&(language==='all'||p.lang===language)&&(`${p.qid} ${p.title}`.toLowerCase().includes(query)));
  const sort=$('sort').value;
  items.sort((a,b)=>sort==='number' ? Number(a.qid)-Number(b.qid) : sort==='title' ? a.title.localeCompare(b.title) : b.date.localeCompare(a.date)||Number(a.qid)-Number(b.qid));
  $('result-count').textContent=`${items.length} of ${problems.length} problems`;
  const body=$('problems'); body.replaceChildren();
  if(!items.length) {const row=document.createElement('tr');cell(row,'No matching problems. Try another search.','empty').colSpan=6;body.append(row);return;}
  const fragment=document.createDocumentFragment();
  for(const p of items) {
    const row=document.createElement('tr'); cell(row,p.qid,'number');
    const title=document.createElement('a');title.href=`https://leetcode.com/problems/${encodeURIComponent(p.slug)}/`;title.target='_blank';title.rel='noopener noreferrer';title.textContent=p.title;cell(row,title);
    const badge=document.createElement('span');badge.className=`pill ${p.difficulty}`;badge.textContent=p.difficulty;cell(row,badge);
    const display={Python3:'Python',Python:'Python',cpp:'C++',golang:'Go',javascript:'JavaScript',typescript:'TypeScript',csharp:'C#'};
    cell(row,display[p.lang]||p.lang);cell(row,p.date);
    const source=document.createElement('a');source.className='source';source.textContent='CODE ↗';source.href=repo+`src/${p.difficulty.toLowerCase()}/${p.qid}-${p.slug}/solution.${p.ext}`;source.target='_blank';source.rel='noopener noreferrer';source.setAttribute('aria-label',`View solution for ${p.title}`);cell(row,source);
    fragment.append(row);
  }
  body.append(fragment);
}
async function start() {
  try {
    const response=await fetch('./data.json',{cache:'no-cache'});
    if(!response.ok) throw new Error(`HTTP ${response.status}`);
    const data=await response.json();
    if(!Array.isArray(data.problems)) throw new Error('Invalid data');
    problems=data.problems;
    renderStats();renderTable();
    for(const id of ['search','difficulty-filter','language-filter','sort']) $(id).addEventListener(id==='search'?'input':'change',renderTable);
  } catch(error) {
    console.error('Could not load archive:',error);
    $('updated').textContent='Archive unavailable';
    $('problems').replaceChildren();
    const row=document.createElement('tr');cell(row,'Could not load solutions. Please refresh the page.','empty').colSpan=6;$('problems').append(row);
  }
}
start();
