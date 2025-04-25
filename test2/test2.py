import tkinter as tk
import webbrowser
import time
from tkinter import messagebox
import googlemaps
from flask import Flask, render_template_string, request
from threading import Thread
from dotenv import load_dotenv
import os

load_dotenv()
############# FLASK IMPLEMENTATION ###########
location_data = {"lat": None, "lng": None}

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
        <html>
        <body onload="getLocation()">
            <script>
                function getLocation() {
                    navigator.geolocation.getCurrentPosition(function(pos) {
                        fetch('/location', {
                            method: 'POST',
                            headers: {'Content-Type': 'application/json'},
                            body: JSON.stringify({
                                lat: pos.coords.latitude,
                                lng: pos.coords.longitude
                            })
                        }).then(() => window.close());
                    });
                }
            </script>
            <p>Getting location...</p>
        </body>
        </html>
    ''')

@app.route('/location', methods=['POST'])
def get_location():
    data = request.get_json()
    location_data['lat'] = data['lat']
    location_data['lng'] = data['lng']
    return '', 200

def run_flask():
    app.run(port=5000)

###################### MAIN APPLICATION ######################
# Start Flask server in a thread
flask_thread = Thread(target=run_flask)
flask_thread.daemon = True
flask_thread.start()

api_key = os.getenv("API_KEY")
gmaps = googlemaps.Client(key=api_key)

def reverse_geocode(lat, lng):
    result = gmaps.reverse_geocode((lat, lng))
    return result[0]['formatted_address']

def on_button_click():
    # Open browser to get location
    webbrowser.open("http://127.0.0.1:5000")
    
    # Wait for location to be received (or timeout after 10 seconds)
    for _ in range(20):
        if location_data['lat'] is not None:
            break
        time.sleep(0.5)

    if location_data['lat'] is not None:
        lat = location_data['lat']
        lng = location_data['lng']
        address = reverse_geocode(lat, lng)
        coordLabel.config(text=f"Location: {address}\n Coordinates: {lat} {lng}")
    else:
        messagebox.showerror("Error", "Failed to get location from browser.")

# Tkinter GUI
root = tk.Tk()
root.title("Accurate Location App")
root.geometry("300x200")

button = tk.Button(root, text="Get Location", command=on_button_click)
button.pack(pady=50)

coordLabel = tk.Label(root, text="Location:")
coordLabel.pack()

root.mainloop()


