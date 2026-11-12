import React, { useState, useMemo } from 'react';
import Header from '../../components/Header/Header';
import BookForm from '../../components/BookForm/BookForm';
import BookList from '../../components/BookList/BookList';
import BookFilter from '../../components/BookFilter/BookFilter';
import { useBooks } from '../../context/BookContext';
import './Home.css';

function Home() {
  const { books, addBook, updateBook, deleteBook } = useBooks();

  const [statusFilter, setStatusFilter] = useState('semua');
  const [searchQuery, setSearchQuery] = useState('');
  const [editingBook, setEditingBook] = useState(null);

  const filteredBooks = useMemo(() => {
    return books.filter((book) => {
      const matchesStatus =
        statusFilter === 'semua' || book.status === statusFilter;
      const q = searchQuery.trim().toLowerCase();
      const matchesSearch =
        q === '' ||
        book.title.toLowerCase().includes(q) ||
        book.author.toLowerCase().includes(q);
      return matchesStatus && matchesSearch;
    });
  }, [books, statusFilter, searchQuery]);

  const handleAdd = (bookData) => {
    addBook(bookData);
  };

  const handleUpdate = (id, bookData) => {
    updateBook(id, bookData);
    setEditingBook(null);
  };

  const handleEdit = (book) => {
    setEditingBook(book);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const handleCancelEdit = () => {
    setEditingBook(null);
  };

  const handleDelete = (id) => {
    if (window.confirm('Yakin ingin menghapus buku ini?')) {
      deleteBook(id);
      if (editingBook && editingBook.id === id) {
        setEditingBook(null);
      }
    }
  };

  return (
    <div className="home">
      <Header title="Manajemen Buku Pribadi" description="Catat buku yang dimiliki, dibaca, atau ingin dibeli" />
      <main className="container">
        <BookForm
          initialBook={editingBook}
          onSubmit={editingBook ? handleUpdate : handleAdd}
          onCancel={handleCancelEdit}
        />
        <BookFilter
          statusFilter={statusFilter}
          onStatusChange={setStatusFilter}
          searchQuery={searchQuery}
          onSearchChange={setSearchQuery}
        />
        <BookList books={filteredBooks} onEdit={handleEdit} onDelete={handleDelete} />
      </main>
    </div>
  );
}

export default Home;