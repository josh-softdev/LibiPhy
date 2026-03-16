{% extends 'library/base.html' %}

{% block content %}

<div class="row mb-5">
    <div class="col-12 text-center">
        <!-- Main Title with Better Font -->
        <h1 class="display-4 fw-bold text-primary" style="font-family: 'Poppins', sans-serif;">
            📚 LibiPhy
        </h1>
        <!-- Subtitle -->
        <p class="text-muted fs-5" style="font-family: 'Roboto', sans-serif;">
            Physics Thesis Library
        </p>
    </div>
</div>

<!-- Search Bar -->
<div class="row mb-4">
    <div class="col-md-8 mx-auto">
        <form method="GET" class="input-group">
            <input type="text" name="q" class="form-control form-control-lg" placeholder="Search thesis by title or author...">
            <button class="btn btn-primary btn-lg" type="submit">
                🔍 Search
            </button>
        </form>
    </div>
</div>

<!-- Thesis Cards -->
<div class="row">

{% for doc in documents %}

<div class="col-md-4 mb-4">
    <div class="card h-100 shadow-sm">
        
        <div class="card-body">
            <h5 class="card-title fw-bold">{{ doc.title }}</h5>
            
            <div class="mb-3">
                <p class="card-text text-muted">
                    <strong>👤 Author:</strong> {{ doc.author }}<br>
                    <strong>📅 Year:</strong> {{ doc.year }}<br>
                    <strong>📁 Type:</strong> {{ doc.document_type }}
                </p>
            </div>
            
            <div class="d-grid gap-2">
                <a href="/document/{{ doc.id }}/" class="btn btn-success btn-lg">
                    👁 View Thesis
                </a>
                <a href="{{ doc.file.url }}" class="btn btn-primary btn-lg">
                    ⬇ Download PDF
                </a>
            </div>
        </div>
        
        <div class="card-footer bg-white border-0">
            <small class="text-muted">ID: {{ doc.id }}</small>
        </div>
    </div>
</div>

{% empty %}

<div class="col-12 text-center">
    <div class="alert alert-info">
        <h4>📭 No Documents Found</h4>
        <p>No theses match your search. Try a different keyword.</p>
    </div>
</div>

{% endfor %}

</div>

{% endblock %}