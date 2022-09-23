v = "aiueoAIUEO"
w = input("")
for hur in w:
    if(hur in v):
        w = w.replace(hur, "")
print(w)