# Research Overview
At MathBioLab, we develop and apply mathematical and computational approaches to understand complex biological systems.


<style>
    /* Swiper container - moves the slideshow to the right */



/* Swiper container - sets size */
.swiper-container {
    width: 650px;
    height: 300px;
    margin: auto;
    overflow: hidden;
    position: relative;
    background-color: white; /* Ensures no overlapping visibility issues */
}

/*
.swiper-container {
    width: 350px;  /* Adjust width as needed */
    height: 400px; /* Adjust height as needed */
    margin: 0 0 10px 10px; /* Adds spacing from text */
    float: right; /* Moves it to the right */
}

/* Ensures text wraps around the slideshow */
.text-content {
    overflow: hidden; /* Prevents text from overlapping */
    text-align: justify; 
}
*/

/* Each slide container */
.swiper-slide {
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;  /* Center horizontally */
    align-items: center;  /* Center vertically */
    background-color: white; /* Ensures background is always clear */
    visibility: hidden; /* Hides non-active slides */
}

/* Ensure only the active slide is visible */
.swiper-slide.swiper-slide-active {
    visibility: visible;
}

/* Images inside slides */
.swiper-slide img {
    max-width: 100%;
    max-height: 100%;
    width: auto;
    height: auto;
    display: block;
    margin: auto; /* Ensures automatic centering */
    object-fit: contain; /* Keeps image inside container without cropping */
}

</style>

<!-- Include Swiper.js from CDN -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css" />
<script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>

<!-- Swiper Slideshow Container -->
<div class="swiper-container">
    <div class="swiper-wrapper">
        {{ get_research_images() }}
    </div>
    <!-- Navigation Arrows -->
    <div class="swiper-button-next"></div>
    <div class="swiper-button-prev"></div>
    <!-- Pagination Dots -->
    <div class="swiper-pagination"></div>
</div>

<!-- Initialize Swiper -->
<script>
document.addEventListener("DOMContentLoaded", function () {
    var swiper = new Swiper(".swiper-container", {
        loop: true, // Infinite looping
        autoplay: { 
            delay: 4000, // 3 seconds per slide
            disableOnInteraction: false 
        },
        effect: "fade", // Smooth fade transition
        fadeEffect: {
            crossFade: true // Ensures smooth fade
        },
        speed: 1000, // Transition duration (in milliseconds)
        pagination: { 
            el: ".swiper-pagination",
            clickable: true
        },
        pagination: { 
            el: ".swiper-pagination",
            clickable: true
        },
        navigation: { 
            nextEl: ".swiper-button-next",
            prevEl: ".swiper-button-prev"
        },
        slidesPerView: 1, // Ensure only one image is shown at a time
        spaceBetween: 0 // Prevent overlap
    });
});
</script>


## Core Research Areas

### Mathematical Modeling
We develop mathematical models to describe biological processes at various scales, from molecular interactions to population dynamics.

### Computational Genomics
We utilize high-throughput genomic and transcriptomic data to understand gene regulation, in Apicomplexan parasites and cancer.

### Machine Learning in Biology
We apply and develop machine learning techniques to extract insights from biological data and predict outcomes of biological processes.

### Systems Biology
We study biological systems as integrated networks, examining how components interact to produce emergent properties.

## Interdisciplinary Approach

Our research is inherently interdisciplinary, combining expertise from:
- Mathematics and Statistics
- Computer Science
- Molecular Biology
- Genetics and Genomics
- Systems Biology