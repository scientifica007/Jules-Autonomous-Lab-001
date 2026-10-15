import {addTask, toggleTask, removeTask, counts, sanitizeLoadedTasks, STATUS} from './logic.mjs';

const STORAGE_KEY = 'jules-lab-minidesk-demo-v1';
const form = document.querySelector('#task-form');
const titleInput = document.querySelector('#task-title');
const list = document.querySelector('#task-list');
const countOutput = document.querySelector('#counts');
const emptyState = document.querySelector('#empty-state');

function load() {
  try { return sanitizeLoadedTasks(JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]')); }
  catch { return []; }
}
let tasks = load();
let nextId = Math.max(0, ...tasks.map(task => task.id)) + 1;

function save() {
  try { localStorage.setItem(STORAGE_KEY, JSON.stringify(tasks)); }
  catch { countOutput.textContent = 'تعذر الحفظ المحلي — البيانات في الذاكرة فقط'; }
}

function actionButton(label, className, click) {
  const button = document.createElement('button');
  button.type = 'button';
  button.textContent = label;
  button.className = className;
  button.addEventListener('click', click);
  return button;
}

// TODO(Jules): export locally stored test tasks to a user-initiated JSON download, never to a server.
function render() {
  list.replaceChildren();
  const count = counts(tasks);
  countOutput.textContent = `${count.all} مهمة — ${count.done} منجزة`;
  emptyState.hidden = tasks.length > 0;
  for (const task of tasks) {
    const item = document.createElement('li');
    item.className = 'task';
    const title = document.createElement('span');
    title.textContent = task.title;  // Never insert user text via innerHTML.
    if (task.status === STATUS.DONE) title.className = 'done';
    const controls = document.createElement('div');
    controls.append(
      actionButton(task.status === STATUS.OPEN ? 'إنجاز' : 'إعادة فتح', '', () => {
        tasks = toggleTask(tasks, task.id); save(); render();
      }),
      actionButton('حذف', 'delete', () => {
        tasks = removeTask(tasks, task.id); save(); render();
      })
    );
    item.append(title, controls);
    list.append(item);
  }
}

form.addEventListener('submit', event => {
  event.preventDefault();
  try {
    tasks = addTask(tasks, titleInput.value, nextId++);
    titleInput.value = '';
    save(); render(); titleInput.focus();
  } catch (error) {
    titleInput.setCustomValidity(error.message);
    titleInput.reportValidity();
  }
});
titleInput.addEventListener('input', () => titleInput.setCustomValidity(''));
render();
