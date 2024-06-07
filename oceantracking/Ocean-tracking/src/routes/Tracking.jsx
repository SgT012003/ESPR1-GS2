import React, { useState, useEffect } from 'react';
import '../css/style.scss';

function Tracking() {
    const [boias, setBoia] = useState([]);
    const [pagina, setPagina] = useState(0);

    useEffect(() => {
        fetch(`http://127.0.0.1:5000/?page=${pagina}`)
            .then((resp) => {
                if (!resp.ok) {
                    throw new Error('Erro na resposta da rede');
                }
                return resp.json();
            })
            .then((data) => {
                if (Array.isArray(data)) {
                    setBoia(data);
                } else {
                    throw new Error('Dados não são um array');
                }
            })
            .catch((error) => {
                console.error("Erro ao buscar dados:", error);
                setBoia([]); // Definindo como um array vazio em caso de erro
            });
    }, [pagina]);

    const avancarPagina = () => {
        setPagina((prevPagina) => prevPagina + 1);
    };

    const retrocederPagina = () => {
        setPagina((prevPagina) => Math.max(prevPagina - 1, 0));
    };

    return (
        <>
            <section>
                <h1 className='white'>Dados do Oceano</h1>
            </section>
            <section>
                <table className="table table-striped table-dark">
                    <thead>
                        <tr>
                            <th scope="col">Data</th>
                            <th scope="col">Impurezas</th>
                            <th scope="col">Latitude</th>
                            <th scope="col">Longitude</th>
                            <th scope="col">Temp.Água</th>
                            <th scope="col">Temp.Amb</th>
                            <th scope="col">Turbidez</th>
                            <th scope="col">Umidade</th>
                        </tr>
                    </thead>
                    <tbody>
                        {boias.map((item, indice) => (
                            <tr key={indice}>
                                <td>{item.data}</td>
                                <td>{item.impurezas} ppm</td>
                                <td>{item.latitude}</td>
                                <td>{item.longitude}</td>
                                <td>{item.temperatura_agua} ºC</td>
                                <td>{item.temperatura_ambiente} ºC</td>
                                <td>{item.turbidez} UNT</td>
                                <td>{item.umidade} %</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </section>
            <section>
                <button className='enviar' onClick={retrocederPagina} disabled={pagina === 0}>Retroceder</button>
                <button className='enviar' onClick={avancarPagina} disabled={boias.length < 25}>Avançar</button>
            </section>
        </>
    );
}

export default Tracking;