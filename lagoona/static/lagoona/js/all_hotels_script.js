(function (){
    function changeStarSize() {
        let stars = document.querySelectorAll('.hotel-rate-star')
        stars.forEach((e) => {
            e.style.width = '20px'
        })
        let blockStars = document.querySelectorAll('.hotel-rate')
        blockStars.forEach( (e) => {
            e.style.marginBottom = '20px'
        })
    };

    addEventListener("DOMContentLoaded", function (){

        changeStarSize()
    });
})();