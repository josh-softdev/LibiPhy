{% extends 'library/base.html' %}
{% block content %}
<div class="row mb-5">
    <div class="col-12">
        <h1 class="display-4 fw-bold text-primary" style="font-family: 'Poppins', sans-serif;">📊 Admin Dashboard</h1>
        <p class="text-muted">OJT Narratives & Document Management</p>
    </div>
</div>

<!-- Statistics Cards -->
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

<!-- Recent OJT Narratives -->
<div class="row mb-5">
    <div class="col-12">
        <h2 class="fw-bold mb-4" style="font-family: 'Poppins', sans-serif;">📋 Recent OJT Narratives</h2>
    </div>
</div>
<div class="row">
{% for doc in recent_ojt %}
<div class="col-md-6 mb-4">
    <div class="card shadow-sm">
        <div class="card-body">
            <h5 class="card-title fw-bold">{{ doc.title }}</h5>
            <p class="card-text text-muted">
                <strong>👤 Author:</strong> {{ doc.author }}<br>
                <strong>📅 Year:</strong> {{ doc.year }}<br>
                <strong>📁 Program:</strong> {{ doc.program }}<br>
                <strong>📅 Uploaded:</strong> {{ doc.date_uploaded }}
            </p>
            <a href="/document/{{ doc.id }}/" class="btn btn-success btn-sm">👁 View Document</a>
            <a href="/admin/library/document/{{ doc.id }}/change/" class="btn btn-primary btn-sm">✏️ Edit</a>
        </div>
    </div>
</div>
{% empty %}
<div class="col-12 text-center">
    <p class="text-muted">No OJT narratives available yet.</p>
</div>
{% endfor %}
</div>

<!-- Recent Documents -->
<div class="row mb-5">
    <div class="col-12">
        <h2 class="fw-bold mb-4" style="font-family: 'Poppins', sans-serif;">📄 Recent Documents</h2>
    </div>
</div>
<div class="row">
{% for doc in recent_documents %}
<div class="col-md-6 mb-4">
    <div class="card shadow-sm">
        <div class="card-body">
            <h5 class="card-title fw-bold">{{ doc.title }}</h5>
            <p class="card-text text-muted">
                <strong>👤 Author:</strong> {{ doc.author }}<br>
                <strong>📅 Year:</strong> {{ doc.year }}<br>
                <strong>📁 Type:</strong> {{ doc.get_document_type_display }}
            </p>
            <a href="/document/{{ doc.id }}/" class="btn btn-success btn-sm">👁 View Document</a>
            <a href="/admin/library/document/{{ doc.id }}/change/" class="btn btn-primary btn-sm">✏️ Edit</a>
        </div>
    </div>
</div>
{% empty %}
<div class="col-12 text-center">
    <p class="text-muted">No documents available yet.</p>
</div>
{% endfor %}
</div>

<!-- Borrowing Statistics -->
<div class="row mb-5">
    <div class="col-12">
        <h2 class="fw-bold mb-4" style="font-family: 'Poppins', sans-serif;">📚 Borrowing Statistics</h2>
    </div>
</div>
<div class="row">
    <div class="col-md-6 mb-4">
        <div class="card h-100 shadow-sm text-center">
            <div class="card-body">
                <div class="display-4 mb-3">📋</div>
                <h5 class="fw-bold">Active Borrowings</h5>
                <h2 class="text-primary">{{ active_borrowings }}</h2>
                <p class="text-muted">Currently Borrowed</p>
            </div>
        </div>
    </div>
    <div class="col-md-6 mb-4">
        <div class="card h-100 shadow-sm text-center">
            <div class="card-body">
                <div class="display-4 mb-3">⚠️</div>
                <h5 class="fw-bold">Overdue Borrowings</h5>
                <h2 class="text-danger">{{ overdue_borrowings }}</h2>
                <p class="text-muted">Need Attention</p>
            </div>
        </div>
    </div>
</div>

<!-- Quick Actions -->
<div class="row mb-5">
    <div class="col-12">
        <h2 class="fw-bold mb-4" style="font-family: 'Poppins', sans-serif;">⚡ Quick Actions</h2>
    </div>
</div>
<div class="row">
    <div class="col-md-3 mb-4">
        <div class="card h-100 shadow-sm text-center">
            <div class="card-body">
                <div class="display-4 mb-3">➕</div>
                <h5 class="fw-bold">Add Document</h5>
                <a href="/admin/library/document/add/" class="btn btn-primary btn-lg">Add New</a>
            </div>
        </div>
    </div>
    <div class="col-md-3 mb-4">
        <div class="card h-100 shadow-sm text-center">
            <div class="card-body">
                <div class="display-4 mb-3">📋</div>
                <h5 class="fw-bold">OJT Narratives</h5>
                <a href="/admin/library/document/?document_type=OJT" class="btn btn-success btn-lg">View OJT</a>
            </div>
        </div>
    </div>
    <div class="col-md-3 mb-4">
        <div class="card h-100 shadow-sm text-center">
            <div class="card-body">
                <div class="display-4 mb-3">📚</div>
                <h5 class="fw-bold">Borrowings</h5>
                <a href="/admin/library/borrowing/" class="btn btn-info btn-lg">View All</a>
            </div>
        </div>
    </div>
    <div class="col-md-3 mb-4">
        <div class="card h-100 shadow-sm text-center">
            <div class="card-body">
                <div class="display-4 mb-3">🔧</div>
                <h5 class="fw-bold">Admin Panel</h5>
                <a href="/admin/" class="btn btn-warning btn-lg">Go to Admin</a>
            </div>
        </div>
    </div>
</div>
{% endblock %}