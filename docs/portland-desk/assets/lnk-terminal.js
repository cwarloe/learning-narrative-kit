/**
 * Learning Narrative Kit (LNK) — Interactive In-Browser Micro-Terminal Engine
 * Zero-backend client-side terminal simulator for Docsify courseware
 */

(function () {
  'use strict';

  window.initLnkTerminals = function () {
    document.querySelectorAll('.lnk-terminal-instance').forEach(function (el) {
      if (el.dataset.initialized) return;
      el.dataset.initialized = 'true';

      let config = {};
      let commands = {};
      try {
        config = JSON.parse(decodeURIComponent(el.getAttribute('data-config') || '%7B%7D'));
        commands = JSON.parse(decodeURIComponent(el.getAttribute('data-commands') || '%7B%7D'));
      } catch (err) {
        console.warn('Could not parse terminal attributes', err);
      }

      const objectives = config.objectives || [];
      const screen = el.querySelector('.lnk-term-screen');
      const input = el.querySelector('.lnk-term-input');
      const promptText = config.prompt || (config.shell === 'powershell' ? 'PS C:\\Support> ' : (config.shell === 'serial' ? 'SCALE_04# ' : 'C:\\> '));
      const history = [];
      let historyIdx = -1;

      function appendLine(html, isOutput) {
        const line = document.createElement('div');
        line.className = isOutput ? 'lnk-term-output-block' : 'lnk-term-line';
        line.innerHTML = html;
        const row = el.querySelector('.lnk-term-input-row');
        if (row && row.parentNode) {
          row.parentNode.insertBefore(line, row);
        } else {
          screen.appendChild(line);
        }
        screen.scrollTop = screen.scrollHeight;
      }

      function checkObjectives(cmd) {
        const cleanCmd = cmd.trim().toLowerCase();
        objectives.forEach(function (obj) {
          if (cleanCmd === (obj.trigger || '').trim().toLowerCase()) {
            const pill = Array.from(el.querySelectorAll('.lnk-term-obj-pill')).find(function (p) { return p.dataset.obj === obj.id; });
            if (pill && !pill.classList.contains('completed')) {
              pill.classList.add('completed');
              const check = pill.querySelector('.lnk-term-obj-check');
              if (check) check.textContent = '[OK]';
            }
          }
        });
      }

      function executeCommand(rawCmd) {
        const cmd = rawCmd.trim();
        if (!cmd) return;

        appendLine('<span class="lnk-term-prompt">' + escapeHtml(promptText) + '</span> <span class="lnk-term-cmd">' + escapeHtml(cmd) + '</span>', false);
        history.push(cmd);
        historyIdx = history.length;

        if (cmd === 'clear' || cmd === 'cls') {
          screen.querySelectorAll('.lnk-term-line, .lnk-term-output-block').forEach(function (l) { l.remove(); });
          input.value = '';
          return;
        }

        // Exact or case-insensitive match
        const foundKey = Object.keys(commands).find(function (k) {
          return k.toLowerCase() === cmd.toLowerCase();
        });

        if (foundKey) {
          appendLine('<pre class="lnk-term-output">' + escapeHtml(commands[foundKey]) + '</pre>', true);
          checkObjectives(cmd);
        } else if (cmd.startsWith('ping')) {
          appendLine('<pre class="lnk-term-output">Pinging target [Host unreachable or clock desynchronized]. Check interface parameters.</pre>', true);
        } else if (cmd === 'help') {
          const avail = Object.keys(commands).concat(['clear', 'help']).join('  |  ');
          appendLine('<pre class="lnk-term-output">Available diagnostics:\n' + escapeHtml(avail) + '</pre>', true);
        } else {
          appendLine('<pre class="lnk-term-output error">Command or framing not recognized: \'' + escapeHtml(cmd) + '\'\nType \'help\' to view active diagnostic routines.</pre>', true);
        }

        input.value = '';
      }

      function escapeHtml(str) {
        return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
      }

      if (input) {
        input.addEventListener('keydown', function (e) {
          if (e.key === 'Enter') {
            e.preventDefault();
            executeCommand(input.value);
          } else if (e.key === 'ArrowUp') {
            if (historyIdx > 0) {
              historyIdx--;
              input.value = history[historyIdx] || '';
            }
          } else if (e.key === 'ArrowDown') {
            if (historyIdx < history.length - 1) {
              historyIdx++;
              input.value = history[historyIdx] || '';
            } else {
              historyIdx = history.length;
              input.value = '';
            }
          }
        });
      }

      screen.addEventListener('click', function () {
        if (input) input.focus();
      });

      // Animated Keystroke Replay
      const replayBtn = el.querySelector('.lnk-term-replay-btn');
      if (replayBtn) {
        replayBtn.addEventListener('click', function () {
          const triggers = objectives.map(function (o) { return o.trigger; }).filter(Boolean);
          if (triggers.length === 0 || replayBtn.disabled) return;
          replayBtn.disabled = true;
          input.disabled = true;
          let currentTrigger = 0;

          function finishReplay() {
            replayBtn.disabled = false;
            input.disabled = false;
          }

          function typeNext() {
            if (!el.isConnected || currentTrigger >= triggers.length) {
              finishReplay();
              return;
            }
            const text = triggers[currentTrigger];
            let charIdx = 0;
            input.value = '';

            const interval = setInterval(function () {
              if (!el.isConnected) {
                clearInterval(interval);
                finishReplay();
                return;
              }
              if (charIdx < text.length) {
                input.value += text[charIdx];
                charIdx++;
              } else {
                clearInterval(interval);
                setTimeout(function () {
                  if (!el.isConnected) { finishReplay(); return; }
                  executeCommand(text);
                  currentTrigger++;
                  setTimeout(typeNext, 850);
                }, 400);
              }
            }, 45);
          }
          typeNext();
        });
      }
    });
  };
})();
