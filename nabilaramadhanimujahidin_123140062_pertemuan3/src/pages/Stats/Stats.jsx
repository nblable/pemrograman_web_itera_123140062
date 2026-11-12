import React from 'react';
import Header from '../../components/Header/Header';
import { useBooks } from '../../context/BookContext';
import useBookStats from '../../hooks/useBookStats';
import './Stats.css';

function Stats() {
  const { books } = useBooks();
  const stats = useBookStats(books);

  return (
    <div className="stats-page">
      <Header title="Statistik Buku" description="Ringkasan koleksi buku Anda" />
      <main className="container">
        <div className="stats-grid">
          <div className="stat-card">
            <h3>Total Buku</h3>
            <p className="stat-number">{stats.total}</p>
          </div>
          <div className="stat-card status-milik">
            <h3>Dimiliki</h3>
            <p className="stat-number">{stats.milik}</p>
            <p className="stat-percent">{stats.percentMilik.toFixed(0)}%</p>
          </div>
          <div className="stat-card status-baca">
            <h3>Sedang Dibaca</h3>
            <p className="stat-number">{stats.baca}</p>
            <p className="stat-percent">{stats.percentBaca.toFixed(0)}%</p>
          </div>
          <div className="stat-card status-beli">
            <h3>Ingin Dibeli</h3>
            <p className="stat-number">{stats.beli}</p>
            <p className="stat-percent">{stats.percentBeli.toFixed(0)}%</p>
          </div>
        </div>

        <div className="author-stats">
          <h3>Buku per Penulis</h3>
          {Object.keys(stats.byAuthor).length === 0 ? (
            <p className="empty-state">Belum ada data.</p>
          ) : (
            <ul>
              {Object.entries(stats.byAuthor).map(([author, count]) => (
                <li key={author}>
                  <span>{author}</span>
                  <span className="count">{count}</span>
                </li>
              ))}
            </ul>
          )}
        </div>
      </main>
    </div>
  );
}

export default Stats;