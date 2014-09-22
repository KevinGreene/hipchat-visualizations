    var processResults = function(results) {
      console.log("Remote file parsed!", results);
      var data = results.data
      var resultsLength = data.length;
      for (var i = 0; i < resultsLength; i++) {
        row = data[i]
        setTimeout(makeCircle, parseInt(row[4] * 100), row[1]);
      }
    }

    Papa.parse("/hipchat.out", {
      download: true,
      complete: processResults
    });


    var parent, ink, d, x, y;

    var makeCircle = function(elementName) {
      element = $('#' + elementName);
      if (element.find(".drop").length === 0)
        element.prepend("<span class='drop'></span>");


      drop = element.find(".drop");
      drop.removeClass("animate");

      if (!drop.height() && !drop.width()) {
        d = Math.max(element.outerWidth(), element.outerHeight());
        drop.css({
          height: d,
          width: d
        });
      }

      x = 0
      y = 0

      //set the position and add class .animate
      drop.css({
        top: y + 'px',
        left: x + 'px'
      }).addClass("animate");
    };