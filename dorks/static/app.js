function openNav() {
  document.getElementById("bar").style.width = "250px";
}

function closeNav() {
  document.getElementById("bar").style.width = "0";
}

function generateGoogleDork(){
    alert('Generate Google Dork');
    var dork='';
    var domain = document.getElementById('inputdomain');
    if(domain.value != ''){
        console.log('domain '+domain.value);
        dork=dork+'( domain: ' +domain.value+' )';
    }
    var literal = document.getElementById('inputliteral1');
    if(literal.value != ''){
        console.log('literal '+literal.value);
        dork=dork+'( allintext:"' +literal.value+'" )';
    }

    var title = document.getElementById('inputintitle');
     if(title.value != ''){
        console.log('title '+title.value);
        dork=dork+'( intitle: "' +title.value+'" )';
    }
    var url = document.getElementById('inputurl');
     if(url.value != ''){
        console.log('url '+url.value);
        dork=dork+'( url: "' +url.value+'" )';
    }
    var body = document.getElementById('inputbody');
    if(body.value != ''){
        console.log('body '+body.value);
        dork=dork+'( allintext: "' +body.value+'" )';
    }
    var filetype = document.getElementById('inputfiletype');
    if(filetype.value != '' && filetype.value != 'Choose...' ){
        console.log('filetype '+filetype.value);
        dork=dork+'( filetype: "' +filetype.value+'" ) ';
    }
    var exclude = document.getElementById('inputexclude');
    if(exclude.value != ''){
        console.log('exclude '+exclude.value);
        dork=dork+' ( -' +literal.value+' ) ';
    }
    var and = document.getElementById('inputand');
    if(and.value != ''){
        console.log('and '+and.value);
        dork=dork+'and ( "' +and.value+'" ) ';
    }
    var or = document.getElementById('inputor');
    if(or.value != ''){
        console.log('or '+or.value);
        dork=dork+'or ( "' +or.value+'" ) ';
    }
    var ip = document.getElementById('inputip');
    if(ip.value != ''){
        console.log('ip '+ip.value);
        dork=dork+' ( ip: ' +ip.value+' ) ';
    }
    var rss = document.getElementById('inputrss');
    if(rss.value != ''){
        console.log('rss '+rss.value);
        dork=dork+' ( rss: "' +rss.value+'" ) ';
    }
    var date = document.getElementById('inputdate');
    if(date.value != '' && date.value!='Choose...'){
        console.log('date '+date.value);
        dork=dork+' ( date: "' +date.value+'" ) ';
    }
    var hack = document.getElementById('dorSelect');
    if(hack.value != '' && hack.value !='Choose...'){
        console.log('dorSelect '+hack.value);
        dork=dork+' '+hack.value+'';
    }

    document.getElementById('inputcommand').value=dork;
}