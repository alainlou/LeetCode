let all = document.getElementsByTagName('td');
arr = [];
for (let e of all) {
  if (e.innerText && !isNaN(e.innerText) && Number(e.innerText) < 1700) { arr.push(e.innerText); }
}
arr.toString();
