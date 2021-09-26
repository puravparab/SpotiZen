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

		let grandparentDiv = document.createElement("div");
		grandparentDiv.className = 'largerTrackContainer';
		let parentDiv = document.createElement("div");
		parentDiv.className = 'trackContainer';

		let hIndex = document.createElement("h3");
		hIndex.className = 'index';
		let textIndex = document.createTextNode(index + 1);
		hIndex.appendChild(textIndex);
		parentDiv.appendChild(hIndex);

		let img = document.createElement("img");
		img.src = data[index].image;
		parentDiv.appendChild(img);

		let trackData = document.createElement("div");
		trackData.className = 'trackData';

		let hTrack = document.createElement("h3");
		hTrack.className = 'trackName';
		let textTrack = document.createTextNode(trackString);
		hTrack.appendChild(textTrack);

		let hArtists = document.createElement("h3");
		hArtists.className = 'artistsName';
		let textArtists = document.createTextNode(artistsString);
		hArtists.appendChild(textArtists);

		trackData.appendChild(hTrack);
		trackData.appendChild(hArtists);
		parentDiv.appendChild(trackData);

		let preview = document.createElement("a")
		preview.href = data[index].preview;
		let link = document.createTextNode("Preview");
		preview.appendChild(link);

		parentDiv.appendChild(preview);
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
		let str = (index+1) + ": " + data[index].name;

		let newDiv = document.createElement("div")
		let h = document.createElement("h3");
		let text = document.createTextNode(str);
		h.appendChild(text);

		let img = document.createElement("img");
		img.src = data[index].image;

		newDiv.appendChild(h);
		newDiv.appendChild(img);
		artist.appendChild(newDiv);

		index += 1;
	}

}