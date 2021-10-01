const executeApiRequest = async (url) => {
	let data = await fetch(url);
	let dataJson = await data.json();
	return dataJson;
}

// Functions for Top Tracks 
export const getTopTracksList = async (url) => {
	let data = await executeApiRequest(url);
	let track = document.getElementById('track');

	// Remove Existing List
	let child = track.getElementsByTagName('*')
	if(child.length !== 0){
		while(child.length !== 0){
			track.removeChild(child[0])
		}
	}

	// Create New List
	let index = 0;
	for (let i in data){
		let trackString = data[index].name;
		let artistsString = data[index].artists;
		let previewUrl = data[index].preview;

		let grandparentDiv = document.createElement("div");
		grandparentDiv.className = 'largerTrackContainer';
		let parentDiv = document.createElement("div");
		parentDiv.className = 'trackContainer';

		// Create Index
		let hIndex = document.createElement("h3");
		hIndex.className = 'index';
		let textIndex = document.createTextNode(index + 1);
		hIndex.appendChild(textIndex);
		parentDiv.appendChild(hIndex);

		// Create Cover Image
		let img = document.createElement("img");
		img.src = data[index].image;
		// Play the track preview when user hovers over track cover
		img.addEventListener("mouseenter", ()=>{
			var audio = new Audio(previewUrl);
			img.style.border = "2px solid green";
			audio.play()
			img.addEventListener("mouseleave", ()=>{
				audio.pause();
				img.style.border = "";
			});
		});
		parentDiv.appendChild(img);

		// Create Track Details
		let trackData = document.createElement("div");
		trackData.className = 'trackData';

		// Add Track Name
		let hTrack = document.createElement("h3");
		hTrack.className = 'trackName';
		let textTrack = document.createTextNode(trackString);
		hTrack.appendChild(textTrack);

		// Add Track Artist
		let hArtists = document.createElement("h3");
		hArtists.className = 'artistsName';
		let textArtists = document.createTextNode(artistsString);
		hArtists.appendChild(textArtists);

		trackData.appendChild(hTrack);
		trackData.appendChild(hArtists);
		parentDiv.appendChild(trackData);

		// Song Preview
		let preview = document.createElement("a")
		preview.href = data[index].preview;
		preview.target = "_blank"
		let link = document.createTextNode("Preview");
		preview.appendChild(link);
		// parentDiv.appendChild(preview);

		// Create a track entry
		grandparentDiv.appendChild(parentDiv);

		track.appendChild(grandparentDiv);

		index += 1;
	}
}

// Functions for Top Artists
export const getTopArtistsList = async (url) => {
	let data = await executeApiRequest(url);
	let artist = document.getElementById('artist');

	// Remove Existing List
	let child = artist.getElementsByTagName('*')
	if(child.length !== 0){
		while(child.length !== 0){
			artist.removeChild(child[0])
		}
	}

	// Create New List
	let index = 0;
	for (let i in data){
		let artistString = data[index].name;

		let grandparentDiv = document.createElement("div");
		grandparentDiv.className = 'largerArtistContainer';
		let parentDiv = document.createElement("div");
		parentDiv.className = 'artistContainer';

		let hIndex = document.createElement("h3");
		hIndex.className = 'index';
		let textIndex = document.createTextNode(index + 1);
		hIndex.appendChild(textIndex);
		parentDiv.appendChild(hIndex);

		let img = document.createElement("img");
		img.src = data[index].image;
		parentDiv.appendChild(img);

		let hArtist = document.createElement("h3");
		hArtist.className = 'artistName';
		let textArtist = document.createTextNode(artistString);
		hArtist.appendChild(textArtist);

		parentDiv.appendChild(hArtist);
		grandparentDiv.appendChild(parentDiv);
		artist.appendChild(grandparentDiv);

		index += 1;
	}
}
