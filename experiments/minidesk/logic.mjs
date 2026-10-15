/** Pure, browser-independent local task logic. No I/O and no network access. */
export const STATUS = Object.freeze({OPEN: 'open', DONE: 'done'});

export function addTask(tasks, title, id) {
  if (!Array.isArray(tasks)) throw new TypeError('tasks must be an array');
  const clean = String(title ?? '').trim();
  if (!clean || clean.length > 120) throw new Error('title must contain 1 to 120 characters');
  if (!Number.isSafeInteger(id) || id < 1 || tasks.some(task => task.id === id)) {
    throw new Error('id must be unique and positive');
  }
  return [...tasks, {id, title: clean, status: STATUS.OPEN}];
}

export function toggleTask(tasks, id) {
  return tasks.map(task => task.id !== id ? task : {
    ...task, status: task.status === STATUS.OPEN ? STATUS.DONE : STATUS.OPEN
  });
}

export function removeTask(tasks, id) {
  return tasks.filter(task => task.id !== id);
}

export function counts(tasks) {
  const done = tasks.filter(task => task.status === STATUS.DONE).length;
  return {all: tasks.length, done, open: tasks.length - done};
}

export function sanitizeLoadedTasks(input) {
  if (!Array.isArray(input)) return [];
  const found = new Set();
  return input.filter(task => {
    if (!task || !Number.isSafeInteger(task.id) || task.id < 1 || found.has(task.id) ||
        typeof task.title !== 'string' || !task.title.trim() || task.title.length > 120 ||
        !Object.values(STATUS).includes(task.status)) return false;
    found.add(task.id);
    return true;
  });
}
