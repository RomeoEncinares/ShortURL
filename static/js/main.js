const form = document.getElementById("url-form")

form.addEventListener('submit', e=>{
    $.ajax({
        type: "POST",
        url: "",
        data: {
            url:$('input[name="url"').val(),
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
          },
        success: function(response){
            console.log(response)
        },
        error: function(error){
            console.log(error)
        },
        cache: false, 
    })
})

const formDiv = document.getElementById("url-output")
formDiv.addEventListener("click",function(){
    const shorturl= document.getElementById("shorturl")
    navigator.clipboard.writeText(shorturl.value);
});