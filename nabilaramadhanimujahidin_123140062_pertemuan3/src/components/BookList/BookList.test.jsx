import React from 'react';
import { render, screen } from '@testing-library/react';
import BookList from './BookList';

describe('Komponen BookList', () => {
  const books = [
    { id: 1, title: 'Buku Satu', author: 'A', status: 'milik' },
    { id: 2, title: 'Buku Dua', author: 'B', status: 'baca' },
  ];

  test('merender semua buku dalam daftar', () => {
    render(<BookList books={books} onEdit={vi.fn()} onDelete={vi.fn()} />);
    expect(screen.getByText('Buku Satu')).toBeInTheDocument();
    expect(screen.getByText('Buku Dua')).toBeInTheDocument();
  });

  test('menampilkan pesan kosong jika daftar buku kosong', () => {
    render(<BookList books={[]} onEdit={vi.fn()} onDelete={vi.fn()} />);
    expect(screen.getByText(/Tidak ada buku yang ditemukan/i)).toBeInTheDocument();
  });
});