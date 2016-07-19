
function main(){
    initPageAnimation();
    initPageNavigation();
    initBackGroundImageRotator();
}

function initPageAnimation(){
    $("body").css("display", "none");
    $("body").fadeIn(2000);

    $("a").click(function(event){
        event.preventDefault();
        linkLocation = this.href;
        $("body").fadeOut(1000, redirectPage);
    });

    function redirectPage() {
        window.location = linkLocation;
    }
}

function initPageNavigation() {
    $(document).keydown(function(e) {
         switch(e.which) {
            case 40: // down
                linkLocation = firstPersonLink;
                $("body").fadeOut(1000, redirectPage);
                break;
            default:
                break;
            }
    });

    function redirectPage() {
        window.location = linkLocation;
    }
}

function initBackGroundImageRotator(){
    console.log("initBackGroundImageRotator");
    var InfiniteRotator = {
        init: function() {
            var initialFadeIn = 1000; //initial fade-in time (in ms)
            var itemInterval = 5000; //interval between items (in ms)
            var fadeTime = 2500; //cross-fade time (in milliseconds)
            var numberOfItems = images.length; //count number of items
            var currentItem = 0;

            $('body').css("background-image", "url(" + images[0] + ")");

            var infiniteLoop = setInterval(function(){ //loop through the items
                if(currentItem == numberOfItems - 1){
                    currentItem = 0;
                }else {
                    currentItem++;
                }
                $('body').css("background-image", "url(" + images[currentItem] + ")");
            }, itemInterval);
        }
    };
    InfiniteRotator.init();
}

$(document).ready(main);
