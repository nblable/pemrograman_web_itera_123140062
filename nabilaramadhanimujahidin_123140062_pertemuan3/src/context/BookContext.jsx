import React, { createContext, useContext, useCallback } from 'react';
import useLocalStorage from '../hooks/useLocalStorage';

const BookContext = createContext();

export function useBooks() {
  const context = useContext(BookContext);
  if (!context) {
    throw new Error('useBooks harus digunakan di dalam BookProvider');
  }
  return context;
}

export function BookProvider({ children }) {
  const [books, setBooks] = useLocalStorage('books_data', []);

  const addBook = useCallback((book) => {
    setBooks((prev) => [...prev, { ...book, id: Date.now() }]);
  }, [setBooks]);

  const updateBook = useCallback((id, updated) => {
    setBooks((prev) => prev.map((b) => (b.id === id ? { ...b, ...updated } : b)));
  }, [setBooks]);

  const deleteBook = useCallback((id) => {
    setBooks((prev) => prev.filter((b) => b.id !== id));
  }, [setBooks]);

  const value = {
    books,
    addBook,
    updateBook,
    deleteBook,
  };

  return <BookContext.Provider value={value}>{children}</BookContext.Provider>;
}