# -*-coding:utf-8-*-
import re

s = '''
var SCREEN_DATA =
[
  {
    "data": {
      "Large": {
        "hdpi": "0.4",
        "ldpi": "0.1",
        "mdpi": "3.6",
        "tvdpi": "1.8",
        "xhdpi": "0.4"
      },
      "Normal": {
        "hdpi": "35.4",
        "mdpi": "2.3",
        "tvdpi": "0.2",
        "xhdpi": "34.3",
        "xxhdpi": "16.8"
      },
      "Small": {
        "ldpi": "1.1"
      },
      "Xlarge": {
        "hdpi": "0.5",
        "mdpi": "2.5",
        "xhdpi": "0.6"
      }
    },
    "densitychart": "//chart.googleapis.com/chart?chco=c4df9b%2C6fad0c&cht=p&chs=400x250&chl=ldpi%7Cmdpi%7Ctvdpi%7Chdpi%7Cxhdpi%7Cxxhdpi&chd=t%3A1.2%2C8.4%2C2.0%2C36.3%2C35.3%2C16.8&chf=bg%2Cs%2C00000000",
    "layoutchart": "//chart.googleapis.com/chart?chco=c4df9b%2C6fad0c&cht=p&chs=400x250&chl=Xlarge%7CLarge%7CNormal%7CSmall&chd=t%3A3.6%2C6.3%2C89.0%2C1.1&chf=bg%2Cs%2C00000000"
  }
];


var VERSION_DATA =
[
  {
    "chart": "//chart.googleapis.com/chart?chco=c4df9b%2C6fad0c&cht=p&chs=500x250&chl=Gingerbread%7CIce%20Cream%20Sandwich%7CJelly%20Bean%7CKitKat%7CLollipop%7CMarshmallow%7CNougat&chd=t%3A0.9%2C0.9%2C10.1%2C20.0%2C32.0%2C31.2%2C4.9&chf=bg%2Cs%2C00000000",
    "data": [
      {
        "api": 10,
        "name": "Gingerbread",
        "perc": "0.9"
      },
      {
        "api": 15,
        "name": "Ice Cream Sandwich",
        "perc": "0.9"
      },
      {
        "api": 16,
        "name": "Jelly Bean",
        "perc": "3.5"
      },
      {
        "api": 17,
        "name": "Jelly Bean",
        "perc": "5.1"
      },
      {
        "api": 18,
        "name": "Jelly Bean",
        "perc": "1.5"
      },
      {
        "api": 19,
        "name": "KitKat",
        "perc": "20.0"
      },
      {
        "api": 21,
        "name": "Lollipop",
        "perc": "9.0"
      },
      {
        "api": 22,
        "name": "Lollipop",
        "perc": "23.0"
      },
      {
        "api": 23,
        "name": "Marshmallow",
        "perc": "31.2"
      },
      {
        "api": 24,
        "name": "Nougat",
        "perc": "4.5"
      },
      {
        "api": 25,
        "name": "Nougat",
        "perc": "0.4"
      }
    ]
  }
];


var VERSION_NAMES =
[
  {"api":0},{"api":1},{"api":2},{"api":3},
  {
    "api":4,
    "link":'<a href="https://developer.android.google.cn/about/versions/android-1.6.html">1.6</a>',
    "codename":"Donut",
  },
  { "api":5},
  { "api":6},
  {
    "api":7,
    "link":'<a href="https://developer.android.google.cn/about/versions/android-2.1.html">2.1</a>',
    "codename":"Eclair",
  },
  {
    "api":8,
    "link":'<a href="https://developer.android.google.cn/about/versions/android-2.2.html">2.2</a>',
    "codename":"Froyo"
  },
  {
    "api":9,
    "link":'<a href="https://developer.android.google.cn/about/versions/android-2.3.html">2.3 -<br>2.3.2</a>',
    "codename":"Gingerbread"
  },
  {
    "api":10,
    "link":'<a href="https://developer.android.google.cn/about/versions/android-2.3.3.html">2.3.3 -<br>2.3.7</a>',
    "codename":"Gingerbread"
  },
  { "api":11},
  {
    "api":12,
    "link":'<a href="https://developer.android.google.cn/about/versions/android-3.1.html">3.1</a>',
    "codename":"Honeycomb"
  },
  {
    "api":13,
    "link":'<a href="https://developer.android.google.cn/about/versions/android-3.2.html">3.2</a>',
    "codename":"Honeycomb"
  },
  { "api":14},
  {
    "api":15,
    "link":'<a href="https://developer.android.google.cn/about/versions/android-4.0.html">4.0.3 -<br>4.0.4</a>',
    "codename":"Ice Cream Sandwich"
  },
  {
    "api":16,
    "link":'<a href="https://developer.android.google.cn/about/versions/android-4.1.html">4.1.x</a>',
    "codename":"Jelly Bean"
  },
  {
    "api":17,
    "link":'<a href="https://developer.android.google.cn/about/versions/android-4.2.html">4.2.x</a>',
    "codename":"Jelly Bean"
  },
  {
    "api":18,
    "link":'<a href="https://developer.android.google.cn/about/versions/android-4.3.html">4.3</a>',
    "codename":"Jelly Bean"
  },
  {
    "api":19,
    "link":'<a href="https://developer.android.google.cn/about/versions/android-4.4.html">4.4</a>',
    "codename":"KitKat"
  },
  {
    "api":20,
    "link":'<a href="https://developer.android.google.cn/about/versions/android-4.4.html">4.4W</a>',
    "codename":"KitKat for Wear"
  },
  {
    "api":21,
    "link":'<a href="https://developer.android.google.cn/about/versions/android-5.0.html">5.0</a>',
    "codename":"Lollipop"
  },
  {
    "api":22,
    "link":'<a href="https://developer.android.google.cn/about/versions/android-5.1.html">5.1</a>',
    "codename":"Lollipop"
  },
  {
    "api":23,
    "link":'<a href="https://developer.android.google.cn/about/versions/marshmallow/index.html">6.0</a>',
    "codename":"Marshmallow"
  },
  {
    "api":24,
    "link":'<a href="https://developer.android.google.cn/about/versions/nougat/index.html">7.0</a>',
    "codename":"Nougat"
  },
  {
    "api":25,
    "link":'<a href="https://developer.android.google.cn/about/versions/nougat/android-7.1.html">7.1</a>',
    "codename":"Nougat"
  }
];



$(document).ready(function(){
  // for each set of data (each month)
  $.each(VERSION_DATA, function(i, set) {

    // set up wrapper divs
    var $div = $('<div class="chart"'
         + ((i == 0) ? ' style="display:block"' : '')
         + ' >');
    var $divtable = $('<div class="col-5" style="margin-left:0">');
    var $divchart = $('<div class="col-8" style="margin-right:0">');

    // set up a new table
    var $table = $("<table>");
    var $trh = $("<tr><th>Version</th>"
                   + "<th>Codename</th>"
                   + "<th>API</th>"
                   + "<th>Distribution</th></tr>");
    $table.append($trh);

    // loop each data set (each api level represented in stats)
    $.each(set.data, function(i, data) {
      // check if we need to rowspan the codename
      var rowspan = 1;
      // must not be first row
      if (i > 0) {
        // if this row's codename is the same as previous row codename
        if (data.name == set.data[i-1].name) {
          rowspan = 0;
        // otherwise, as long as this is not the last row
        } else if (i < (set.data.length - 1)) {
          // increment rowspan for each subsequent row w/ same codename
          while (data.name == set.data[i+rowspan].name) {
            rowspan++;
            // unless we've reached the last row
            if ((i + rowspan) >= set.data.length) break;
          }
        }
      }

      // create table row and get corresponding version info from VERSION_NAMES
      var $tr = $("<tr>");
      $tr.append("<td>" + VERSION_NAMES[data.api].link + "</td>");
      if (rowspan > 0) {
        $tr.append("<td rowspan='" + rowspan + "'>" + VERSION_NAMES[data.api].codename + "</td>");
      }
      $tr.append("<td>" + data.api + "</td>");
      $tr.append("<td>" + data.perc + "%</td>");
      $table.append($tr);
    });

    // create chart image
    var $chart = $('<img style="margin-left:30px" alt="" data-dac-src="' + set.chart + '" />');

    // stack up and insert the elements
    $divtable.append($table);
    $divchart.append($chart);
    $div.append($divtable).append($divchart);
    $("#version-chart").replaceWith($div);
  });



  var SCREEN_SIZES = ["Small","Normal","Large","Xlarge"];
  var SCREEN_DENSITIES = ["ldpi","mdpi","tvdpi","hdpi","xhdpi","xxhdpi"];


  // for each set of screens data (each month)
  $.each(SCREEN_DATA, function(i, set) {

    // set up wrapper divs
    var $div = $('<div class="screens-chart"'
         + ((i == 0) ? ' style="display:block"' : '')
         + ' >');

    // set up a new table
    var $table = $("<table>");
    var $trh = $("<tr><th></th></tr>");
    $.each(SCREEN_DENSITIES, function(i, density) {
      $trh.append("<th scope='col'>" + density + "</th>");
    });
    $trh.append("<th scope='col' class='total'>Total</th>");
    $table.append($trh);

    // array to hold totals for each density
    var densityTotals = new Array(SCREEN_DENSITIES.length);
    $.each(densityTotals, function(i, total) {
      densityTotals[i] = 0; // make them all zero to start
    });

    // loop through each screen size
    $.each(SCREEN_SIZES, function(i, size) {
      // if there are any devices of this size
      if (typeof set.data[size] != "undefined") {
        // create table row and insert data
        var $tr = $("<tr>");
        $tr.append("<th scope='row'>" + size + "</th>");
        // variable to sum all densities for this size
        var total = 0;
        // loop through each density
        $.each(SCREEN_DENSITIES, function(i, density) {
          var num = typeof set.data[size][density] != "undefined" ? set.data[size][density] : 0;
          $tr.append("<td>" + (num != 0 ? num + "%" : "") + "</td>");
          total += parseFloat(num);
          densityTotals[i] += parseFloat(num);
        })
        $tr.append("<td class='total'>" + total.toFixed(1) + "%</td>");
        $table.append($tr);
      }
    });

    // create row of totals for each density
    var $tr = $("<tr><th class='total'>Total</th></tr>");
    $.each(densityTotals, function(i, total) {
      $tr.append("<td class='total'>" + total.toFixed(1) + "%</td>");
    });
    $table.append($tr);

    // create charts
    var $sizechart = $('<img style="float:left;width:380px" alt="" data-dac-src="'
            + set.layoutchart + '" />');
    var $densitychart = $('<img style="float:left;width:380px" alt="" data-dac-src="'
            + set.densitychart + '" />');

    // stack up and insert the elements
    $div.append($table).append($sizechart).append($densitychart);
    $("#screens-chart").replaceWith($div);
  });

  // TODO (akassay): Remove this.
  // I replaced the src attributes in the javascript above with data-dac-src
  // so the value would not be molested by the DevSite parser. So this code here
  // moves that src value into a real src attribute at runtime. This should be
  // removed once we either move this script out of the content body or update
  // the parser to not modify src attributes in <script> tags.
  $('img[data-dac-src]').each(function() {
    var src = $(this).attr('data-dac-src');
    $(this).attr('src', src);
  });

});

'''

s = s.replace(" ","").replace("\t","").replace("\r\n","").replace("\n","").strip()

# find screen data
print(re.search(r"varSCREEN_DATA=\[(.*?)\];", s).group(1))
print(re.search(r"varVERSION_DATA=\[(.*?)\];", s).group(1))
print(re.search(r"varVERSION_DATA=\[(.*?)\];", s).group(1))