import { useMemo } from 'react';

const STATUS_LABELS = {
  milik: 'Dimiliki',
  baca: 'Sedang Dibaca',
  beli: 'Ingin Dibeli',
};

/**
 * Custom hook untuk menghitung statistik buku.
 * @param {Array} books - daftar buku
 * @returns {Object} objek statistik
 */
function useBookStats(books) {
  return useMemo(() => {
    const total = books.length;
    const milik = books.filter((b) => b.status === 'milik').length;
    const baca = books.filter((b) => b.status === 'baca').length;
    const beli = books.filter((b) => b.status === 'beli').length;

    const byAuthor = books.reduce((acc, b) => {
      acc[b.author] = (acc[b.author] || 0) + 1;
      return acc;
    }, {});

    return {
      total,
      milik,
      baca,
      beli,
      byAuthor,
      labels: STATUS_LABELS,
      percentMilik: total > 0 ? (milik / total) * 100 : 0,
      percentBaca: total > 0 ? (baca / total) * 100 : 0,
      percentBeli: total > 0 ? (beli / total) * 100 : 0,
    };
  }, [books]);
}

export default useBookStats;