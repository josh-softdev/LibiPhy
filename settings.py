{% extends 'library/base.html' %}

{% block content %}

<div class="row">
    <div class="col-12">
        <div class="card shadow">
            <div class="card-header bg-primary text-white">
                <h3 class="mb-0" style="font-family: 'Poppins', sans-serif;">📄 Thesis Details - LibiPhy</h3>
            </div>
            
            <div class="card-body">
                <h2 class="fw-bold mb-4" style="font-family: 'Poppins', sans-serif;">{{ document.title }}</h2>
                
                <div class="row mb-4">
                    <div class="col-md-6">
                        <div class="card bg-light">
                            <div class="card-body">
                                <h5 class="card-title fw-bold">👤 Author Information</h5>
                                <p class="mb-1"><strong>Name:</strong> {{ document.author }}</p>
                                <p class="mb-1"><strong>Year:</strong> {{ document.year }}</p>
                                <p class="mb-1"><strong>Type:</strong> {{ document.document_type }}</p>
                            </div>
                        </div>
                    </div>
                    
                    <div class="col-md-6">
                        <div class="card bg-light">
                            <div class="card-body">
                                <h5 class="card-title fw-bold">📝 Document Information</h5>
                                <p class="mb-1"><strong>ID:</strong> {{ document.id }}</p>
                                <p class="mb-1"><strong>Uploaded:</strong> {{ document.date_uploaded|date:"M d, Y" }}</p>
                                <p class="mb-1"><strong>File Size:</strong> {{ document.file.size|floatformat:2 }} KB</p>
                            </div>
                        </div>
                    </div>
                </div>
                
                <hr>
                
                <h4 class="fw-bold mb-3" style="font-family: 'Poppins', sans-serif;">📖 Abstract</h4>
                <p class="lead">{{ document.abstract }}</p>
                
                <hr>
                
                <h4 class="fw-bold mb-3" style="font-family: 'Poppins', sans-serif;">📄 Read Thesis</h4>
                
                <div class="alert alert-info">
                    <strong>PDF Viewer:</strong> Click the button below to view the thesis in your browser
                </div>
                
                <div class="d-grid gap-3 d-md-flex justify-content-md-center">
                    <a href="{{ document.file.url }}" target="_blank" class="btn btn-primary btn-lg">
                        📄 Open PDF in New Tab
                    </a>
                    <a href="{{ document.file.url }}" class="btn btn-success btn-lg">
                        ⬇ Download PDF
                    </a>
                </div>
                
                <br>
                
                <a href="/" class="btn btn-secondary btn-lg">
                    ← Back to List
                </a>
            </div>
        </div>
    </div>
</div>

{% endblock %}