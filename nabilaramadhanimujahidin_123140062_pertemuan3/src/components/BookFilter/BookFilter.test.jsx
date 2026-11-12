import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import BookFilter from './BookFilter';

describe('Komponen BookFilter', () => {
  test('memanggil onSearchChange saat mengetik di kolom pencarian', () => {
    const mockSearch = vi.fn();
    render(
      <BookFilter
        statusFilter="semua"
        onStatusChange={vi.fn()}
        searchQuery=""
        onSearchChange={mockSearch}
      />
    );
    fireEvent.change(screen.getByPlaceholderText(/Cari judul atau penulis/i), {
      target: { value: 'react' },
    });
    expect(mockSearch).toHaveBeenCalledWith('react');
  });

  test('memanggil onStatusChange saat memilih status', () => {
    const mockStatus = vi.fn();
    render(
      <BookFilter
        statusFilter="semua"
        onStatusChange={mockStatus}
        searchQuery=""
        onSearchChange={vi.fn()}
      />
    );
    fireEvent.change(screen.getByRole('combobox'), { target: { value: 'milik' } });
    expect(mockStatus).toHaveBeenCalledWith('milik');
  });
});