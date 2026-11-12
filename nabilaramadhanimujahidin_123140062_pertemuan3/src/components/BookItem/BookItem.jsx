import React from 'react';
import PropTypes from 'prop-types';
import './BookItem.css';

const STATUS_LABELS = {
  milik: 'Dimiliki',
  baca: 'Sedang Dibaca',
  beli: 'Ingin Dibeli',
};

function BookItem({ book, onEdit, onDelete }) {
  return (
    <div className="book-item">
      <div className="book-info">
        <h3 className="book-title">{book.title}</h3>
        <p className="book-author">oleh {book.author}</p>
        <span className={`book-status status-${book.status}`}>
          {STATUS_LABELS[book.status] || book.status}
        </span>
      </div>
      <div className="book-actions">
        <button className="edit-btn" onClick={() => onEdit(book)}>Edit</button>
        <button className="delete-btn" onClick={() => onDelete(book.id)}>Hapus</button>
      </div>
    </div>
  );
}

BookItem.propTypes = {
  book: PropTypes.shape({
    id: PropTypes.number.isRequired,
    title: PropTypes.string.isRequired,
    author: PropTypes.string.isRequired,
    status: PropTypes.oneOf(['milik', 'baca', 'beli']).isRequired,
  }).isRequired,
  onEdit: PropTypes.func.isRequired,
  onDelete: PropTypes.func.isRequired,
};

export default BookItem;