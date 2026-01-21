import os

# 1. Ask for inputs
print("\n🐍 New Python Problem Entry")
print("-" * 30)
name = input("Problem Name (e.g. Codeforces 1903A - Halloumi Boxes): ").strip()
link = input("Problem Link: ").strip()

# ======================================================
# CRITICAL FIX: The marker CANNOT be empty.
# It must match the HTML comment in your file exactly.
# ======================================================
marker = "[a new problem to be inserted here]"

html_block = f"""
        <section class="cp-problem">
            <h3><a href="{link}" target="_blank">{name}</a></h3>
            
            <div class="problem-description">
                <strong>Insight:</strong> 
                Write your insight here...
            </div>

            <details>
                <summary>View Solution</summary>
                <div class="code-block">
<pre><code>
# TODO: Paste your Python code here
def solve():
    pass
</code></pre>
                </div>
            </details>
        </section>

        {marker}"""

# 3. Inject into cp.html
file_path = "cp.html"

if not os.path.exists(file_path):
    print("❌ Error: cp.html not found! Please create the file first.")
    exit()

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# SAFETY CHECK: If marker is missing, STOP. Don't destroy the file.
if marker not in content:
    print(f"❌ Error: The marker '{marker}' was not found in cp.html.")
    print("Please make sure is inside the file.")
    exit()

# This replaces the marker with [New Problem] + [Marker]
new_content = content.replace(marker, html_block)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"✅ Success! Added '{name}' to cp.html")