import subprocess

applescript = """
display dialog "Differences\n\nx: |0.3-0.40121| = 0.10121\n\ny: |0.28 - 0.585938| = 0.305938\n\nRate of Change: 3.0228" ¬
with title "Ruler Tool" ¬
with icon caution ¬
buttons {"OK"}
"""

# This call is for Messagebox in Mac OS
subprocess.call("osascript -e '{}'".format(applescript), shell=True)