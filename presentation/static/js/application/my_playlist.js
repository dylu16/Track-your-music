gapi.load("client", loadClient);
 
function loadClient() {
    gapi.client.setApiKey("AIzaSyA-6BPyjOWdd68coRBBznwGfQDc7wU13mI");
    return gapi.client.load("https://www.googleapis.com/discovery/v1/apis/youtube/v3/rest")
        .then(function() { console.log("GAPI client loaded for API"); },
                function(err) { console.error("Error loading GAPI client for API", err); });
}

setTimeout(
    function () {
        searchPlaylistSongs();
        },
1000);

const videoList = document.getElementById('videoListContainer');

function searchPlaylistSongs(){
    playlistSongs.forEach(playlistSong => {
        //exampleSearchSong();
        searchSong(playlistSong);
    });
}

function exampleSearchSong() {
        const listItems = [
            {
                etag: "ff6iCw_uM3HPJNkAlhwHzfVaJ2o",
                id: {
                    kind: "youtube#video",
                    videoId: "8UVNT4wvIGY"
                },
                kind: "youtube#searchResult",
                snippet: {
                    publishedAt: "2011-07-05T21:29:29Z",
                    channelId: "UCFC9LamNMmLioW643VZ40OA",
                    title: "Gotye - Somebody That I Used To Know (feat. Kimbra) - official music video",
                    description: "From the album Making Mirrors Official Gotye Store…its: Directed, produced and edited by Natasha ...",
                    thumbnails: {
                        default: {url: "https://i.ytimg.com/vi/8UVNT4wvIGY/default.jpg", width: 120, height: 90},
                        high: {url: "https://i.ytimg.com/vi/8UVNT4wvIGY/hqdefault.jpg", width: 480, height: 360},
                        medium: {url: "https://i.ytimg.com/vi/8UVNT4wvIGY/mqdefault.jpg", width: 320, height: 180}
                    }
                }
            },
            {
                etag: "ff6iCw_uM3HPJNkAlhwHzfVaJ2o",
                id: {
                    kind: "youtube#video",
                    videoId: "8DyziWtkfBw"
                },
                kind: "youtube#searchResult",
                snippet: {
                    publishedAt: "2011-07-05T21:29:29Z",
                    channelId: "UCFC9LamNMmLioW643VZ40OA",
                    title: "Gotye - Somebody That I Used To Know (feat. Kimbra) - official music video",
                    description: "From the album Making Mirrors Official Gotye Store…its: Directed, produced and edited by Natasha ...",
                    thumbnails: {
                        default: {url: "https://i.ytimg.com/vi/8UVNT4wvIGY/default.jpg", width: 120, height: 90},
                        high: {url: "https://i.ytimg.com/vi/8UVNT4wvIGY/hqdefault.jpg", width: 480, height: 360},
                        medium: {url: "https://i.ytimg.com/vi/8UVNT4wvIGY/mqdefault.jpg", width: 320, height: 180}
                    }
                }
            },{
                etag: "ff6iCw_uM3HPJNkAlhwHzfVaJ2o",
                id: {
                    kind: "youtube#video",
                    videoId: "8UVNT4wvIGY"
                },
                kind: "youtube#searchResult",
                snippet: {
                    publishedAt: "2011-07-05T21:29:29Z",
                    channelId: "UCFC9LamNMmLioW643VZ40OA",
                    title: "Gotye - Somebody That I Used To Know (feat. Kimbra) - official music video",
                    description: "From the album Making Mirrors Official Gotye Store…its: Directed, produced and edited by Natasha ...",
                    thumbnails: {
                        default: {url: "https://i.ytimg.com/vi/8UVNT4wvIGY/default.jpg", width: 120, height: 90},
                        high: {url: "https://i.ytimg.com/vi/8UVNT4wvIGY/hqdefault.jpg", width: 480, height: 360},
                        medium: {url: "https://i.ytimg.com/vi/8UVNT4wvIGY/mqdefault.jpg", width: 320, height: 180}
                    }
                }
            },{
                etag: "ff6iCw_uM3HPJNkAlhwHzfVaJ2o",
                id: {
                    kind: "youtube#video",
                    videoId: "8UVNT4wvIGY"
                },
                kind: "youtube#searchResult",
                snippet: {
                    publishedAt: "2011-07-05T21:29:29Z",
                    channelId: "UCFC9LamNMmLioW643VZ40OA",
                    title: "Gotye - Somebody That I Used To Know (feat. Kimbra) - official music video",
                    description: "From the album Making Mirrors Official Gotye Store…its: Directed, produced and edited by Natasha ...",
                    thumbnails: {
                        default: {url: "https://i.ytimg.com/vi/8UVNT4wvIGY/default.jpg", width: 120, height: 90},
                        high: {url: "https://i.ytimg.com/vi/8UVNT4wvIGY/hqdefault.jpg", width: 480, height: 360},
                        medium: {url: "https://i.ytimg.com/vi/8UVNT4wvIGY/mqdefault.jpg", width: 320, height: 180}
                    }
                }
            }];

        if (listItems) {

            listItems.forEach(item => {
                console.log(item);

                const videoId = item.id.videoId;
                const videoTitle = item.snippet.title;

                const sectionVideo = document.createElement('section');

                sectionVideo.innerHTML = `
					<iframe width="500" height="315" src="https://www.youtube.com/embed/${videoId}" 
					frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
				`
                videoList.appendChild(sectionVideo);
            });
        }
}

function searchSong(songName) {
    console.log(songName);

    const arr_search = {
        "part": 'snippet',
        "type": 'video',
        "maxResults": 1,
        "q": songName
    };

    return gapi.client.youtube.search.list(arr_search)
    .then(function(response) {
        // Handle the results here (response.result has the parsed body).
        const listItems = response.result.items;

        if (listItems) {

            listItems.forEach(item => {
                console.log(item);

                const videoId = item.id.videoId;
                const videoTitle = item.snippet.title;

                const sectionVideo = document.createElement('section');

                sectionVideo.innerHTML = `
					<iframe width="500" height="315" src="https://www.youtube.com/embed/${videoId}" 
					frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
				`
                videoList.appendChild(sectionVideo);
            });
        }
    },
    function(err) { console.error("Execute error", err); });
}