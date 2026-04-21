import tkinter as tk
from tkinter import ttk
from googleapiclient.discovery import build
import csv
import threading
import re

API_KEY = "your_API_KEY"
youtube = build("youtube", "v3", developerKey=API_KEY)


# ========== ????ID ==========
def extract_video_id(text):
    match = re.search(r"v=([a-zA-Z0-9_-]{11})", text)
    if match:
        return match.group(1)
    return text.strip()


# ========== ??? ==========
def fetch_comments(video_id, callback):
    comments = []
    next_page_token = None
    count = 0

    while True:
        response = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=100,
            pageToken=next_page_token,
            textFormat="plainText"
        ).execute()

        for item in response["items"]:
            text = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            comments.append(text)
            count += 1

            callback(f"???: {count}")

        next_page_token = response.get("nextPageToken")
        if not next_page_token:
            break

    return comments


# ========== ???? ==========
def start():
    url = entry.get().strip()
    video_id = extract_video_id(url)

    listbox.delete(0, tk.END)
    status_label.config(text="????...")

    def run_task():
        try:
            comments = fetch_comments(video_id, update_status)

            # ?????
            for c in comments:
                listbox.insert(tk.END, c)

            # ??CSV
            with open(f"comments_{video_id}.csv", "w", newline="", encoding="utf-8-sig") as f:
                writer = csv.writer(f)
                writer.writerow(["Comment"])
                for c in comments:
                    writer.writerow([c])

            status_label.config(text=f"???? {len(comments)} ???")

        except Exception as e:
            status_label.config(text=f"??: {e}")

    threading.Thread(target=run_task).start()


def update_status(text):
    status_label.config(text=text)


# ========== UI ==========
root = tk.Tk()
root.title("YouTube???????")
root.geometry("700x500")

tk.Label(root, text="?? YouTube ??? Video ID").pack()

entry = tk.Entry(root, width=80)
entry.pack()

tk.Button(root, text="????", command=start).pack(pady=5)

status_label = tk.Label(root, text="")
status_label.pack()

frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

scroll = tk.Scrollbar(frame)
scroll.pack(side="right", fill="y")

listbox = tk.Listbox(frame, yscrollcommand=scroll.set, width=100, height=25)
listbox.pack(side="left", fill="both", expand=True)

scroll.config(command=listbox.yview)

root.mainloop()
