// /**
//  * Enhanced JavaScript for Professional Text Encrypter
//  * Features: Modern ES6+, Error Handling, Performance Optimization
//  */

// class TextEncrypter {
//     constructor() {
//         this.currentMode = 'encrypt';
//         this.isProcessing = false;
//         this.statsRefreshInterval = null;
//         this.debounceTimers = new Map();
        
//         // DOM elements cache
//         this.elements = {};
//         this.initializeElements();
//         this.initializeEventListeners();
//         this.initializeApp();
//     }

//     initializeElements() {
//         const elementIds = [
//             'inputText', 'resultText', 'algorithmSelect', 'passwordInput',
//             'passwordGroup', 'processBtn', 'messageContainer', 'statsContent',
//             'operationCount', 'uptime', 'inputLabel', 'passwordStrength',
//             'keyLength', 'keyLengthDisplay', 'includeSymbols', 'autoRefresh',
//             'settingsContent', 'settingsToggleIcon', 'passwordToggleIcon'
//         ];

//         elementIds.forEach(id => {
//             this.elements[id] = document.getElementById(id);
//         });

//         // Cache frequently used selectors
//         this.elements.modeOptions = document.querySelectorAll('.mode-option');
//         this.elements.charCounter = document.querySelector('.char-counter');
//         this.elements.algorithmInfo = document.getElementById('algorithmInfo');
//     }

//     initializeEventListeners() {
//         // Mode selector
//         this.elements.modeOptions.forEach(option => {
//             option.addEventListener('click', (e) => this.switchMode(e.target.dataset.mode));
//         });

//         // Input text change with debounce
//         this.elements.inputText?.addEventListener('input', (e) => {
//             this.debounce('characterCount', () => this.updateCharacterCount(), 100);
//             this.debounce('passwordStrength', () => this.updatePasswordStrength(), 300);
//         });

//         // Algorithm change
//         this.elements.algorithmSelect?.addEventListener('change', () => {
//             this.handleAlgorithmChange();
//         });

//         // Password input
//         this.elements.passwordInput?.addEventListener('input', () => {
//             this.debounce('passwordStrength', () => this.updatePasswordStrength(), 200);
//         });

//         // Key length slider
//         this.elements.keyLength?.addEventListener('input', () => {
//             this.updateKeyLengthDisplay();
//         });

//         // Keyboard shortcuts
//         document.addEventListener('keydown', (e) => this.handleKeyboardShortcuts(e));

//         // Auto-refresh toggle
//         this.elements.autoRefresh?.addEventListener('change', (e) => {
//             this.toggleAutoRefresh(e.target.checked);
//         });

//         // Window events
//         window.addEventListener('beforeunload', () => this.cleanup());
//         document.addEventListener('visibilitychange', () => this.handleVisibilityChange());
//     }

//     initializeApp() {
//         this.hideLoadingScreen();
//         this.handleAlgorithmChange();
//         this.updateCharacterCount();
//         this.loadInitialStats();
//         this.startUptimeCounter();
//         this.toggleAutoRefresh(true);
        
//         // Add entrance animations
//         this.addEntranceAnimations();
//     }

//     hideLoadingScreen() {
//         setTimeout(() => {
//             const loadingScreen = document.getElementById('loadingScreen');
//             if (loadingScreen) {
//                 loadingScreen.classList.add('hidden');
//                 setTimeout(() => loadingScreen.remove(), 500);
//             }
//         }, 1500);
//     }

//     addEntranceAnimations() {
//         const animatedElements = document.querySelectorAll('.crypto-box, .stats-panel, .advanced-settings');
//         animatedElements.forEach((el, index) => {
//             setTimeout(() => {
//                 el.classList.add('fade-in');
//             }, index * 200);
//         });
//     }

//     // Utility function for debouncing
//     debounce(key, func, delay) {
//         if (this.debounceTimers.has(key)) {
//             clearTimeout(this.debounceTimers.get(key));
//         }
        
//         const timeoutId = setTimeout(func, delay);
//         this.debounceTimers.set(key, timeoutId);
//     }

//     // Mode switching
//     switchMode(mode) {
//         if (this.isProcessing || this.currentMode === mode) return;

//         this.currentMode = mode;
        
//         // Update UI
//         this.elements.modeOptions.forEach(option => {
//             option.classList.toggle('active', option.dataset.mode === mode);
//         });

//         // Update labels and button text
//         const isEncrypt = mode === 'encrypt';
//         if (this.elements.inputLabel) {
//             this.elements.inputLabel.textContent = isEncrypt ? '🔤 Text to Encrypt' : '🔓 Text to Decrypt';
//         }

//         if (this.elements.processBtn) {
//             this.elements.processBtn.querySelector('.btn-icon').textContent = isEncrypt ? '🔒' : '🔓';
//             this.elements.processBtn.querySelector('.btn-text').textContent = isEncrypt ? 'Encrypt Text' : 'Decrypt Text';
//         }

//         // Clear previous results
//         this.clearResults();
        
//         // Add mode switch animation
//         this.addModeAnimation();
//     }

//     addModeAnimation() {
//         const cryptoBox = document.querySelector('.crypto-box');
//         if (cryptoBox) {
//             cryptoBox.style.transform = 'scale(0.98)';
//             setTimeout(() => {
//                 cryptoBox.style.transform = 'scale(1)';
//             }, 150);
//         }
//     }

//     // Algorithm handling
//     handleAlgorithmChange() {
//         const algorithm = this.elements.algorithmSelect?.value;
//         const showPassword = algorithm === 'fernet';
        
//         // Show/hide password field
//         if (this.elements.passwordGroup) {
//             this.elements.passwordGroup.style.display = showPassword ? 'block' : 'none';
//         }

//         // Update algorithm info
//         this.updateAlgorithmInfo(algorithm);
        
//         // Clear results when switching algorithms
//         this.clearResults();
//     }

//     updateAlgorithmInfo(algorithm) {
//         if (!this.elements.algorithmInfo) return;

//         const algorithmData = {
//             caesar: {
//                 badge: { class: 'info-learning', text: 'Learning Algorithm' },
//                 description: 'Simple shift-based encryption perfect for educational purposes'
//             },
//             fernet: {
//                 badge: { class: 'info-secure', text: 'Production Ready' },
//                 description: 'AES-256 encryption with authentication - industry standard security'
//             },
//             hash: {
//                 badge: { class: 'info-hash', text: 'One-Way Function' },
//                 description: 'SHA-256 cryptographic hash - cannot be reversed or decrypted'
//             }
//         };

//         const data = algorithmData[algorithm];
//         if (data) {
//             this.elements.algorithmInfo.innerHTML = `
//                 <span class="info-badge ${data.badge.class}">${data.badge.text}</span>
//                 <span class="info-text">${data.description}</span>
//             `;
//         }
//     }

//     // Character count and validation
//     updateCharacterCount() {
//         const text = this.elements.inputText?.value || '';
//         const count = text.length;
//         const maxLength = 10000;
        
//         if (this.elements.charCounter) {
//             this.elements.charCounter.textContent = `${count} / ${maxLength}`;
//             this.elements.charCounter.style.color = count > maxLength * 0.9 ? '#dc3545' : '#666666';
//         }

//         // Validate input length
//         if (count > maxLength) {
//             this.showMessage('Text too long! Maximum 10,000 characters allowed.', 'error');
//             return false;
//         }
        
//         return true;
//     }

//     // Password strength indicator
//     updatePasswordStrength() {
//         const password = this.elements.passwordInput?.value || '';
//         const strengthElement = this.elements.passwordStrength;
        
//         if (!strengthElement || !password) {
//             strengthElement?.setAttribute('class', 'password-strength');
//             return;
//         }

//         const strength = this.calculatePasswordStrength(password);
//         strengthElement.setAttribute('class', `password-strength ${strength.level}`);
//         strengthElement.setAttribute('title', `Password strength: ${strength.score}/100`);
//     }

//     calculatePasswordStrength(password) {
//         let score = 0;
//         let level = 'weak';

//         // Length bonus
//         score += Math.min(password.length * 4, 40);

//         // Character variety
//         if (/[a-z]/.test(password)) score += 10;
//         if (/[A-Z]/.test(password)) score += 10;
//         if (/[0-9]/.test(password)) score += 10;
//         if (/[^A-Za-z0-9]/.test(password)) score += 15;

//         // Pattern penalties
//         if (/(.)\1{2,}/.test(password)) score -= 10;
//         if (/123|abc|qwe/i.test(password)) score -= 15;

//         // Determine level
//         if (score >= 70) level = 'strong';
//         else if (score >= 40) level = 'medium';

//         return { score: Math.max(0, Math.min(100, score)), level };
//     }

//     // Main processing function
//     async processText() {
//         if (this.isProcessing) return;

//         const inputText = this.elements.inputText?.value?.trim();
//         if (!inputText) {
//             this.showMessage('Please enter some text to process!', 'error');
//             this.elements.inputText?.focus();
//             return;
//         }

//         if (!this.updateCharacterCount()) return;

//         this.setProcessingState(true);

//         try {
//             const requestData = {
//                 text: inputText,
//                 method: this.elements.algorithmSelect?.value || 'caesar',
//                 password: this.elements.passwordInput?.value || 'defaultpass',
//                 action: this.currentMode
//             };

//             const response = await this.makeApiRequest('/process', {
//                 method: 'POST',
//                 headers: { 'Content-Type': 'application/json' },
//                 body: JSON.stringify(requestData)
//             });

//             if (response.success) {
//                 this.handleSuccessfulProcess(response);
//             } else {
//                 throw new Error(response.error || 'Processing failed');
//             }

//         } catch (error) {
//             this.handleProcessingError(error);
//         } finally {
//             this.setProcessingState(false);
//         }
//     }

//     handleSuccessfulProcess(response) {
//         if (this.elements.resultText) {
//             this.elements.resultText.value = response.result;
//         }

//         // Update result info
//         const resultInfo = document.querySelector('.result-info');
//         if (resultInfo) {
//             resultInfo.textContent = `${response.method} • ${response.input_length}→${response.output_length} chars`;
//         }

//         // Show success message
//         const message = `✅ ${response.action} completed successfully! (${response.output_length} characters)`;
//         this.showMessage(message, 'success');

//         // Add success animation
//         this.elements.processBtn?.classList.add('success-pulse');
//         setTimeout(() => {
//             this.elements.processBtn?.classList.remove('success-pulse');
//         }, 600);

//         // Auto-refresh stats
//         this.refreshStats();
//     }

//     handleProcessingError(error) {
//         console.error('Processing error:', error);
//         const message = error.message || 'An unexpected error occurred. Please try again.';
//         this.showMessage(`❌ ${message}`, 'error');
//     }

//     setProcessingState(isProcessing) {
//         this.isProcessing = isProcessing;
        
//         if (this.elements.processBtn) {
//             this.elements.processBtn.classList.toggle('loading', isProcessing);
//             this.elements.processBtn.disabled = isProcessing;
//         }

//         // Disable other buttons during processing
//         const buttons = document.querySelectorAll('.btn:not(#processBtn)');
//         buttons.forEach(btn => {
//             btn.disabled = isProcessing;
//         });
//     }

//     // Key generation
//     async generateSecureKey() {
//         try {
//             const length = this.elements.keyLength?.value || 16;
//             const includeSymbols = this.elements.includeSymbols?.checked ?? true;
            
//             const response = await this.makeApiRequest(
//                 `/generate-key?length=${length}&symbols=${includeSymbols}`
//             );

//             if (response.success) {
//                 if (this.elements.passwordInput) {
//                     this.elements.passwordInput.value = response.key;
//                     this.updatePasswordStrength();
//                 }
                
//                 this.showMessage(`🔑 Generated ${response.strength.toLowerCase()} key (${response.length} chars)`, 'success');
//             } else {
//                 throw new Error(response.error || 'Key generation failed');
//             }

//         } catch (error) {
//             console.error('Key generation error:', error);
//             this.showMessage('❌ Failed to generate key. Please try again.', 'error');
//         }
//     }

//     // Utility functions
//     async clearInput() {
//         if (this.elements.inputText) {
//             this.elements.inputText.value = '';
//             this.updateCharacterCount();
//             this.elements.inputText.focus();
//         }
//     }

//     async pasteFromClipboard() {
//         try {
//             const text = await navigator.clipboard.readText();
//             if (this.elements.inputText) {
//                 this.elements.inputText.value = text;
//                 this.updateCharacterCount();
//                 this.showMessage('📋 Text pasted from clipboard!', 'success');
//             }
//         } catch (error) {
//             this.showMessage('❌ Unable to access clipboard. Please paste manually.', 'error');
//         }
//     }

//     async copyResult() {
//         const resultText = this.elements.resultText?.value;
//         if (!resultText) {
//             this.showMessage('❌ No result to copy!', 'error');
//             return;
//         }

//         try {
//             await navigator.clipboard.writeText(resultText);
//             this.showMessage('📋 Result copied to clipboard!', 'success');
//         } catch (error) {
//             // Fallback for older browsers
//             this.fallbackCopyToClipboard(resultText);
//         }
//     }

//     fallbackCopyToClipboard(text) {
//         const textArea = document.createElement('textarea');
//         textArea.value = text;
//         textArea.style.position = 'fixed';
//         textArea.style.opacity = '0';
//         document.body.appendChild(textArea);
//         textArea.focus();
//         textArea.select();
        
//         try {
//             document.execCommand('copy');
//             this.showMessage('📋 Result copied to clipboard!', 'success');
//         } catch (error) {
//             this.showMessage('❌ Unable to copy to clipboard', 'error');
//         }
        
//         document.body.removeChild(textArea);
//     }

//     swapTexts() {
//         const inputValue = this.elements.inputText?.value || '';
//         const resultValue = this.elements.resultText?.value || '';
        
//         if (this.elements.inputText) this.elements.inputText.value = resultValue;
//         if (this.elements.resultText) this.elements.resultText.value = inputValue;
        
//         this.updateCharacterCount();
//         this.showMessage('🔄 Input and result swapped!', 'info');
//     }

//     downloadResult() {
//         const resultText = this.elements.resultText?.value;
//         if (!resultText) {
//             this.showMessage('❌ No result to download!', 'error');
//             return;
//         }

//         const algorithm = this.elements.algorithmSelect?.value || 'unknown';
//         const timestamp = new Date().toISOString().slice(0, 19).replace(/[:.]/g, '-');
//         const filename = `encrypted-text-${algorithm}-${timestamp}.txt`;
        
//         this.downloadTextFile(resultText, filename);
//         this.showMessage(`💾 Result downloaded as ${filename}`, 'success');
//     }

//     downloadTextFile(content, filename) {
//         const blob = new Blob([content], { type: 'text/plain' });
//         const url = URL.createObjectURL(blob);
//         const link = document.createElement('a');
//         link.href = url;
//         link.download = filename;
//         link.style.display = 'none';
//         document.body.appendChild(link);
//         link.click();
//         document.body.removeChild(link);
//         URL.revokeObjectURL(url);
//     }

//     async shareResult() {
//         const resultText = this.elements.resultText?.value;
//         if (!resultText) {
//             this.showMessage('❌ No result to share!', 'error');
//             return;
//         }

//         if (navigator.share && /Mobile|Android|iPhone|iPad/i.test(navigator.userAgent)) {
//             try {
//                 await navigator.share({
//                     title: 'Encrypted Text',
//                     text: resultText,
//                     url: window.location.href
//                 });
//                 this.showMessage('📤 Result shared successfully!', 'success');
//             } catch (error) {
//                 if (error.name !== 'AbortError') {
//                     this.fallbackShare(resultText);
//                 }
//             }
//         } else {
//             this.fallbackShare(resultText);
//         }
//     }

//     fallbackShare(text) {
//         // Copy to clipboard as fallback
//         this.copyResult();
//     }

//     // Statistics management
//     async refreshStats() {
//         try {
//             const response = await this.makeApiRequest('/stats');
//             this.displayStats(response);
//             this.updateHeaderStats(response);
//         } catch (error) {
//             console.error('Stats loading error:', error);
//             if (this.elements.statsContent) {
//                 this.elements.statsContent.innerHTML = '<div class="error-state">Failed to load statistics</div>';
//             }
//         }
//     }

//     displayStats(stats) {
//         if (!this.elements.statsContent) return;

//         if (stats.message) {
//             this.elements.statsContent.innerHTML = `
//                 <div class="error-state">
//                     <div class="error-icon">📊</div>
//                     <p>${stats.message}</p>
//                 </div>
//             `;
//             return;
//         }

//         const statsHtml = `
//             <div class="stat-card">
//                 <h4>📈 Overview</h4>
//                 <div class="stat-item-row">
//                     <span class="stat-label-text">Total Operations</span>
//                     <span class="stat-value-text">${stats.total_operations || 0}</span>
//                 </div>
//                 <div class="stat-item-row">
//                     <span class="stat-label-text">Characters Processed</span>
//                     <span class="stat-value-text">${(stats.total_characters || 0).toLocaleString()}</span>
//                 </div>
//                 <div class="stat-item-row">
//                     <span class="stat-label-text">Average Length</span>
//                     <span class="stat-value-text">${stats.average_length || 0} chars</span>
//                 </div>
//                 <div class="stat-item-row">
//                     <span class="stat-label-text">Success Rate</span>
//                     <span class="stat-value-text">${stats.success_rate || 0}%</span>
//                 </div>
//             </div>
            
//             <div class="stat-card">
//                 <h4>🔧 Algorithms Used</h4>
//                 ${Object.entries(stats.methods_used || {}).map(([method, count]) => `
//                     <div class="stat-item-row">
//                         <span class="stat-label-text">${method}</span>
//                         <span class="stat-value-text">${count}</span>
//                     </div>
//                 `).join('')}
//                 ${Object.keys(stats.methods_used || {}).length === 0 ? 
//                     '<p class="stat-label-text">No algorithms used yet</p>' : ''}
//             </div>
            
//             <div class="stat-card">
//                 <h4>⏱️ System Info</h4>
//                 <div class="stat-item-row">
//                     <span class="stat-label-text">Uptime</span>
//                     <span class="stat-value-text">${stats.uptime || '00:00:00'}</span>
//                 </div>
//                 <div class="stat-item-row">
//                     <span class="stat-label-text">Most Used</span>
//                     <span class="stat-value-text">${stats.most_used || 'None'}</span>
//                 </div>
//             </div>
//         `;

//         this.elements.statsContent.innerHTML = statsHtml;
//     }

//     updateHeaderStats(stats) {
//         if (this.elements.operationCount) {
//             this.elements.operationCount.textContent = stats.total_operations || 0;
//         }
//     }

//     async loadInitialStats() {
//         await this.refreshStats();
//     }

//     toggleAutoRefresh(enabled) {
//         if (this.statsRefreshInterval) {
//             clearInterval(this.statsRefreshInterval);
//             this.statsRefreshInterval = null;
//         }

//         if (enabled) {
//             this.statsRefreshInterval = setInterval(() => {
//                 this.refreshStats();
//             }, 10000); // Refresh every 10 seconds
//         }
//     }

//     async clearHistory() {
//         try {
//             const response = await this.makeApiRequest('/clear-history', {
//                 method: 'POST'
//             });

//             if (response.message) {
//                 this.showMessage('🗑️ History cleared successfully!', 'success');
//                 this.refreshStats();
//             }
//         } catch (error) {
//             console.error('Clear history error:', error);
//             this.showMessage('❌ Failed to clear history', 'error');
//         }
//     }

//     async exportStats() {
//         try {
//             const response = await this.makeApiRequest('/stats');
//             const dataStr = JSON.stringify(response, null, 2);
//             const timestamp = new Date().toISOString().slice(0, 19).replace(/[:.]/g, '-');
//             const filename = `encryption-stats-${timestamp}.json`;
            
//             this.downloadTextFile(dataStr, filename);
//             this.showMessage(`📊 Statistics exported as ${filename}`, 'success');
//         } catch (error) {
//             console.error('Export error:', error);
//             this.showMessage('❌ Failed to export statistics', 'error');
//         }
//     }

//     // Advanced settings
//     toggleAdvancedSettings() {
//         const settings = document.querySelector('.advanced-settings');
//         const isExpanded = settings?.classList.contains('expanded');
        
//         settings?.classList.toggle('expanded');
        
//         if (this.elements.settingsToggleIcon) {
//             this.elements.settingsToggleIcon.textContent = isExpanded ? '▼' : '▲';
//         }
//     }

//     updateKeyLengthDisplay() {
//         const length = this.elements.keyLength?.value || 16;
//         if (this.elements.keyLengthDisplay) {
//             this.elements.keyLengthDisplay.textContent = `${length} characters`;
//         }
//     }

//     // Password visibility toggle
//     togglePasswordVisibility() {
//         const passwordField = this.elements.passwordInput;
//         const toggleIcon = this.elements.passwordToggleIcon;
        
//         if (!passwordField || !toggleIcon) return;

//         const isPassword = passwordField.type === 'password';
//         passwordField.type = isPassword ? 'text' : 'password';
//         toggleIcon.textContent = isPassword ? '🙈' : '👁️';
//     }

//     // Keyboard shortcuts
//     handleKeyboardShortcuts(event) {
//         // Ctrl/Cmd + Enter: Process text
//         if ((event.ctrlKey || event.metaKey) && event.key === 'Enter') {
//             event.preventDefault();
//             this.processText();
//         }
        
//         // Ctrl/Cmd + K: Generate key
//         if ((event.ctrlKey || event.metaKey) && event.key === 'k') {
//             event.preventDefault();
//             this.generateSecureKey();
//         }
        
//         // Ctrl/Cmd + C: Copy result (when result is focused)
//         if ((event.ctrlKey || event.metaKey) && event.key === 'c' && 
//             document.activeElement === this.elements.resultText) {
//             event.preventDefault();
//             this.copyResult();
//         }
        
//         // Escape: Clear messages
//         if (event.key === 'Escape') {
//             this.clearMessages();
//         }
//     }

//     // Uptime counter
//     startUptimeCounter() {
//         setInterval(() => {
//             this.updateUptime();
//         }, 1000);
//     }

//     updateUptime() {
//         if (!this.elements.uptime) return;
        
//         const startTime = sessionStorage.getItem('appStartTime') || Date.now();
//         if (!sessionStorage.getItem('appStartTime')) {
//             sessionStorage.setItem('appStartTime', startTime);
//         }
        
//         const uptime = Date.now() - parseInt(startTime);
//         const hours = Math.floor(uptime / 3600000);
//         const minutes = Math.floor((uptime % 3600000) / 60000);
//         const seconds = Math.floor((uptime % 60000) / 1000);
        
//         this.elements.uptime.textContent = 
//             `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
//     }

//     // Message system
//     showMessage(text, type = 'info', duration = 4000) {
//         if (!this.elements.messageContainer) return;

//         const messageId = 'msg_' + Date.now();
//         const messageElement = document.createElement('div');
//         messageElement.className = `message ${type}`;
//         messageElement.id = messageId;
//         messageElement.innerHTML = `
//             <span>${text}</span>
//             <button onclick="document.getElementById('${messageId}').remove()" style="background:none;border:none;color:inherit;float:right;cursor:pointer;font-size:1.2em;padding:0 0 0 10px;">&times;</button>
//         `;

//         this.elements.messageContainer.appendChild(messageElement);

//         // Auto-remove after duration
//         setTimeout(() => {
//             const msg = document.getElementById(messageId);
//             if (msg) {
//                 msg.style.opacity = '0';
//                 msg.style.transform = 'translateX(-20px)';
//                 setTimeout(() => msg.remove(), 300);
//             }
//         }, duration);

//         // Limit number of messages
//         const messages = this.elements.messageContainer.children;
//         if (messages.length > 3) {
//             messages[0].remove();
//         }
//     }

//     clearResults() {
//         if (this.elements.resultText) {
//             this.elements.resultText.value = '';
//         }
//         this.clearMessages();
//     }

//     clearMessages() {
//         if (this.elements.messageContainer) {
//             this.elements.messageContainer.innerHTML = '';
//         }
//     }

//     // API request helper
//     async makeApiRequest(url, options = {}) {
//         const defaultOptions = {
//             method: 'GET',
//             headers: {
//                 'Content-Type': 'application/json',
//             },
//         };

//         const mergedOptions = { ...defaultOptions, ...options };

//         try {
//             const response = await fetch(url, mergedOptions);
            
//             if (!response.ok) {
//                 const errorText = await response.text();
//                 throw new Error(`HTTP ${response.status}: ${errorText}`);
//             }

//             return await response.json();
//         } catch (error) {
//             if (error.name === 'TypeError' && error.message.includes('fetch')) {
//                 throw new Error('Network error. Please check your connection.');
//             }
//             throw error;
//         }
//     }

//     // Visibility change handler
//     handleVisibilityChange() {
//         if (document.hidden) {
//             // Page is hidden, pause auto-refresh
//             if (this.statsRefreshInterval) {
//                 clearInterval(this.statsRefreshInterval);
//                 this.statsRefreshInterval = null;
//             }
//         } else {
//             // Page is visible, resume auto-refresh if enabled
//             if (this.elements.autoRefresh?.checked) {
//                 this.toggleAutoRefresh(true);
//             }
//         }
//     }

//     // Cleanup
//     cleanup() {
//         if (this.statsRefreshInterval) {
//             clearInterval(this.statsRefreshInterval);
//         }
        
//         this.debounceTimers.forEach(timer => clearTimeout(timer));
//         this.debounceTimers.clear();
//     }
// }

// // Global functions for HTML onclick handlers
// let encrypterApp;

// function initializeApp() {
//     encrypterApp = new TextEncrypter();
// }

// function switchMode(mode) {
//     encrypterApp?.switchMode(mode);
// }

// function handleAlgorithmChange() {
//     encrypterApp?.handleAlgorithmChange();
// }

// function processText() {
//     encrypterApp?.processText();
// }

// function generateSecureKey() {
//     encrypterApp?.generateSecureKey();
// }

// function clearInput() {
//     encrypterApp?.clearInput();
// }

// function pasteFromClipboard() {
//     encrypterApp?.pasteFromClipboard();
// }

// function copyResult() {
//     encrypterApp?.copyResult();
// }

// function swapTexts() {
//     encrypterApp?.swapTexts();
// }

// function downloadResult() {
//     encrypterApp?.downloadResult();
// }

// function shareResult() {
//     encrypterApp?.shareResult();
// }

// function refreshStats() {
//     encrypterApp?.refreshStats();
// }

// function clearHistory() {
//     encrypterApp?.clearHistory();
// }

// function exportStats() {
//     encrypterApp?.exportStats();
// }

// function toggleAdvancedSettings() {
//     encrypterApp?.toggleAdvancedSettings();
// }

// function updateKeyLengthDisplay() {
//     encrypterApp?.updateKeyLengthDisplay();
// }

// function togglePasswordVisibility() {
//     encrypterApp?.togglePasswordVisibility();
// }

// // Service Worker registration for PWA capabilities
// if ('serviceWorker' in navigator) {
//     window.addEventListener('load', () => {
//         navigator.serviceWorker.register('/sw.js')
//             .then(registration => {
//                 console.log('SW registered: ', registration);
//             })
//             .catch(registrationError => {
//                 console.log('SW registration failed: ', registrationError);
//             });
//     });
// }

// // Error handling for unhandled promises
// window.addEventListener('unhandledrejection', event => {
//     console.error('Unhandled promise rejection:', event.reason);
    
//     if (encrypterApp) {
//         encrypterApp.showMessage('An unexpected error occurred. Please try again.', 'error');
//     }
    
//     event.preventDefault();
// });

// // Performance monitoring
// if (typeof performance !== 'undefined' && performance.mark) {
//     performance.mark('app-start');
    
//     window.addEventListener('load', () => {
//         performance.mark('app-loaded');
//         performance.measure('app-load-time', 'app-start', 'app-loaded');
        
//         const loadTime = performance.getEntriesByName('app-load-time')[0];
//         console.log(`App loaded in ${loadTime.duration.toFixed(2)}ms`);
//     });
// }

// // Export for module usage
// if (typeof module !== 'undefined' && module.exports) {
//     module.exports = TextEncrypter;
// }