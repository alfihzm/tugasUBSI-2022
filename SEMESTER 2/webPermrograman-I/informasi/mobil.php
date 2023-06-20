<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="stylesheet" href="../assets/mobil.css?php echo time(); ?>">
    <link
        href="https://fonts.googleapis.com/css2?family=Battambang:wght@100;300;400&family=Montserrat:wght@400;700&family=Noto+Sans:ital,wght@0,100;0,300;0,400;0,700;1,400&family=Quicksand:wght@300;400&family=Roboto:wght@400;500;700&display=swap"
        rel="stylesheet">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500&display=swap" rel="stylesheet">
    <script type="module" src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.esm.js"></script>
    <script nomodule src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.js"></script>
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
                <li><a href="../index.html"> Beranda </a></li>
                <li><a href="../index.html#about-us"> Tentang </a></li>
                <li><a href="../informasi.php"> Informasi </a></li>
                <li><a href="#"> Lainnya </a></li>
            </ul>
        </nav>

        <button class="hamburgers">
            <div class="bar"></div>
        </button>

        <button class="hamburger-2">
            <div class="bars"></div>
        </button>
    </header>

    <nav class="mobile-navs">
        <ul>
            <li><a href="../index.html"> Beranda </a></li>
            <li><a href="../index.html#about-us"> Tentang </a></li>
            <li><a href="../informasi.php"> Informasi </a></li>
            <li><a href="lainnya.php"> Lainnya </a></li>
        </ul>
    </nav>

    <nav class="items">
        <ul>
            <li><a href="mobil.php"> Mobil </a></li>
            <li><a href="#"> Suku Cadang </a></li>
            <li><a href="#"> Ban </a></li>
        </ul>
    </nav>



    <!-- CONTENT  -->
    <div class="container">
        <div class="wrapper">
            <div class="box">
                <img src="../images/Ford-Mustang.jpg" alt="Ford-Mustang">
                <div class="car-name"> 
                    <p> Ford Mustang </p>
                </div> 
                <button class="btn"><a href="spec/ford-mustang.php"> View More </a></button>
            </div>

            <div class="box">
                <img src="../images/mercedes.jpg" alt="Mercedes-C2000K">
                <div class="car-name"> Mercedes C2000K </div>
                <button class="btn"> View More </button>
            </div>

            <div class="box">
                <img src="../images/Civic.jpg" alt="Honda Civic 1.5 E Hatchback Turbo 2019">
                <div class="car-name"> Honda Civic Turbo </div>
                <button class="btn"> View More </button>
            </div>

            <div class="box">
                <img src="../images/BRV.jpg" alt="Honda-BRV-2017">
                <div class="car-name"> Honda BRV </div>
                <button class="btn"> View More </button>
            </div>

            <div class="box">
                <img src="../images/Yaris.jpg" alt="Toyota Yaris TRD matic 2014">
                <div class="car-name"> Toyota Yaris </div>
                <button class="btn"> View More </button>
            </div>

            <div class="box">
                <img src="../images/BMW.jpg" alt="Bmw 318i M40 1991">
                <div class="car-name"> BMW M40 </div>
                <button class="btn"> View More </button>
            </div>
        </div>
    </div>

    <!-- FOOTER -->
    <footer>
        <p><a href="https://www.instagram.com/garagerx_id/">
            <ion-icon class="icon" name="logo-instagram"></ion-icon>
        </a></p>

        <p> Hak Cipta &copy GarageRX 2023. All rights reserved. </p>
    </footer>

    <script src="../JS/script2.js"></script>
</body>

</html>