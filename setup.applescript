tell application "iTerm"
    activate
    -- Launch python Application
    tell application "System Events" to keystroke "python run.py"
    tell application "System Events" to keystroke return
    -- New Tab for listener
    tell application "System Events" to keystroke "t" using command down
    delay 0.5
    -- Launch Webhook Listener
    tell application "System Events" to keystroke "bash launch_listener.sh"
    tell application "System Events" to keystroke return
     -- New Tab for poster
    tell application "System Events" to keystroke "t" using command down
    delay 0.5
    -- Throw a sample post after a delay
    tell application "System Events" to keystroke "bash example_hook.sh"
    tell application "System Events" to keystroke return
    -- cmd left arrow twice so we're back on python to watch the magic
    tell application "System Events" to keystroke (ASCII character 28) using command down
    tell application "System Events" to keystroke (ASCII character 28) using command down
end tell