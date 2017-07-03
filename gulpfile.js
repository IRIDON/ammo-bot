var gulp = require('gulp');
var sass = require('gulp-sass');
var gulpCopy = require('gulp-copy');
var minifyCSS = require('gulp-csso');

var config = {
    style: './assets/scss/*.scss',
    image: './assets/img/*',
    dest: './static'
}

gulp.task('sass', function () {
    return gulp.src(config.style)
        .pipe(sass().on('error', sass.logError))
        .pipe(minifyCSS())
        .pipe(gulp.dest(
            config.dest + '/css'
        ));
});

gulp.task('images', function () {
    return gulp.src(config.image)
        .pipe(gulpCopy(
            config.dest,
            {
                prefix: 1
            }
        ))
        .pipe(gulp.dest(
            config.dest
        ));
});

gulp.task('default', [
    'sass',
    'images'
]);
