import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import BookForm from './BookForm';

describe('Komponen BookForm', () => {
  test('merender field judul, penulis, dan status', () => {
    render(<BookForm onSubmit={vi.fn()} />);
    expect(screen.getByLabelText(/Judul Buku/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/Penulis/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/Status/i)).toBeInTheDocument();
  });

  test('menampilkan pesan error jika submit dengan field kosong', () => {
    const mockSubmit = vi.fn();
    render(<BookForm onSubmit={mockSubmit} />);
    fireEvent.click(screen.getByRole('button', { name: /Tambah Buku/i }));
    expect(screen.getByText(/Judul wajib diisi/i)).toBeInTheDocument();
    expect(screen.getByText(/Penulis wajib diisi/i)).toBeInTheDocument();
    expect(mockSubmit).not.toHaveBeenCalled();
  });

  test('memanggil onSubmit dengan data buku ketika form valid', () => {
    const mockSubmit = vi.fn();
    render(<BookForm onSubmit={mockSubmit} />);
    fireEvent.change(screen.getByLabelText(/Judul Buku/i), { target: { value: 'Buku A' } });
    fireEvent.change(screen.getByLabelText(/Penulis/i), { target: { value: 'Penulis A' } });
    fireEvent.click(screen.getByRole('button', { name: /Tambah Buku/i }));
    expect(mockSubmit).toHaveBeenCalledWith({
      title: 'Buku A',
      author: 'Penulis A',
      status: 'milik',
    });
  });

  test('mengisi form dari initialBook (mode edit)', () => {
    const mockSubmit = vi.fn();
    render(
      <BookForm
        initialBook={{ id: 1, title: 'Judul Lama', author: 'Penulis Lama', status: 'baca' }}
        onSubmit={mockSubmit}
      />
    );
    expect(screen.getByLabelText(/Judul Buku/i).value).toBe('Judul Lama');
    expect(screen.getByLabelText(/Penulis/i).value).toBe('Penulis Lama');
    expect(screen.getByRole('button', { name: /Simpan Perubahan/i })).toBeInTheDocument();
  });
});