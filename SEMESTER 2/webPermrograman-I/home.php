<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="assets/home.css?v=<?php echo time(); ?>">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link
        href="https://fonts.googleapis.com/css2?family=Battambang:wght@100;300;400&family=Montserrat:wght@400;700&family=Noto+Sans:ital,wght@0,100;0,300;0,400;0,700;1,400&family=Quicksand:wght@300;400&family=Roboto:wght@400;500;700&display=swap"
        rel="stylesheet">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@9/swiper-bundle.min.css" />
    <title> GarageRX | Indonesia </title>
</head>

<body>
    <header>
        <nav>
            <div class="logo">
                <span style="color: rgb(255, 255, 255)">Garage</span><span style="color: #eaa420">RX</span><span
                    style="color: rgb(255, 255, 255)">.</span>
            </div>
            <ul>
                <li><a href="home.php"> Beranda </a></li>
                <li><a href="#about-us"> Tentang </a></li>
                <li><a href="informasi.php"> Informasi </a></li>
                <li><a href="#"> Lainnya </a></li>
                <li><a href="login.php"> Login </a></li>
            </ul>
        </nav>

        <button class="hamburger">
            <div class="bar"></div>
        </button>
    </header>
    <nav class="mobile-nav">
        <ul>
            <li><a href="home.php"> Beranda </a></li>
            <li><a href="#about-us"> Tentang </a></li>
            <li><a href="informasi.php"> Informasi </a></li>
            <li><a href="#"> Galeri </a></li>
            <li><a href="login.php"> Lainnya </a></li>
        </ul>
    </nav>



    <!-- BERANDA -->
    <section id="section1" class="home">
        <div class="container1">
            <div class="swiper">
                <!-- Additional required wrapper -->
                <div class="swiper-wrapper">
                    <!-- Slides -->
                    <div class="swiper-slide"><img src="images/car-1.jpg" alt="car-1"></div>
                    <div class="swiper-slide"><img src="images/car-2.jpg" alt="car-2"></div>
                    <div class="swiper-slide"><img src="images/tengyart-90HcLnI0T1w-unsplash.jpg" alt="car-3"></div>
                    <div class="swiper-slide"><img src="images/car-10.jpg" alt="car-4"></div>

                </div>
                <!-- If we need pagination -->
                <div class="swiper-pagination"></div>

                <!-- If we need navigation buttons -->
                <div class="swiper-button-prev"></div>
                <div class="swiper-button-next"></div>
            </div>
        </div>

        <div class="homeNews">

        </div>
        </div>
    </section>



    <!-- TENTANG -->
    <section id="section2" class="aboutUs">
        <div id="about-us">
            <h1> TENTANG </h1>
            <div class="container2">
                <div class="wrapper2">
                    <div class="ourbox1">
                        <div class="images">
                            <img src="images/car-inside.jpg" alt="machine">
                        </div>
                        <div class="description">
                            <p> Selamat datang di GarageRX </p>
                            <br>
                            <p> GarageRX adalah destinasi utama bagi pecinta mobil dan penggemar dunia otomotif. Kami
                                adalah sumber terpercaya untuk segala hal terkait dengan kendaraan, menyediakan beragam
                                informasi terkini, ulasan kendaraan, tips perawatan, dan berita terbaru dari industri
                                otomotif. </p>
                            <br>
                            <p> Di Web Informasi GarageRX, Anda akan menemukan berbagai artikel informatif yang mencakup
                                segala aspek tentang kendaraan. Apakah Anda mencari informasi tentang mobil baru, ulasan
                                tentang model terbaru, atau ingin mengetahui lebih banyak tentang teknologi terkini
                                dalam industri otomotif, kami memiliki semua yang Anda butuhkan. </p>
                        </div>
                    </div>

                    <!-- <div class="ourboxes">
                        <div class="visi">
                            <h2> VISI </h2>
                        </div>

                        <div class="misi">
                            <h2> MISI </h2>
                        </div>
                    </div> -->
                </div>
            </div>
        </div>
    </section>





    <!-- PELAYANAN -->
    <!-- <section id="section3" class="aboutUs">
        <div id="service">
            <h1> Pelayanan </h1>
            <div class="container2">
                <div class="wrapper2">
                    <div class="ourbox1">

                    </div>
                </div>
            </div>
        </div>
    </section> -->


    <!-- FOOTER -->
    <footer>
        <p> Hak Cipta &copy GarageRX 2023. All rights reserved. </p>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/swiper@9/swiper-bundle.min.js"></script>
    <script src="JS/swiper.js"></script>
    <script src="JS/script.js"></script>
</body>

</html>