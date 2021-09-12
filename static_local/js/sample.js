$(document).ready(function () {
   // Sidebar

   $(".hamburger-menu").click(function () {
      $("#side-navbar").toggleClass("active");
   });
   $(".news--feed-container").click(function () {
      $("#side-navbar").removeClass("active");
   });

   // End Sidebar
   // Comments

//   $(".fsa-comments").click(function () {
//      const post_id = $(".fsa-comments").find('input[name="post_id"]').val();
//      console.log(post_id);
//      $(".pp-comment-section"+post_id).toggleClass("active");
//   });

   $(".comments-reply").click(function () {
      $(".reply-section").show();
   });
   // End Comments
   // Dropdown
//   $(".post--edit-imgbox").click(function (e) {
//      $(".dropdown-content").toggleClass("active");
//      e.stopPropagation();
//   });
   $(document).on("click", function (e) {
      if ($(e.target).is(".post--edit-imgbox") === false) {
         $(".dropdown-content").removeClass("active");
      }
   });

   // tab view
   $(function () {
      $(".company--tabs-content .single-tab").hide();
      $(".company--tabs-content .single-tab:first").show();
      $(".profile--tab-card a").click(function () {
         // Check for active
         $(".profile--tab-card li").removeClass("active");
         $(this).parent().addClass("active");

         // Display active tab
         let currentTab = $(this).attr("href");
         $(".company--tabs-content .single-tab").hide();
         $(currentTab).show();

         return false;
      });
   });
   // end tab view
});
