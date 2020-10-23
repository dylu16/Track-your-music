// https://pqina.nl/blog/async-form-posts-with-a-couple-lines-of-vanilla-javascript/

const formUploadSong = document.getElementById("form-add-song");

const playlist_table = $('#playlist-table').DataTable( {
    "responsive" : true,
    "processing" : true,
    "serverSide": true,
    "orderMulti": false,
    "ajax": {
        "url": "/app/load-data-playlist"
    },
    "columns" : [
        { "data" : "song_name", "name" : "Song name" },
        { "data" : "total_hashes", "name" : "Total hashes" },
        { "data" : "date_created", "name" : "Date created"},
        { "data" : "date_modified", "name" : "Date modified" },
        { "data" : "Actions"}
    ],
    "columnDefs": [{
        "targets": -1,
        "className": "actions dt-body-center",
        render: function (data, type, row, meta) {
            return '<i class=\"fa fa-trash remove-song\" data-id=\"' + row["song_id"] + '\"></i>'
        },
        "orderable": false
    }]
});

$(document).delegate('.remove-song','click',function(){
    Swal.fire({
      title: 'Please confirm',
      text: "Are you sure you want to remove this song?",
      type: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#d33',
      cancelButtonColor: '#3085d6',
      cancelButtonText: 'No',
      confirmButtonText: 'Yes'
    }).then((result) => {
        if (result.value) {
            $.ajax({
                type: "DELETE",
                url: "/app/remove-song/" + $(this).attr("data-id"),
                success: function () {
                    Swal.fire({
                        text: "Song was removed successfully!",
                        type: 'success'
                    }).then(() => {
                       playlist_table
                        .row( $(this).parents('tr') )
                        .remove()
                        .draw();
                    });
                },
                error: function(){
                    Swal.fire({
                        text: "Song couldn't be removed!",
                        type: 'error'
                    })
                }
            });
        }
    });
});

function readSongURL(input){
     if (input.files && input.files[0]) {
          let reader = new FileReader();

          reader.onload = function (e){
              formUploadSong.submit();
          };

          reader.readAsDataURL(input.files[0]);
      }
}
