const recordButton = document.getElementById("record-button");
const containersCircle = document.getElementsByClassName("container-circle");
const seconds = document.getElementById("seconds");
const iconFileAudio = document.getElementsByClassName("fa-file-audio")[0]

recordButton.addEventListener("click", startRecording);

function startRecording() {
    const iconMicrophone = recordButton.firstChild;
    iconMicrophone.style.color = 'red';

    let xhr = new XMLHttpRequest();
    xhr.onloadend = function (e) {
         for(let item of containersCircle){
                item.style.display = "none";
        }
        if (this.status === 200) {
            responseData = JSON.parse(e.target.responseText);
            Swal.fire({
                title: 'Song recognized!',
                text: 'The song name is ' + responseData["song_name"],
                type: 'info',
                confirmButtonText: 'Ok'
            }).then(() => {
                setTimeout(function () {
                     for(let item of containersCircle){
                        item.style.display = "block";
                     }
                     iconMicrophone.style.color = '#fff';
                }, 500);
            });
        }
        else {
            Swal.fire({
                title: 'Song couldn\'t be recognized!',
                text: 'The song it\'s not in database',
                type: 'error',
                confirmButtonText: 'Ok'
            }).then(() => {
                setTimeout(function () {
                     for(let item of containersCircle){
                        item.style.display = "block";
                     }
                     iconMicrophone.style.color = '#fff';
                }, 500);
            });
        }
    };
    xhr.open("GET", "/recognize-song-by-mic?seconds=" + seconds.options[seconds.selectedIndex].value, true);
    xhr.send();
}

function readSongURL(input){
     if (input.files && input.files[0]) {
          let reader = new FileReader();

          reader.onload = function (e){
             iconFileAudio.style.color = "red";
          };

          reader.readAsDataURL(input.files[0]);
      }
}
