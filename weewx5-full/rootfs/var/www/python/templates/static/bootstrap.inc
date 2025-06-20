<link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
/>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>

<style type="text/css">
  #mainiframe {
    width: 100%;
    height: 2500;
  }

  /* ============ desktop view ============ */
  @media all and (min-width: 990px) {
    .dropdown-menu li {
      position: relative;
    }

    .dropdown-menu .submenu {
      display: none;
      position: absolute;
      left: 100%;
      top: -7px;
    }

    .dropdown-menu .submenu-left {
      right: 100%;
      left: auto;
    }

    .dropdown-menu > li:hover {
      background-color: #f1f1f1;
    }

    .dropdown-menu > li:hover > .submenu {
      display: block;
    }
  }

  /* ============ desktop view .end// ============ */

  /* ============ small devices ============ */
  @media (max-width: 991px) {
    .dropdown-menu .dropdown-menu {
      margin-left: 0.7rem;
      margin-right: 0.7rem;
      margin-bottom: 0.5rem;
    }
  }

  /* ============ small devices .end// ============ */

  /* make primary button bold */
  .btn-primary {
    color: #fff;
  }

  .badge {
    font-size: 1.1rem;
  }

  .label {
    font-weight: bold;
    font-size: 1.1rem;
  }

  .success {background-color: #04AA6D;} /* Green */
  .info {background-color: #2196F3;} /* Blue */
  .warning {background-color: #ff9800;} /* Orange */
  .danger {background-color: #f44336;} /* Red */ 
  .other {background-color: #e7e7e7; color: black;} /* Gray */ 
  
</style>

<script type="text/javascript">
  //	window.addEventListener("resize", function() {
  //		"use strict"; window.location.reload();
  //	});

  document.addEventListener("DOMContentLoaded", function () {
    /////// Prevent closing from click inside dropdown
    //document.querySelectorAll(".dropdown-menu").forEach(function (element) {
    //  element.addEventListener("click", function (e) {
    //    e.stopPropagation();
    //  });
    // });

    // make it as accordion for smaller screens
    if (window.innerWidth < 992) {
      // close all inner dropdowns when parent is closed
      document
        .querySelectorAll(".navbar .dropdown")
        .forEach(function (everydropdown) {
          everydropdown.addEventListener("hidden.bs.dropdown", function () {
            // after dropdown is hidden, then find all submenus
            this.querySelectorAll(".submenu").forEach(function (everysubmenu) {
              // hide every submenu as well
              everysubmenu.style.display = "none";
            });
          });
        });

      document.querySelectorAll(".dropdown-menu a").forEach(function (element) {
        element.addEventListener("click", function (e) {
          let nextEl = this.nextElementSibling;
          if (nextEl && nextEl.classList.contains("submenu")) {
            // prevent opening link if link needs to open dropdown
            e.preventDefault();
            console.log(nextEl);
            if (nextEl.style.display == "block") {
              nextEl.style.display = "none";
            } else {
              nextEl.style.display = "block";
            }
          }
        });
      });
    }
    // end if innerWidth
  });
  // DOMContentLoaded  end
</script>

<!--Set the iframe to the content selected by the menu -->
<script type="text/javascript">
  //  function setFrame(e) {
  //    var page = e.getAttribute("data-name");
  //    //setCookie("mydefaultreport", page, 7);
  //   window.location.replace("/");
  // }
</script>

<script type="text/javascript">
  function setCookie(name, value, days) {
    var expires = "";
    if (days) {
      var date = new Date();
      date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
      expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "") + expires + "; path=/";
  }
  function getCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(";");
    for (var i = 0; i < ca.length; i++) {
      var c = ca[i];
      while (c.charAt(0) == " ") c = c.substring(1, c.length);
      if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
    }
    return null;
  }
  function eraseCookie(name) {
    document.cookie =
      name + "=; Path=/; Expires=Thu, 01 Jan 1970 00:00:01 GMT;";
  }
</script>
