import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import './BookForm.css';

const STATUS_OPTIONS = [
  { value: 'milik', label: 'Dimiliki' },
  { value: 'baca', label: 'Sedang Dibaca' },
  { value: 'beli', label: 'Ingin Dibeli' },
];

function BookForm({ initialBook, onSubmit, onCancel }) {
  const [title, setTitle] = useState('');
  const [author, setAuthor] = useState('');
  const [status, setStatus] = useState('milik');
  const [errors, setErrors] = useState({});

  useEffect(() => {
    if (initialBook) {
      setTitle(initialBook.title || '');
      setAuthor(initialBook.author || '');
      setStatus(initialBook.status || 'milik');
    } else {
      setTitle('');
      setAuthor('');
      setStatus('milik');
    }
    setErrors({});
  }, [initialBook]);

  const validate = () => {
    const newErrors = {};
    if (!title.trim()) newErrors.title = 'Judul wajib diisi';
    if (!author.trim()) newErrors.author = 'Penulis wajib diisi';
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!validate()) return;

    const bookData = {
      title: title.trim(),
      author: author.trim(),
      status,
    };

    if (initialBook) {
      onSubmit(initialBook.id, bookData);
    } else {
      onSubmit(bookData);
    }

    if (!initialBook) {
      setTitle('');
      setAuthor('');
      setStatus('milik');
    }
  };

  return (
    <form className="book-form" onSubmit={handleSubmit} noValidate>
      <div className="form-group">
        <label htmlFor="title">Judul Buku</label>
        <input
          id="title"
          type="text"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          className={errors.title ? 'input-error' : ''}
          placeholder="Masukkan judul buku"
        />
        {errors.title && <span className="error-text">{errors.title}</span>}
      </div>

      <div className="form-group">
        <label htmlFor="author">Penulis</label>
        <input
          id="author"
          type="text"
          value={author}
          onChange={(e) => setAuthor(e.target.value)}
          className={errors.author ? 'input-error' : ''}
          placeholder="Masukkan nama penulis"
        />
        {errors.author && <span className="error-text">{errors.author}</span>}
      </div>

      <div className="form-group">
        <label htmlFor="status">Status</label>
        <select
          id="status"
          value={status}
          onChange={(e) => setStatus(e.target.value)}
        >
          {STATUS_OPTIONS.map((opt) => (
            <option key={opt.value} value={opt.value}>
              {opt.label}
            </option>
          ))}
        </select>
      </div>

      <div className="form-actions">
        <button type="submit" className="submit-btn">
          {initialBook ? 'Simpan Perubahan' : 'Tambah Buku'}
        </button>
        {initialBook && onCancel && (
          <button type="button" className="cancel-btn" onClick={onCancel}>
            Batal
          </button>
        )}
      </div>
    </form>
  );
}

BookForm.propTypes = {
  initialBook: PropTypes.shape({
    id: PropTypes.number,
    title: PropTypes.string,
    author: PropTypes.string,
    status: PropTypes.oneOf(['milik', 'baca', 'beli']),
  }),
  onSubmit: PropTypes.func.isRequired,
  onCancel: PropTypes.func,
};

export default BookForm;