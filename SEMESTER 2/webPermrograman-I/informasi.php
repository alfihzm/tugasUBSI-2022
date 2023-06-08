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

            <ul>
                <li><a href="home.php"> Beranda </a></li>
                <li><a href="home.php#about-us"> Tentang </a></li>
                <li><a href="informasi.php"> Informasi </a></li>
                <li>
                    <a href="#"> Lainnya </a>
                    
                </li>
                <li><a href="login.php"> Login </a></li>
            </ul>
        </nav>
    </header>

    <button class="hamburger">
        <div class="bar"></div>
    </button>

    <button class="hamburger-2">
        <div class="bars"></div>
    </button>

    </header>
    <nav class="mobile-nav">
        <ul>
            <li><a href="home.php"> Beranda </a></li>
            <li><a href="home.php#about-us"> Tentang </a></li>
            <li><a href="informasi.php"> Informasi </a></li>
            <li><a href="#"> Lainnya </a></li>
            <li><a href="login.php"> Login </a></li>
        </ul>
    </nav>

    <!-- <nav class="wrapping">
        <ul>
            <li><a href="informasi/mobil.php"> Mobil </a></li>
            <a href="informasi/suku-cadang.php"> Suku Cadang </a>
            <a href="informasi/ban.php"> Ban </a>
        </ul>
    </nav> -->

    <div id="section1">
        <div class="container1">
            <div class="wrapper1">
                <div class="title">
                    <h1> Informasi Terkini </h1>
                </div>

                <div class="news1">
                    <div class="news-info">
                        <img src="images/new-pajero-sport.jpg" alt="sedan">
                        <div class="news-desc">
                            <h3> Semakin Gahar! Spesifikasi All New Pajero Sport 2023 </h3>
                            <p> Otomotif • 2 jam yang lalu </p>
                        </div>
                    </div>
                    
                    <div class="news-info">
                        <img src="images/gas.jpg" alt="gas">
                        <div class="news-desc">
                            <h3> Dikabarkan Tarif BBM Akan Naik Tahun Depan </h3>
                            <p> Bahan Bakar • 5 jam yang lalu </p>
                        </div>
                    </div>

                    <div class="news-info">
                        <img src="images/sedan.jpg" alt="sedan">
                        <div class="news-desc">
                            <h3> Lama Menghilang, 5 Sedan ini Dikabarkan Akan Hadir Kembali dengan Tampilan Baru </h3>
                            <p> Otomotif • 10 jam yang lalu </p>
                        </div>
                    </div>

                    <div class="news-info">
                        <img src="images/Elon-Ma1.jpg" alt="jokowi-elon">
                        <div class="news-desc">
                            <h3> Elon Musk Dikabarkan akan Berinvestasi di Indonesia </h3>
                            <p> Investasi • 2 hari yang lalu </p>
                        </div>
                    </div>

                    <div class="news-info">
                        <img src="images/peta-ganjil-genap1.jpg" alt="ganjil-genap">
                        <div class="news-desc">
                            <h3> Ganjil Genap Jakarta 2023 di Mana Saja? Ini Lokasinya  </h3>
                            <p> Peta Jalan • 3 hari yang lalu </p>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>


    <script src="JS/script1.js"></script>
</body>

</html>