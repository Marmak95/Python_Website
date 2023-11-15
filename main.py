from website import createApp

app = createApp()

# Must run this file to run the application
if __name__ == "__main__":
    # Reruns the code when modifying the code because of debug = True
    app.run(debug = True) 