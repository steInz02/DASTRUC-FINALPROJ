// ==============================
// MOVIE PLAYLIST SYSTEM
// JAVASCRIPT VERSION
// ==============================

let movies = [

    {
        movie_id: "M01",
        title: "Titanic",
        actor: "Leonardo DiCaprio and Kate Winslet",
        screen_time: 194,
        rating: 8.0,
        director: "James Cameron",
        genre: "Drama, History, Romance",
        release_year: 1997,

        // PUTYOURPICHERE
        poster: "titanic.jpg",

        // PUTYOURTRAILERHERE
        trailer: "https://youtu.be/I7c1etV7D7g"
    },

    {
        movie_id: "M02",
        title: "The Greatest Showman",
        actor: "Hugh Jackman, Zac Efron, Zendaya",
        screen_time: 105,
        rating: 7.5,
        director: "Michael Gracey",
        genre: "Drama, Musical, Biography",
        release_year: 2017,

        poster: "TGS.jpg",
        trailer: "https://youtu.be/EodWwczRIe4"
    },

    {
        movie_id: "M03",
        title: "Girl, Boy, Bakla, Tomboy",
        actor: "Vice Ganda, Maricel Soriano",
        screen_time: 103,
        rating: 6.2,
        director: "Wenn V. Deramas",
        genre: "Comedy, Drama",
        release_year: 2013,

        poster: "GBBT.jpg",
        trailer: "https://youtu.be/P7mAsauoYJQ"
    },

    {
        movie_id: "M04",
        title: "Sisterakas",
        actor: "Vice Ganda, Kris Aquino",
        screen_time: 110,
        rating: 5.4,
        director: "Wenn V. Deramas",
        genre: "Comedy",
        release_year: 2012,

        poster: "SISTERAKAS.jpg",
        trailer: "https://youtu.be/ajsCQyTJZE4"
    },

    {
        movie_id: "M05",
        title: "Almost Us",
        actor: "Fyang Smith and JM Ibarra",
        screen_time: 102,
        rating: 7.1,
        director: "Dan Villegas",
        genre: "Romantic Comedy",
        release_year: 2026,

        poster: "ALMOSTUS.jpg",
        trailer: "https://youtu.be/7Syb_uhtdN0"
    }

];

// ==============================
// GLOBAL VARIABLES
// ==============================

let currentIndex = 0;
let updateIndex = -1;

// ==============================
// UPDATE DASHBOARD
// ==============================

function updateDashboard(message) {

    document.getElementById("totalMovies").textContent =
        movies.length;

    if (movies.length === 0) {

        document.getElementById("currentMovieText").textContent =
            "None";

    } else {

        document.getElementById("currentMovieText").textContent =
            movies[currentIndex].title;
    }

    document.getElementById("statusText").textContent =
        message;
}

// ==============================
// CREATE MOVIE CARD
// ==============================

function createMovieCard(movie, isCurrent) {

    let cardClass = "movie-card";

    if (isCurrent === true) {
        cardClass += " current-card";
    }

    return `
        <div class="${cardClass}"
            onmouseenter="changeHero('${movie.poster}', '${movie.trailer}')">

            <div class="poster"
                style="
                    background-image:url('${movie.poster}');
                ">
            </div>

            <div class="movie-info">

                <h3>${movie.title}</h3>

                <p><b>Actor:</b> ${movie.actor}</p>

                <p><b>Genre:</b> ${movie.genre}</p>

                <p><b>Rating:</b> ${movie.rating}</p>

                <p><b>Year:</b> ${movie.release_year}</p>

            </div>

        </div>
    `;
}

// ==============================
// DISPLAY MOVIES
// ==============================

function showMovies(list, message) {

    let output =
        document.getElementById("movieOutput");

    output.innerHTML = "";

    if (list.length === 0) {

        output.innerHTML =
            "<p>No movies found.</p>";

        updateDashboard(message);
        return;
    }

    for (let i = 0; i < list.length; i++) {

        output.innerHTML += createMovieCard(
            list[i],
            list[i] === movies[currentIndex]
        );
    }

    updateDashboard(message);
}

// ==============================
// CHANGE HERO IMAGE + TRAILER
// ==============================

function changeHero(image, trailer) {

    let hero =
        document.querySelector(".hero");

    hero.style.background = `
        linear-gradient(
            to right,
            rgba(0,0,0,0.95),
            rgba(0,0,0,0.55),
            rgba(0,0,0,0.95)
        ),
        url('${image}')
    `;

    hero.style.backgroundSize = "cover";
    hero.style.backgroundPosition = "center";

    document.getElementById("trailerButton").href =
        trailer;
}

// ==============================
// DISPLAY ALL MOVIES
// ==============================

function displayAll() {

    showMovies(
        movies,
        "Displaying all movies."
    );
}

// ==============================
// DISPLAY REVERSE
// ==============================

function displayReverse() {

    let reversed = [];

    for (let i = movies.length - 1; i >= 0; i--) {

        reversed.push(movies[i]);
    }

    showMovies(
        reversed,
        "Displaying movies in reverse."
    );
}

// ==============================
// CURRENT MOVIE
// ==============================

function showCurrent() {

    if (movies.length === 0) {

        updateDashboard("Playlist is empty.");
        return;
    }

    showMovies(
        [movies[currentIndex]],
        "Current movie displayed."
    );
}

// ==============================
// NEXT MOVIE
// ==============================

function nextMovie() {

    if (movies.length === 0) {

        updateDashboard("Playlist is empty.");
        return;
    }

    currentIndex++;

    if (currentIndex >= movies.length) {
        currentIndex = 0;
    }

    showCurrent();
}

// ==============================
// PREVIOUS MOVIE
// ==============================

function previousMovie() {

    if (movies.length === 0) {

        updateDashboard("Playlist is empty.");
        return;
    }

    currentIndex--;

    if (currentIndex < 0) {
        currentIndex = movies.length - 1;
    }

    showCurrent();
}

// ==============================
// SEARCH BY TITLE
// ==============================

function searchByTitle() {

    let title =
        document.getElementById("searchTitle")
            .value
            .toLowerCase();

    let results = [];

    for (let i = 0; i < movies.length; i++) {

        if (
            movies[i]
                .title
                .toLowerCase()
                .includes(title)
        ) {
            results.push(movies[i]);
        }
    }

    showMovies(results, "Search complete.");
}

// ==============================
// SEARCH BY ACTOR
// ==============================

function searchByActor() {

    let actor =
        document.getElementById("searchActor")
            .value
            .toLowerCase();

    let results = [];

    for (let i = 0; i < movies.length; i++) {

        if (
            movies[i]
                .actor
                .toLowerCase()
                .includes(actor)
        ) {
            results.push(movies[i]);
        }
    }

    showMovies(results, "Actor search complete.");
}

// ==============================
// GET MOVIE INPUT
// ==============================

function getMovieInput() {

    let movie = {

        movie_id:
            document.getElementById("movieId").value,

        title:
            document.getElementById("title").value,

        actor:
            document.getElementById("actor").value,

        screen_time:
            document.getElementById("screenTime").value,

        rating:
            document.getElementById("rating").value,

        director:
            document.getElementById("director").value,

        genre:
            document.getElementById("genre").value,

        release_year:
            document.getElementById("releaseYear").value,

        poster:
            "images/default.jpg",

        trailer:
            "https://www.youtube.com/"
    };

    return movie;
}

// ==============================
// CLEAR INPUTS
// ==============================

function clearInputs() {

    document.getElementById("movieId").value = "";
    document.getElementById("title").value = "";
    document.getElementById("actor").value = "";
    document.getElementById("screenTime").value = "";
    document.getElementById("rating").value = "";
    document.getElementById("director").value = "";
    document.getElementById("genre").value = "";
    document.getElementById("releaseYear").value = "";
    document.getElementById("position").value = "";
}

// ==============================
// ADD AT BEGINNING
// ==============================

function addBeginning() {

    let movie = getMovieInput();

    movies.unshift(movie);

    currentIndex = 0;

    clearInputs();

    displayAll();

    updateDashboard(
        "Movie added at beginning."
    );
}

// ==============================
// ADD AT END
// ==============================

function addEnd() {

    let movie = getMovieInput();

    movies.push(movie);

    clearInputs();

    displayAll();

    updateDashboard(
        "Movie added at end."
    );
}

// ==============================
// ADD AT POSITION
// ==============================

function addPosition() {

    let movie = getMovieInput();

    let position =
        document.getElementById("position").value;

    if (
        position < 1 ||
        position > movies.length + 1
    ) {

        updateDashboard("Invalid position.");
        return;
    }

    movies.splice(position - 1, 0, movie);

    clearInputs();

    displayAll();

    updateDashboard(
        "Movie added at position."
    );
}

// ==============================
// DELETE MOVIE
// ==============================

function deleteMovie() {

    let title =
        document.getElementById("deleteTitle")
            .value
            .toLowerCase();

    for (let i = 0; i < movies.length; i++) {

        if (
            movies[i]
                .title
                .toLowerCase() === title
        ) {

            let confirmDelete =
                confirm(
                    "Do you really want to delete this movie?"
                );

            if (confirmDelete === true) {

                movies.splice(i, 1);

                displayAll();

                updateDashboard(
                    "Movie deleted successfully."
                );
            }

            return;
        }
    }

    updateDashboard("Movie not found.");
}

// ==============================
// OPEN UPDATE BOX
// ==============================

function openUpdateBox() {

    let title =
        document.getElementById("updateTitle")
            .value
            .toLowerCase();

    for (let i = 0; i < movies.length; i++) {

        if (
            movies[i]
                .title
                .toLowerCase() === title
        ) {

            updateIndex = i;

            document
                .getElementById("updateBox")
                .classList
                .remove("hidden");

            return;
        }
    }

    updateDashboard("Movie not found.");
}

// ==============================
// SAVE UPDATE
// ==============================

function saveUpdate() {

    if (updateIndex === -1) {
        return;
    }

    movies[updateIndex].movie_id =
        document.getElementById("updateMovieId").value;

    movies[updateIndex].title =
        document.getElementById("updateNewTitle").value;

    movies[updateIndex].actor =
        document.getElementById("updateActor").value;

    movies[updateIndex].screen_time =
        document.getElementById("updateScreenTime").value;

    movies[updateIndex].rating =
        document.getElementById("updateRating").value;

    movies[updateIndex].director =
        document.getElementById("updateDirector").value;

    movies[updateIndex].genre =
        document.getElementById("updateGenre").value;

    movies[updateIndex].release_year =
        document.getElementById("updateReleaseYear").value;

    document
        .getElementById("updateBox")
        .classList
        .add("hidden");

    displayAll();

    updateDashboard(
        "Movie updated successfully."
    );
}

// ==============================
// INITIAL DISPLAY
// ==============================

displayAll();
updateDashboard("System ready.");