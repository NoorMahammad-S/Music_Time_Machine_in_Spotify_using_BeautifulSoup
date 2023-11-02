# Music Time Machine in Spotify using BeautifulSoup

This Python script allows you to create a Spotify playlist of the Billboard Hot 100 songs for a specific date. You can specify the desired date in the format `YYYY-MM-DD`, 
and the script will scrape the Billboard Hot 100 chart for that date, search for the songs on Spotify, create a private playlist, and add the songs to the playlist.

## Prerequisites

Before using this script, you need to have the following:

1. Python installed on your system.
2. A Spotify Developer Account to obtain the client ID and client secret.
3. The `spotipy` library installed. You can install it using pip:

   ```
   pip install spotipy
   ```

## Getting Started

1. Clone this repository to your local machine:

   ```
   git clone https://github.com/NoorMahammad-S/music-time-machine.git
   ```

2. Navigate to the project directory:

   ```
   cd music-time-machine
   ```

3. Create a Spotify Developer Application:

   - Visit the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
   - Create a new application and note down the Client ID and Client Secret.

4. Set the environment variables for your Spotify credentials:

   You can set these variables in your shell or create a `.env` file in the project directory with the following content:

   ```
   export SPOTIPY_CLIENT_ID=your-client-id
   export SPOTIPY_CLIENT_SECRET=your-client-secret
   ```

   Make sure to replace `your-client-id` and `your-client-secret` with the actual values.

5. Run the script:

   ```
   python music_time_machine.py
   ```

6. Follow the script's instructions and input the date in `YYYY-MM-DD` format.

7. The script will create a private Spotify playlist with the Billboard Hot 100 songs for the specified date.

## Notes

- This script uses the Spotipy library to interact with the Spotify API. Ensure you have the required permissions to create playlists on your Spotify account.

- Remember to keep your Spotify credentials (Client ID and Client Secret) secure.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Feel free to fork, modify, and use this code in accordance with the license.

Happy listening!
