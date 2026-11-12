import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import BookItem from './BookItem';

describe('Komponen BookItem', () => {
  const dummyBook = { id: 5, title: 'React Dasar', author: 'Andi', status: 'milik' };

  test('merender judul, penulis, dan status buku', () => {
    render(<BookItem book={dummyBook} onEdit={vi.fn()} onDelete={vi.fn()} />);
    expect(screen.getByText('React Dasar')).toBeInTheDocument();
    expect(screen.getByText(/oleh Andi/i)).toBeInTheDocument();
    expect(screen.getByText('Dimiliki')).toBeInTheDocument();
  });

  test('memanggil onEdit dengan objek buku saat tombol Edit diklik', () => {
    const mockEdit = vi.fn();
    render(<BookItem book={dummyBook} onEdit={mockEdit} onDelete={vi.fn()} />);
    fireEvent.click(screen.getByRole('button', { name: /Edit/i }));
    expect(mockEdit).toHaveBeenCalledWith(dummyBook);
  });

  test('memanggil onDelete dengan id buku saat tombol Hapus diklik', () => {
    const mockDelete = vi.fn();
    render(<BookItem book={dummyBook} onEdit={vi.fn()} onDelete={mockDelete} />);
    fireEvent.click(screen.getByRole('button', { name: /Hapus/i }));
    expect(mockDelete).toHaveBeenCalledWith(5);
  });
});