{% extends 'library/base.html' %}
{% block content %}

<!-- Hero Section -->
<div class="row mb-5">
    <div class="col-12 text-center">
        <div class="p-5 bg-white rounded shadow-lg">
            <h1 class="display-3 fw-bold text-primary mb-3" style="font-family: 'Poppins', sans-serif;">
                📚 Welcome to LibiPhy
            </h1>
            <p class="lead text-muted mb-4">
                Your Gateway to Physics Thesis Research
            </p>
            <div class="d-grid gap-3 d-md-flex justify-content-center">
                <a href="/library/" class="btn btn-primary btn-lg">
                    🔍 Browse Library
                </a>
                <a href="/admin/" class="btn btn-outline-primary btn-lg">
                    👤 Admin Panel
                </a>
            </div>
        </div>
    </div>
</div>

<!-- Quick Stats Section -->
<div class="row mb-5">
    <div class="col-12">
        <h2 class="fw-bold mb-4" style="font-family: 'Poppins', sans-serif;">📊 Quick Statistics</h2>
    </div>
</div>

<div class="row mb-5">
    <div class="col-md-3 mb-4">
        <div class="card h-100 shadow-sm text-center">
            <div class="card-body">
                <div class="display-4 mb-3">📄</div>
                <h5 class="fw-bold">Total Documents</h5>
                <h2 class="text-primary">{{ total_documents }}</h2>
                <p class="text-muted">All Types</p>
            </div>
        </div>
    </div>
    <div class="col-md-3 mb-4">
        <div class="card h-100 shadow-sm text-center">
            <div class="card-body">
                <div class="display-4 mb-3">📚</div>
                <h5 class="fw-bold">Thesis</h5>
                <h2 class="text-primary">{{ total_thesis }}</h2>
                <p class="text-muted">Research Papers</p>
            </div>
        </div>
    </div>
    <div class="col-md-3 mb-4">
        <div class="card h-100 shadow-sm text-center">
            <div class="card-body">
                <div class="display-4 mb-3">📋</div>
                <h5 class="fw-bold">OJT Narratives</h5>
                <h2 class="text-primary">{{ total_ojt }}</h2>
                <p class="text-muted">Internship Reports</p>
            </div>
        </div>
    </div>
    <div class="col-md-3 mb-4">
        <div class="card h-100 shadow-sm text-center">
            <div class="card-body">
                <div class="display-4 mb-3">⚙️</div>
                <h5 class="fw-bold">SDD</h5>
                <h2 class="text-primary">{{ total_sdd }}</h2>
                <p class="text-muted">System Design Docs</p>
            </div>
        </div>
    </div>
</div>

<!-- Featured Documents Section -->
<div class="row mb-5">
    <div class="col-12">
        <h2 class="fw-bold mb-4" style="font-family: 'Poppins', sans-serif;">🌟 Featured Documents</h2>
    </div>
</div>

<div class="row">
{% for doc in featured_documents %}
<div class="col-md-4 mb-4">
    <div class="card h-100 shadow-sm">
        <div class="card-body">
            <h5 class="card-title fw-bold">{{ doc.title }}</h5>
            <p class="card-text text-muted">
                <strong>👤 Author:</strong> {{ doc.author }}<br>
                <strong>📅 Year:</strong> {{ doc.year }}<br>
                <strong>📁 Type:</strong> {{ doc.get_document_type_display }}
            </p>
            <a href="/document/{{ doc.id }}/" class="btn btn-success btn-sm">👁 View Document</a>
        </div>
    </div>
</div>
{% empty %}
<div class="col-12 text-center">
    <p class="text-muted">No featured documents available yet.</p>
</div>
{% endfor %}
</div>

<!-- Features Section -->
<div class="row mb-5">
    <div class="col-12">
        <h2 class="fw-bold mb-4" style="font-family: 'Poppins', sans-serif;">✨ System Features</h2>
    </div>
</div>

<div class="row">
    <div class="col-md-3 mb-4">
        <div class="card h-100 shadow-sm text-center">
            <div class="card-body">
                <div class="display-4 mb-3">🔍</div>
                <h5 class="fw-bold">Advanced Search</h5>
                <p class="text-muted">Find theses by title, author, or keywords</p>
            </div>
        </div>
    </div>
    <div class="col-md-3 mb-4">
        <div class="card h-100 shadow-sm text-center">
            <div class="card-body">
                <div class="display-4 mb-3">📄</div>
                <h5 class="fw-bold">PDF Viewer</h5>
                <p class="text-muted">Read theses directly in browser</p>
            </div>
        </div>
    </div>
    <div class="col-md-3 mb-4">
        <div class="card h-100 shadow-sm text-center">
            <div class="card-body">
                <div class="display-4 mb-3">📚</div>
                <h5 class="fw-bold">Borrowing System</h5>
                <p class="text-muted">Track thesis loans and returns</p>
            </div>
        </div>
    </div>
    <div class="col-md-3 mb-4">
        <div class="card h-100 shadow-sm text-center">
            <div class="card-body">
                <div class="display-4 mb-3">🔒</div>
                <h5 class="fw-bold">Secure Access</h5>
                <p class="text-muted">School network only access</p>
            </div>
        </div>
    </div>
</div>

<!-- Call to Action -->
<div class="row mb-5">
    <div class="col-12 text-center">
        <div class="p-5 bg-primary text-white rounded shadow-lg">
            <h2 class="fw-bold mb-3">Ready to Explore?</h2>
            <p class="lead mb-4">Browse our collection of physics theses and research papers</p>
            <a href="/library/" class="btn btn-light btn-lg">🔍 Start Searching</a>
        </div>
    </div>
</div>

{% endblock %}