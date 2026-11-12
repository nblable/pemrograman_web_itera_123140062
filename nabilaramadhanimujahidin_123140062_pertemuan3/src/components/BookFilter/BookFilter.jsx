import React from 'react';
import PropTypes from 'prop-types';
import './BookFilter.css';

const STATUS_OPTIONS = [
  { value: 'semua', label: 'Semua Status' },
  { value: 'milik', label: 'Dimiliki' },
  { value: 'baca', label: 'Sedang Dibaca' },
  { value: 'beli', label: 'Ingin Dibeli' },
];

function BookFilter({ statusFilter, onStatusChange, searchQuery, onSearchChange }) {
  return (
    <div className="book-filter">
      <input
        type="text"
        placeholder="Cari judul atau penulis..."
        value={searchQuery}
        onChange={(e) => onSearchChange(e.target.value)}
        className="search-input"
      />
      <select
        value={statusFilter}
        onChange={(e) => onStatusChange(e.target.value)}
        className="status-select"
      >
        {STATUS_OPTIONS.map((opt) => (
          <option key={opt.value} value={opt.value}>
            {opt.label}
          </option>
        ))}
      </select>
    </div>
  );
}

BookFilter.propTypes = {
  statusFilter: PropTypes.string.isRequired,
  onStatusChange: PropTypes.func.isRequired,
  searchQuery: PropTypes.string.isRequired,
  onSearchChange: PropTypes.func.isRequired,
};

export default BookFilter;