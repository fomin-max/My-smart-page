$(document).ready(function() {


    var form = $('#form_search_news');
    var like = $('#form_like_news');
    var dislike = $('#form_dislike_news');
    var mycity = $('#mycity').data("city");
    var citynews = $('#citynews').data("citynews");
    var i=0;
    var j=1;
    var onefeed = "";

    // console.log(mycity);
    while (i!=citynews.length){
        onefeed = onefeed + citynews[i];
        i=i+1;
        if (citynews[i]=='\n'){break}
    }

    $('.items-first').append('<ui>'+onefeed+'</ui>');

    i=0;
    var first_feed = "";
    while (i!=mycity.length){
        first_feed = first_feed + mycity[i];
        i=i+1;
        if (mycity[i]=='\n'){break}
    }
    $('.first_feed').append('<ui id="myvar">'+first_feed+'</ui>');
    // $('.first_feed').a
    // var mylink = $('#mylink');
    // mylink.on('submit',function (e) {
    //     e.preventDefault();
    // };
    like.on('submit',function (e) {
        e.preventDefault();
        j=j+1;
        next_feed = get_likefeed(j);
        if (next_feed === undefined){
            j=0;
            next_feed = "Sorry, not found news in this category ;c";
        }
        $('.first_feed').empty();
        $('.first_feed').append('<ui id="myvar">'+next_feed+'</ui>');
    });
    // console.log(document.getElementById("myvar").innerHTML);
    i=0;
    var submit_btn3 = $('#submit_btn3');
    dislike.on('submit',function (e) {
        e.preventDefault();
        j=1;
        first_feed="";
        mycity=get_dislikefeed(mycity);

        $('.first_feed').empty();
        i=0;
        while (i!=mycity.length){
            first_feed = first_feed + mycity[i];
            i=i+1;
            if (mycity[i]=='\n'){break}
            }
        if (first_feed == "\n"){
            first_feed = "Sorry, no more news :c";
        }
        $('.first_feed').append('<ui id="myvar">'+first_feed+'</ui>');
    });
            // var submit_btn = $('#submit_btn');
    form.on('submit', function(e) {
        e.preventDefault();
        var input = $('#txt').val();
        $('#txt').val('');
        // var submit_btn = $('#submit_btn');
        // var news = submit_btn.data("pull");
        var final = "";
        var mystr = "";
        var i=0;
        var k=0;
        if (input.length < 3) {
            mystr = "Please enter more than 2 letters";
        }
        else{
            top:
            while (i!=citynews.length){
                while(citynews[i]!='\n'){
                    final = final + citynews[i];
                    i=i+1;
                    };
                if (final.includes(input) == true) {
                    k=k+1;
                    if(k>2){break top;}
                    mystr = mystr + final + '<br>';
                    }
                final = "";
                i=i+1;
                }
            if (mystr == "") {
                mystr = "We are not found news :c"
                }
        }
        $('.items-first').empty();
        $('.items-first').append('<ui>'+mystr+'</ui>');
    });



});

        function get_likefeed(n) {
            var i=0;
            var k=0;
            var mycity = $('#mycity').data("city");
            var first_feed = "";
            first_feed = document.getElementById("myvar").innerHTML;
            first_feed = first_feed.replace('\n','');
            i=0;
            // console.log(first_feed);
            var mystr="";
            var final="";
            var filter = "";
            k=first_feed.indexOf("Категория: ");
            while(k!=first_feed.length){
                mystr = mystr + first_feed[k];
                k=k+1;
                }
            k=0;
            i=0;
            while (i!=mycity.length){
                while(mycity[i]!='\n'){
                    final = final + mycity[i];
                    i=i+1;
                    };
                if (final.includes(mystr) == true) {
                    filter = filter + final + '\n';
                    }
                final = "";
                i=i+1;
                };

            // console.log(filter);
            i=0;
            k=0;
            result="";
            // console.log(n);
            while (i!=filter.length) {
                while (filter[i] != '\n') {
                    result = result + filter[i];
                    i = i + 1;
                }
                if (n == 1) {
                    return result
                }
                else {
                    n=n-1;
                    result="";
                }
                i=i+1;
            }
        // console.log(result);
        }

        function get_dislikefeed(mycity) {
            var i=0;
            var k=0;
            var first_feed = "";
            // while (i!=mycity.length){
            //     first_feed = first_feed + mycity[i];
            //     i=i+1;
            //     if (mycity[i]=='\n'){
            //         break
            //     }
            // }
            first_feed = document.getElementById("myvar").innerHTML;
            i=0;
            var mystr="";
            k=first_feed.indexOf("Категория: ");
            while(k!=first_feed.length){
                mystr = mystr + first_feed[k];
                k=k+1;
                }
            k=0;
            i=0;
            var final="";
            var pull=mycity;
            while (i!=mycity.length){
                while(mycity[i]!='\n'){
                    final = final + mycity[i];
                    i=i+1;
                    };
                if (final.includes(mystr) == true) {
                    pull = pull.replace(final,"");
                    pull = pull.replace('\n\n','\n');
                    };
                final = "";
                i=i+1;
                };
            return pull;
        }
