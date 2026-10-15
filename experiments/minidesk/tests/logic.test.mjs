import test from 'node:test';
import assert from 'node:assert/strict';
import {addTask, toggleTask, removeTask, counts, sanitizeLoadedTasks} from '../logic.mjs';

test('create a task immutably', () => {
  const original = [];
  const updated = addTask(original, ' test ', 1);
  assert.equal(original.length, 0);
  assert.deepEqual(updated, [{id: 1, title: 'test', status: 'open'}]);
});

test('reject blank and overlong titles', () => {
  assert.throws(() => addTask([], '   ', 1));
  assert.throws(() => addTask([], 'x'.repeat(121), 1));
});

test('reject duplicate identifiers', () => {
  assert.throws(() => addTask(addTask([], 'one', 1), 'two', 1));
});

test('toggle updates just one task', () => {
  const tasks = addTask(addTask([], 'one', 1), 'two', 2);
  const updated = toggleTask(tasks, 2);
  assert.deepEqual(counts(updated), {all: 2, done: 1, open: 1});
  assert.equal(tasks[1].status, 'open');
});

test('remove a task without touching the original', () => {
  const tasks = addTask([], 'one', 1);
  assert.deepEqual(removeTask(tasks, 1), []);
  assert.equal(tasks.length, 1);
});

test('reject invalid loaded records', () => {
  const cleaned = sanitizeLoadedTasks([{id: 1, title: 'ok', status: 'open'},
    {id: 1, title: 'duplicate', status: 'open'},
    {id: 2, title: '<img src=x>', status: 'done'},
    {id: 3, title: '', status: 'done'}]);
  assert.equal(cleaned.length, 2);
  assert.equal(cleaned[1].title, '<img src=x>');
});
