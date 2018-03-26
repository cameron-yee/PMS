// require the gulp module
var gulp = require('gulp');

// gulp dependencies:
var sass = require('gulp-sass');
var autoprefixer = require('gulp-autoprefixer');
var concat = require('gulp-concat');
var rename = require('gulp-rename');
var uglify = require('gulp-uglify');
var cleanCSS = require('gulp-clean-css');


// path to sass files
var sassFiles = 'pms/static/styles/scss/*.scss';
// destination for compiled css
var cssDest = 'pms/static/styles/css/';

// build sass task
gulp.task('sass', function(){
  // grab all of the sass files
  // set the task as a promise (stream) letting the engine know that it should wait to resolve
  var stream = gulp.src(sassFiles)
    // compile the sass files and alert if there's any errors
    .pipe(sass().on('error', sass.logError))
    // autoprefixer, default configuration (browsers with over 1% market share, last 2 versions of all browsers, firefox esr, opera 12.1)
    .pipe(autoprefixer())
    // dump the compiled css file into the specified destination
    .pipe(gulp.dest(cssDest));
  // return the stream as the completion hint
  return stream;
});

// path to our custom css file
var cssFile = 'pms/static/styles/css/styles.css';
// destination for the minified css file, also where third party minified files will live
var cssMinDest = 'pms/static/styles/css/min/';

// minify css task
// identifies dependent task 'sass' that must be complete before this one begins
gulp.task('cssmin', ['sass'], function(){
  // grab the css file
  // set the task as a promise (stream) letting the engine know that it should wait to resolve
  var stream = gulp.src(cssFile)
    // give it a new name
    .pipe(rename('styles.min.css'))
    // clean and minify the css, add compatibility for internet explorer
    .pipe(cleanCSS({compatibility: 'ie8'}))
    // dump the minified file into the specified destination
    .pipe(gulp.dest(cssMinDest));
  // return the stream as the completion hint
  return stream;
});

// // path to our minified css files, processing order matters
// var cssMinFiles = [
//   'pms/static/styles/css/min/styles.min.css',
// ];
// // destination for the concatenated css file
// var cssConcatDest = 'pms/static/styles/css/concat/';
//
// // concat css.min files task
// // identifies dependent task 'cssmin' that must be complete before this one begins
// gulp.task('cssconcat', ['cssmin'], function(){
//   // grab all of the minified css files
//   // set the task as a promise (stream) letting the engine know that it should wait to resolve
//   var stream = gulp.src(cssMinFiles)
//     // concatenate all of the minified css files and place them into a new file called concat.css
//     .pipe(concat('concat.css'))
//     // dump the concatenated/minified css file into the specified destination
//     .pipe(gulp.dest(cssConcatDest));
//   // return the stream as the completion hint
//   return stream;
// });

// path to our custom javascript file
var jsFile = 'pms/static/js/script.js';
var jsMinDest = 'pms/static/js/min/';

// minify javascript task
gulp.task('scriptmin', function() {
  // grab our custom javascript file
  // set the task as a promise (stream) letting the engine know that it should wait to resolve
  var stream = gulp.src(jsFile)
    // give it a new name
    .pipe(rename('script.min.js'))
    // minify our javascript file
    .pipe(uglify())
    // save the minified javascript file to the specified destination
    .pipe(gulp.dest(jsMinDest));
  // return the stream as the completion hint
  return stream;
});

// // path to the minified javascript files, processing order matters
// var jsMinFiles = [
//   'pms/static/js/min/script.min.js',
// ];
//
// // destination for the concatenated javascript file
// var jsConcatDest = 'pms/static/js/concat/';
//
// // concatenate javascript task
// // identifies dependent task 'scriptmin' that must be complete before this one begins
// gulp.task('scriptconcat', ['scriptmin'], function() {
//   // grab our minified javascript files
//   // set the task as a promise (stream) letting the engine know that it should wait to resolve
//   var stream = gulp.src(jsMinFiles)
//     // concatenate all of the minified javascript files and place them into a new file called concat.js
//     .pipe(concat('concat.js'))
//     // dump the concatenated/minified javascript file into the specified destination
//     .pipe(gulp.dest(jsConcatDest));
//   // return the stream as the completion hint
//   return stream;
// });

// watch all sass, javascript, and template files for changes
gulp.task('watch', function() {
  // // if any of the sass files change carry out the specified gulp tasks
  // gulp.watch(sassFiles,['sass','cssmin','cssconcat']);
  // if any of the sass files change carry out the specified gulp tasks
  gulp.watch(sassFiles,['sass','cssmin']);
  // // if script.js changes carry out the specified gulp tasks
  // gulp.watch(jsFile,['scriptmin','scriptconcat']);
  // if script.js changes carry out the specified gulp task
  gulp.watch(jsFile,['scriptmin']);
});