{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LibiPhy - Digital Library System</title>
    
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    
    <!-- Google Fonts - More Engaging Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=Roboto:wght@300;400;500;700&display=swap" rel="stylesheet">
    
    <!-- Custom CSS -->
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            background-color: #f8f9fa;
        }
        
        .navbar {
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%) !important;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        .navbar-brand {
            font-weight: 700;
            font-size: 1.5rem;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .navbar-brand img {
            height: 40px;
            width: auto;
        }
        
        .navbar-brand span {
            color: #fff;
            font-family: 'Poppins', sans-serif;
            font-weight: 600;
        }
        
        .container {
            max-width: 1200px;
        }
        
        .card {
            border: none;
            border-radius: 10px;
            transition: transform 0.3s, box-shadow 0.3s;
        }
        
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(0,0,0,0.15);
        }
        
        .btn-primary {
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            border: none;
            border-radius: 5px;
        }
        
        .btn-success {
            background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
            border: none;
            border-radius: 5px;
        }
        
        .btn-lg {
            padding: 12px 30px;
            font-weight: 500;
        }
        
        .alert-info {
            background: linear-gradient(135deg, #e0f7fa 0%, #b2ebf2 100%);
            border: none;
            border-radius: 10px;
        }
        
        .footer {
            margin-top: 50px;
            padding: 20px 0;
            background-color: #1e3c72;
            color: white;
            text-align: center;
        }
    </style>
</head>

<body>

<!-- Navigation Bar -->
<nav class="navbar navbar-expand-lg navbar-dark">
  <div class="container">
    <a class="navbar-brand" href="/">
        <!-- Logo - Using LOCAL file -->
        <img src="{% static 'images/logo.png' %}" alt="EquiLib Logo" style="height: 40px;">
        <span>📚 LibiPhy</span>
    </a>

    <div class="collapse navbar-collapse">
      <ul class="navbar-nav ms-auto">
        <li class="nav-item">
            <a class="nav-link" href="/">Home</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" href="/library/">Library</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" href="/admin/">Admin Panel</a>
        </li>
      </ul>
    </div>
  </div>
</nav>

<div class="container mt-4">

{% block content %}

{% endblock %}

</div>

<!-- Footer -->
<div class="footer">
    <div class="container">
        <p>&copy; 2026 LibiPhy - Digital Library System | All Rights Reserved</p>
    </div>
</div>

<!-- Bootstrap JS -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>