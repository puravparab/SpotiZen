const executeApiRequest = async (url) => {
	let data = await fetch(url);
	let dataJson = await data.json();
	return dataJson;
}

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
		let str = (index+1) + ": " + data[index].name 
					+ " - " + data[index].artists;
		// console.log(str);
		let h = document.createElement("h3");
		let text = document.createTextNode(str);
		h.appendChild(text);
		track.appendChild(h);

		index += 1;
	}

}

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
		// console.log(str);
		let h = document.createElement("h3");
		let text = document.createTextNode(str);
		h.appendChild(text);
		artist.appendChild(h);

		let img = document.createElement("img");
		img.src = data[index].image
		artist.appendChild(img);

		index += 1;
	}

}