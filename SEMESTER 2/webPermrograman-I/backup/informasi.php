<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="assets/informasi.css?v=<?php echo time(); ?>">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link
        href="https://fonts.googleapis.com/css2?family=Battambang:wght@100;300;400&family=Montserrat:wght@400;700&family=Noto+Sans:ital,wght@0,100;0,300;0,400;0,700;1,400&family=Quicksand:wght@300;400&family=Roboto:wght@400;500;700&display=swap"
        rel="stylesheet">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500&display=swap" rel="stylesheet">
    <title> GarageRX | Indonesia </title>
</head>

<body>
    <header>
        <nav>
            <div class="logo">
                <span style="color: rgb(255, 255, 255)">Garage</span><span style="color: #eaa420">RX</span><span
                    style="color: rgb(255, 255, 255)">.</span>
            </div>
            <div class="searchBar">
                <div class="search">
                    <input class="searchBar" name="searchBar" placeholder="Cari di sini"></input>
                    <script src="https://cdn.lordicon.com/bhenfmcm.js"></script>
                    <lord-icon src="https://cdn.lordicon.com/xfftupfv.json" trigger="hover" colors="primary: #FFF"
                        style=>
                    </lord-icon>
                </div>
            </div>

            <!-- <div class="searchBar2">
                <div class="search2">
                    <input class="searchBars" name="searchBars" placeholder="Cari di sini"></input>
                    <script src="https://cdn.lordicon.com/bhenfmcm.js"></script>
                    <lord-icon src="https://cdn.lordicon.com/xfftupfv.json" trigger="hover" colors="primary: #FFF"
                        style=>
                    </lord-icon>
                </div>
            </div> -->

            <ul>
                <li><a href="home.php"> Beranda </a></li>
                <li><a href="home.php#about-us"> Tentang </a></li>
                <li><a href="informasi.php"> Informasi </a></li>
                <li>
                    <a href="#"> Lainnya ▾ </a>
                    <ul class="dropdown">
                        <li><a href="#"> Tips </a></li>
                        <li><a href="#"> Artikel </a></li>
                        <li><a href="#"> Galeri </a></li>
                    </ul>
                </li>
                <li><a href="login.php"> Login </a></li>
            </ul>
        </nav>
    </header>


    <button class="hamburger">
        <div class="bar"></div>
    </button>

    </header>
    <nav class="mobile-nav">
        <ul>
            <li><a href="home.php"> Beranda </a></li>
            <li><a href="#about-us"> Tentang </a></li>
            <li><a href="#service"> Informasi </a></li>
            <li><a href="#"> Galeri </a></li>
            <li><a href="#"> Lainnya </a></li>
        </ul>
    </nav>

    <button class="hamburger-2">
        <div class="bars"></div>
    </button>
    
    <div class="wrapper1">
        <div class="items">
            <a href="informasi/mobil.php"> Mobil </a>
            <a href="informasi/suku-cadang.php"> Suku Cadang </a>
            <a href="informasi/ban.php"> Ban </a>
        </div>
    </div>

    <section id="section1">
        <div class="container1">
        </div>

        <div class="container2">
            <div class="wrapper2">
                
            </div>
        </div>
    </section>

    <footer>
        <p> Hak Cipta &copy GarageRX 2023. All rights reserved. </p>
    </footer>

    <script src="JS/script1.js"></script>
</body>

</html>