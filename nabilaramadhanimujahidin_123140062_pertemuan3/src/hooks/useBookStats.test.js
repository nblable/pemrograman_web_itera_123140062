import { renderHook } from '@testing-library/react';
import useBookStats from '../hooks/useBookStats';

describe('Custom Hook useBookStats', () => {
  test('menghitung total dan jumlah per status dengan benar', () => {
    const books = [
      { id: 1, title: 'A', author: 'X', status: 'milik' },
      { id: 2, title: 'B', author: 'X', status: 'baca' },
      { id: 3, title: 'C', author: 'Y', status: 'beli' },
      { id: 4, title: 'D', author: 'Y', status: 'milik' },
    ];
    const { result } = renderHook(() => useBookStats(books));
    expect(result.current.total).toBe(4);
    expect(result.current.milik).toBe(2);
    expect(result.current.baca).toBe(1);
    expect(result.current.beli).toBe(1);
  });

  test('menghitung byAuthor dengan benar', () => {
    const books = [
      { id: 1, title: 'A', author: 'X', status: 'milik' },
      { id: 2, title: 'B', author: 'X', status: 'baca' },
    ];
    const { result } = renderHook(() => useBookStats(books));
    expect(result.current.byAuthor).toEqual({ X: 2 });
  });

  test('menangani daftar kosong', () => {
    const { result } = renderHook(() => useBookStats([]));
    expect(result.current.total).toBe(0);
    expect(result.current.percentMilik).toBe(0);
  });
});