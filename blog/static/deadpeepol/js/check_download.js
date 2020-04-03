$(function(){
    $(document).on("click","#proceed_download",(event)=>{
        const proceed = confirm("Are you sure this the album you paid for?If you proceed to the wrong album you cannot go back.");
        if (proceed){
            return true
        }else{
            return false
        }
    })
})