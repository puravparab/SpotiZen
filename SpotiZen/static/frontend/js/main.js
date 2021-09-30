import { getTopTracksList, getTopArtistsList} from './spotify.js'

// Home Page
var urlTracks = "http://192.168.1.101:8000/spotify/top-tracks"
var urlArtists = "http://192.168.1.101:8000/spotify/top-artists"

const trackbtn1 = document.querySelector(".track-btn-1")
const trackbtn2 = document.querySelector(".track-btn-2")
const trackbtn3 = document.querySelector(".track-btn-3")
const artistbtn1 = document.querySelector(".artist-btn-1")
const artistbtn2 = document.querySelector(".artist-btn-2")
const artistbtn3 = document.querySelector(".artist-btn-3")

getTopTracksList(urlTracks);
getTopArtistsList(urlArtists);

trackbtn1.addEventListener("click", () => {
	let url = urlTracks + "/short_term/50?format=json";
	getTopTracksList(url);
});

trackbtn2.addEventListener("click", () =>{
	let url = urlTracks + "/medium_term/50?format=json";
	getTopTracksList(url);
});

trackbtn3.addEventListener("click", () =>{
	let url = urlTracks + "/long_term/50?format=json";
	getTopTracksList(url);
});

artistbtn1.addEventListener("click", () =>{
	let url = urlArtists + "/short_term/50?format=json";
	getTopArtistsList(url);
});

artistbtn2.addEventListener("click", () =>{
	let url = urlArtists + "/medium_term/50?format=json";
	getTopArtistsList(url);
});

artistbtn3.addEventListener("click", () =>{
	let url = urlArtists + "/long_term/50?format=json";
	getTopArtistsList(url);
});