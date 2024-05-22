<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Organic Soap</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f5f5dc;
            color: #333;
        }
        header {
            background-color: #8b4513;
            color: white;
            padding: 1rem 0;
            text-align: center;
        }
        nav {
            display: flex;
            justify-content: center;
            background-color: #a0522d;
        }
        nav a {
            color: white;
            padding: 1rem;
            text-decoration: none;
        }
        nav a:hover {
            background-color: #8b4513;
        }
        section {
            padding: 2rem;
            margin: 1rem auto;
            max-width: 800px;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .products, .testimonials, .blog {
            display: flex;
            flex-wrap: wrap;
            gap: 1rem;
        }
        .product, .testimonial, .post {
            flex: 1 1 calc(33% - 2rem);
            background-color: #f5f5dc;
            padding: 1rem;
            border: 1px solid #ddd;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        footer {
            text-align: center;
            padding: 1rem 0;
            background-color: #8b4513;
            color: white;
        }
    </style>
</head>
<body>
    <header>
        <h1>Welcome to Organic Soap</h1>
    </header>
    <nav>
        <a href="#home">Home</a>
        <a href="#about">About</a>
        <a href="#products">Products</a>
        <a href="#testimonials">Testimonials</a>
        <a href="#blog">Blog</a>
        <a href="#contact">Contact</a>
    </nav>

    <section id="home">
        <h2>Home</h2>
        <p>Discover the natural goodness of our organic soaps, crafted with care and love from the finest ingredients.</p>
    </section>

    <section id="about">
        <h2>About</h2>
        <p>Our mission is to provide high-quality organic soap that nourishes your skin and respects the environment. Learn more about our journey and values.</p>
    </section>

    <section id="products">
        <h2>Products</h2>
        <div class="products">
            <div class="product">
                <h3>Lavender Bliss</h3>
                <p>Relaxing lavender scent with soothing properties.</p>
            </div>
            <div class="product">
                <h3>Citrus Fresh</h3>
                <p>Energizing citrus scent to start your day right.</p>
            </div>
            <div class="product">
                <h3>Minty Cool</h3>
                <p>Refreshing mint to invigorate your senses.</p>
            </div>
        </div>
    </section>

    <section id="testimonials">
        <h2>Testimonials</h2>
        <div class="testimonials">
            <div class="testimonial">
                <p>"The best soap I've ever used! My skin feels amazing." - Jane Doe</p>
            </div>
            <div class="testimonial">
                <p>"I love the natural scents and how gentle it is on my skin." - John Smith</p>
            </div>
            <div class="testimonial">
                <p>"Highly recommend! Perfect for sensitive skin." - Sarah Lee</p>
            </div>
        </div>
    </section>

    <section id="blog">
        <h2>Blog</h2>
        <div class="blog">
            <div class="post">
                <h3>Benefits of Organic Soap</h3>
                <p>Learn why organic soap is better for your skin and the environment.</p>
            </div>
            <div class="post">
                <h3>How We Source Our Ingredients</h3>
                <p>Discover our commitment to sustainable and ethical sourcing.</p>
            </div>
            <div class="post">
                <h3>DIY Soap Recipes</h3>
                <p>Try making your own organic soap with these simple recipes.</p>
            </div>
        </div>
    </section>

    <section id="contact">
        <h2>Contact</h2>
        <p>Get in touch with us for more information or to place an order.</p>
        <p>Email: info@organicsoap.com</p>
        <p>Phone: 123-456-7890</p>
    </section>

    <footer>
        <p>&copy; 2024 Organic Soap. All rights reserved.</p>
    </footer>
</body>
</html>
